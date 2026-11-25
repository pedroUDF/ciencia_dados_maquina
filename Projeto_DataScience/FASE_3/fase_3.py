# Nota: Este script é um espelho modular para leitura rápida e organização por fase do CRISP-DM.
# Para executar o pipeline completo com saídas visuais e análises, acesse os notebooks em `notebooks/`.

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import os

print("FASE 3: PREPARAÇÃO DOS DADOS (CRISP-DM)\n")

base_url = "https://raw.githubusercontent.com/pedroUDF/ciencia_dados_maquina/main/Projeto_DataScience/data/processed"

try:
    df_2023 = pd.read_parquet(f"{base_url}/2023_completo_df.parquet")
    df_2024_res = pd.read_parquet(f"{base_url}/2024_resultados_df.parquet")
    df_2025_res = pd.read_parquet(f"{base_url}/2025_resultados_df.parquet")
    print("[OK] Bases carregadas diretamente do GitHub.")
except Exception:
    df_2023 = pd.read_parquet("2023_completo_df.parquet")
    df_2024_res = pd.read_parquet("2024_resultados_df.parquet")
    df_2025_res = pd.read_parquet("2025_resultados_df.parquet")
    print("[OK] Bases carregadas do ambiente local do Colab.")

# Função principal (limpeza e eng)
def preparar_base_estrutural(df, ano):
    dados = df.copy()
    dados["ANO"] = ano

    # Remover eliminados (código 2) para manter o que importa, Presente vs. Abstente
    mask_eliminados = (dados["TP_PRESENCA_CH"] == 2) | (dados["TP_PRESENCA_MT"] == 2)
    qtd_elim = mask_eliminados.sum()
    dados = dados[~mask_eliminados].copy()

    # Definição da Target: 1 = faltou em pelo menos 1 dia | 0 = presente nos 2 dias
    dados["ABSTENCAO"] = ((dados["TP_PRESENCA_CH"] == 0) | (dados["TP_PRESENCA_MT"] == 0)).astype(int)

    # Engenharia de Atributos (antes dos nulos)
    dados["POSSUI_ESCOLA_VINCULADA"] = dados["TP_DEPENDENCIA_ADM_ESC"].notna().astype(int)
    dados["ESTUDA_FORA_DF"] = (
        dados["SG_UF_ESC"].notna() & (dados["SG_UF_ESC"] != "DF")
    ).astype(int)

    # Tratamento dos nulos estruturai e agrupamento da anomalia 'Municipal' (3.0)
    # 0 = Sem vínculo escolar | 1 = Federal | 2 = Estadual/DF | 3 = Outras/Fora DF (Municipal) | 4 = Privada
    dados["REDE_ESCOLAR"] = dados["TP_DEPENDENCIA_ADM_ESC"].fillna(0).astype(int)
    dados["LOCALIZACAO_ESC"] = dados["TP_LOCALIZACAO_ESC"].fillna(0).astype(int)  # 0=Sem vínculo, 1=Urbana, 2=Rural
    dados["SIT_FUNC_ESC"] = dados["TP_SIT_FUNC_ESC"].fillna(0).astype(int)        # 0=Sem vínculo, 1=Em atividade...
    dados["UF_ESCOLA_CAT"] = dados["SG_UF_ESC"].fillna("SEM_VINCULO").apply(
        lambda x: x if x in ["DF", "GO", "SEM_VINCULO"] else "OUTRA_UF"
    )
    dados["TP_LINGUA"] = dados["TP_LINGUA"].astype(int)

    # Seleção final de features sem data leakage
    features_estruturais = [
        "ANO",
        "POSSUI_ESCOLA_VINCULADA",
        "ESTUDA_FORA_DF",
        "REDE_ESCOLAR",
        "LOCALIZACAO_ESC",
        "SIT_FUNC_ESC",
        "UF_ESCOLA_CAT",
        "TP_LINGUA",
        "ABSTENCAO"
    ]

    print(f"[{ano}] Registros válidos: {len(dados):,} (Eliminados removidos: {qtd_elim}) | Taxa Abstenção: {dados['ABSTENCAO'].mean()*100:.2f}%")
    return dados[features_estruturais]


print("\n--- 1. PREPARANDO DATASET A: SÉRIE TEMPORAL UNIFICADA (2023–2025) ---")
prep_2023_est = preparar_base_estrutural(df_2023, 2023)
prep_2024_est = preparar_base_estrutural(df_2024_res, 2024)
prep_2025_est = preparar_base_estrutural(df_2025_res, 2025)

# Integração Vertical (Concatenação 2023 + 2024 + 2025)
df_serie_temporal = pd.concat([prep_2023_est, prep_2024_est, prep_2025_est], ignore_index=True)

# Formatação (One-Hot Encoding nas categóricas nominais sem data leakage)
cols_ohe_A = ["REDE_ESCOLAR", "LOCALIZACAO_ESC", "SIT_FUNC_ESC", "UF_ESCOLA_CAT"]
df_serie_encoded = pd.get_dummies(df_serie_temporal, columns=cols_ohe_A, drop_first=False, dtype=int)

# Divisão Temporal (Out-of-Time): Treino (2023-2024) vs. Teste (2025)
train_A = df_serie_encoded[df_serie_encoded["ANO"].isin([2023, 2024])].drop(columns=["ANO"])
test_A = df_serie_encoded[df_serie_encoded["ANO"] == 2025].drop(columns=["ANO"])

print(f"\n[Dataset A - Série Temporal] Shape Treino (2023-2024): {train_A.shape} | Shape Teste OOT (2025): {test_A.shape}")


# DATASET B: MODELO SOCIOECONÔMICO RICO (BASE COMPLETA 2023)

print("\n--- 2. PREPARANDO DATASET B: PERFIL SOCIOECONÔMICO COMPLETO (2023) ---")
dados_23 = df_2023.copy()

# Remover eliminados
mask_elim_23 = (dados_23["TP_PRESENCA_CH"] == 2) | (dados_23["TP_PRESENCA_MT"] == 2)
dados_23 = dados_23[~mask_elim_23].copy()
dados_23["ABSTENCAO"] = ((dados_23["TP_PRESENCA_CH"] == 0) | (dados_23["TP_PRESENCA_MT"] == 0)).astype(int)

# Engenharia de Atributos Escolares e Demográficos
dados_23["POSSUI_ESCOLA_VINCULADA"] = dados_23["TP_DEPENDENCIA_ADM_ESC"].notna().astype(int)
dados_23["ESTUDA_FORA_DF"] = (dados_23["SG_UF_ESC"].notna() & (dados_23["SG_UF_ESC"] != "DF")).astype(int)
dados_23["REDE_ESCOLAR"] = dados_23["TP_DEPENDENCIA_ADM_ESC"].fillna(0).astype(int)
dados_23["EGRESSO_FORA_FLUXO"] = dados_23["TP_ST_CONCLUSAO"].isin([1, 4]).astype(int)

# Mapeamento Ordinal das Variáveis Socioeconômicas (preservando ordem de grandeza)
mapa_renda = {letra: idx for idx, letra in enumerate(list("ABCDEFGHIJKLMNOPQ"))}  # 0 (Nenhuma) a 16 (+20 SM)
mapa_esc_pais = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": -1}  # -1 = Não sei
mapa_bens = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

dados_23["RENDA_ORDINAL"] = dados_23["Q006"].map(mapa_renda)
dados_23["ESC_PAI_ORDINAL"] = dados_23["Q001"].map(mapa_esc_pais)
dados_23["ESC_MAE_ORDINAL"] = dados_23["Q002"].map(mapa_esc_pais)
dados_23["QTD_COMPUTADORES"] = dados_23["Q024"].map(mapa_bens)
dados_23["ACESSO_INTERNET"] = (dados_23["Q025"] == "B").astype(int)
dados_23["SEXO_MASC"] = (dados_23["TP_SEXO"] == "M").astype(int)

features_B = [
    "TP_FAIXA_ETARIA",
    "SEXO_MASC",
    "TP_ESTADO_CIVIL",
    "TP_COR_RACA",
    "TP_ST_CONCLUSAO",
    "IN_TREINEIRO",
    "POSSUI_ESCOLA_VINCULADA",
    "ESTUDA_FORA_DF",
    "EGRESSO_FORA_FLUXO",
    "REDE_ESCOLAR",
    "TP_LINGUA",
    "RENDA_ORDINAL",
    "ESC_PAI_ORDINAL",
    "ESC_MAE_ORDINAL",
    "QTD_COMPUTADORES",
    "ACESSO_INTERNET",
    "ABSTENCAO"
]

df_socio_2023 = dados_23[features_B].copy()

# One-Hot Encoding para categóricas nominais
cols_ohe_B = ["TP_ESTADO_CIVIL", "TP_COR_RACA", "TP_ST_CONCLUSAO", "REDE_ESCOLAR"]
df_socio_encoded = pd.get_dummies(df_socio_2023, columns=cols_ohe_B, drop_first=False, dtype=int)

# Divisão Estratificada 80/20
train_B, test_B = train_test_split(
    df_socio_encoded, test_size=0.20, random_state=42, stratify=df_socio_encoded["ABSTENCAO"]
)

print(f"[Dataset B - Socioeconômico 2023] Shape Treino (80%): {train_B.shape} | Shape Teste (20%): {test_B.shape}")

# SALVANDO OS DATASETS (FASE 4)
os.makedirs("dados_modelagem", exist_ok=True)
train_A.to_parquet("dados_modelagem/train_serie_A.parquet", index=False)
test_A.to_parquet("dados_modelagem/test_serie_A.parquet", index=False)
train_B.to_parquet("dados_modelagem/train_socio_B.parquet", index=False)
test_B.to_parquet("dados_modelagem/test_socio_B.parquet", index=False)

print("\n[SUCESSO] Todos os 4 conjuntos prontos para modelagem foram salvos em 'dados_modelagem/'!")
print("Nulos residuais em train_A:", train_A.isna().sum().sum(), "| train_B:", train_B.isna().sum().sum())
