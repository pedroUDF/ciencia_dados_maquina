# Nota: Este script é um espelho modular para leitura rápida e organização por fase do CRISP-DM.
# Para executar o pipeline completo com saídas visuais e análises, acesse os notebooks em `notebooks/`.

import joblib
import json
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import HistGradientBoostingClassifier

print("FASE 6: IMPLEMENTAÇÃO E ESCORAGEM EM LOTE\n")

base_url = "https://raw.githubusercontent.com/pedroUDF/ciencia_dados_maquina/main/Projeto_DataScience/data/processed"
df_2023 = pd.read_parquet(f"{base_url}/2023_completo_df.parquet")

def preparar_features_producao(df):
    d = df.copy()
    d["POSSUI_ESCOLA_VINCULADA"] = d["TP_DEPENDENCIA_ADM_ESC"].notna().astype(int)
    d["ESTUDA_FORA_DF"] = (d["SG_UF_ESC"].notna() & (d["SG_UF_ESC"] != "DF")).astype(int)
    d["REDE_ESCOLAR"] = d["TP_DEPENDENCIA_ADM_ESC"].fillna(0).astype(int)
    d["EGRESSO_FORA_FLUXO"] = d["TP_ST_CONCLUSAO"].isin([1, 4]).astype(int)

    mapa_renda = {l: i for i, l in enumerate(list("ABCDEFGHIJKLMNOPQ"))}
    mapa_esc = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": -1}
    mapa_bens = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}

    d["RENDA_ORDINAL"] = d["Q006"].map(mapa_renda)
    d["ESC_PAI_ORDINAL"] = d["Q001"].map(mapa_esc)
    d["ESC_MAE_ORDINAL"] = d["Q002"].map(mapa_esc)
    d["QTD_COMPUTADORES"] = d["Q024"].map(mapa_bens)
    d["ACESSO_INTERNET"] = (d["Q025"] == "B").astype(int)
    d["SEXO_MASC"] = (d["TP_SEXO"] == "M").astype(int)

    cols_B = [
        "TP_FAIXA_ETARIA", "SEXO_MASC", "TP_ESTADO_CIVIL", "TP_COR_RACA", "TP_ST_CONCLUSAO",
        "IN_TREINEIRO", "POSSUI_ESCOLA_VINCULADA", "ESTUDA_FORA_DF", "EGRESSO_FORA_FLUXO",
        "REDE_ESCOLAR", "TP_LINGUA", "RENDA_ORDINAL", "ESC_PAI_ORDINAL", "ESC_MAE_ORDINAL",
        "QTD_COMPUTADORES", "ACESSO_INTERNET"
    ]
    return pd.get_dummies(d[cols_B], columns=["TP_ESTADO_CIVIL", "TP_COR_RACA", "TP_ST_CONCLUSAO", "REDE_ESCOLAR"], dtype=int)

# Filtrar válidos e gerar target para treino completo de produção
validos = df_2023[~((df_2023["TP_PRESENCA_CH"] == 2) | (df_2023["TP_PRESENCA_MT"] == 2))].copy()
y_prod = ((validos["TP_PRESENCA_CH"] == 0) | (validos["TP_PRESENCA_MT"] == 0)).astype(int)
X_prod = preparar_features_producao(validos)

modelo_producao = HistGradientBoostingClassifier(
    max_iter=200, max_depth=6, learning_rate=0.05, class_weight="balanced", random_state=42
)
modelo_producao.fit(X_prod, y_prod)

# Exportar artefato do modelo + contrato de colunas e limiar operacional
artefato = {
    "modelo": modelo_producao,
    "colunas_esperadas": list(X_prod.columns),
    "limiar_operacional": 0.48,
    "limiar_alto_risco": 0.65,
    "versao": "1.0.0-enem-df"
}
joblib.dump(artefato, "modelo_abstencao_enem_df.joblib")
print("Artefato serializado salvo em 'modelo_abstencao_enem_df.joblib'.")

# Simulação de Escoragem em Lote (Batch Scoring) em 10 novos inscritos
amostra_novos = validos.sample(10, random_state=99).copy()
X_novos = preparar_features_producao(amostra_novos).reindex(columns=artefato["colunas_esperadas"], fill_value=0)

scores = modelo_producao.predict_proba(X_novos)[:, 1]
amostra_novos["SCORE_ABSTENCAO"] = scores.round(4)
amostra_novos["FAIXA_RISCO"] = pd.cut(
    scores,
    bins=[-0.01, 0.48, 0.65, 1.01],
    labels=["Baixo Risco (Sem Ação)", "Risco Moderado (Régua Digital)", "Alto Risco (Busca Ativa)"]
)

print("\nAMOSTRA DE SAÍDA DO PIPELINE DE ESCORAGEM EM LOTE (BATCH SCORING)")
print(amostra_novos[["TP_FAIXA_ETARIA", "Q006", "TP_ST_CONCLUSAO", "SCORE_ABSTENCAO", "FAIXA_RISCO"]].to_string(index=False))
