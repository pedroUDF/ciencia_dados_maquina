# Nota: Este script é um espelho modular para leitura rápida e organização por fase do CRISP-DM.
# Para executar o pipeline completo com saídas visuais e análises, acesse os notebooks em `notebooks/`.

#2.1
import pandas as pd

# Carrega os arquivos
df_2023 = pd.read_parquet("2023_completo_df.parquet")
df_2024_part = pd.read_parquet("2024_participantes_df.parquet")
df_2024_res = pd.read_parquet("2024_resultados_df.parquet")
df_2025_part = pd.read_parquet("2025_participantes_df.parquet")
df_2025_res = pd.read_parquet("2025_resultados_df.parquet")

bases = {
    "2023_Completo": df_2023,
    "2024_Participantes": df_2024_part,
    "2024_Resultados": df_2024_res,
    "2025_Participantes": df_2025_part,
    "2025_Resultados": df_2025_res,
}

print("--- 1. TIPOS DE DADOS POR BASE ---")
for nome, df in bases.items():
    tipos = df.dtypes.value_counts().to_dict()
    tipos_str = {str(k): v for k, v in tipos.items()}
    print(f"{nome}: {df.shape[0]} linhas x {df.shape[1]} colunas | Tipos: {tipos_str}")

print("\n--- 2. CÓDIGOS DE PRESENÇA NOS DIAS DE PROVA (DF) ---")
# Códigos INEP: 0 = Faltou à prova | 1 = Presente na prova | 2 = Eliminado na prova
for ano, df in [(2023, df_2023), (2024, df_2024_res), (2025, df_2025_res)]:
    print(f"\n--- ENEM {ano} (Total DF: {len(df)}) ---")
    print("Dia 1 (Ciências Humanas - TP_PRESENCA_CH):")
    print(df["TP_PRESENCA_CH"].value_counts(dropna=False).sort_index())
    print("Dia 2 (Matemática - TP_PRESENCA_MT):")
    print(df["TP_PRESENCA_MT"].value_counts(dropna=False).sort_index())

#2.2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

base_url = "https://raw.githubusercontent.com/pedroUDF/ciencia_dados_maquina/main/Projeto_DataScience/data/processed"

try:
    df_2023 = pd.read_parquet(f"{base_url}/2023_completo_df.parquet")
    df_2024_res = pd.read_parquet(f"{base_url}/2024_resultados_df.parquet")
    df_2025_res = pd.read_parquet(f"{base_url}/2025_resultados_df.parquet")
    print("Bases carregadas com sucesso!")
except Exception:
    df_2023 = pd.read_parquet("2023_completo_df.parquet")
    df_2024_res = pd.read_parquet("2024_resultados_df.parquet")
    df_2025_res = pd.read_parquet("2025_resultados_df.parquet")
    print("Bases carregadas do ambiente local do Colab!")

sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(16, 11))
fig.suptitle("Subfase 2.3: Análise Exploratória da Abstenção no ENEM (DF | 2023–2025)", fontsize=15, fontweight="bold")

# GRÁFICO 1: Evolução da Abstenção por Dia e Ano (2023-2025)
dados_anos = []
for ano, df in [(2023, df_2023), (2024, df_2024_res), (2025, df_2025_res)]:
    abst_d1 = (df["TP_PRESENCA_CH"] == 0).mean() * 100
    abst_d2 = (df["TP_PRESENCA_MT"] == 0).mean() * 100
    abst_geral = ((df["TP_PRESENCA_CH"] == 0) | (df["TP_PRESENCA_MT"] == 0)).mean() * 100
    dados_anos.append({
        "Ano": str(ano),
        "Dia 1 (CH/LC)": abst_d1,
        "Dia 2 (MT/CN)": abst_d2,
        "Pelo menos 1 dia": abst_geral
    })

df_evol = pd.DataFrame(dados_anos)
df_evol_melt = df_evol.melt(id_vars="Ano", var_name="Métrica", value_name="Taxa (%)")

sns.barplot(data=df_evol_melt, x="Ano", y="Taxa (%)", hue="Métrica", ax=axes[0, 0], palette="viridis")
axes[0, 0].set_title("1. Evolução da Abstenção no DF (2023–2025)")
axes[0, 0].set_ylim(0, 40)
for container in axes[0, 0].containers:
    axes[0, 0].bar_label(container, fmt="%.1f%%", fontsize=9, padding=2)

# GRÁFICO 2: Abstenção por Dependência Administrativa da Escola (2023-2025)
mapa_dep = {1.0: "Federal", 2.0: "Estadual/DF", 3.0: "Municipal", 4.0: "Privada"}
lista_dep = []
for ano, df in [(2023, df_2023), (2024, df_2024_res), (2025, df_2025_res)]:
    temp = df.copy()
    temp["Rede_Escola"] = temp["TP_DEPENDENCIA_ADM_ESC"].map(mapa_dep).fillna("Sem vínculo / Egresso")
    temp["Abstencao_Geral"] = ((temp["TP_PRESENCA_CH"] == 0) | (temp["TP_PRESENCA_MT"] == 0)).astype(int)
    grp = temp.groupby("Rede_Escola")["Abstencao_Geral"].mean().reset_index()
    grp["Ano"] = str(ano)
    grp["Taxa (%)"] = grp["Abstencao_Geral"] * 100
    lista_dep.append(grp)

df_dep = pd.concat(lista_dep)
sns.barplot(data=df_dep, x="Rede_Escola", y="Taxa (%)", hue="Ano", ax=axes[0, 1], palette="magma")
axes[0, 1].set_title("2. Abstenção (≥1 dia) por Rede Escolar no DF")
axes[0, 1].tick_params(axis="x", rotation=15)
axes[0, 1].set_ylim(0, 45)

# GRÁFICO 3: Abstenção por Renda Familiar (Q006 - Base Completa 2023)
df_2023_eda = df_2023.copy()
df_2023_eda["Abstencao_Geral"] = ((df_2023_eda["TP_PRESENCA_CH"] == 0) | (df_2023_eda["TP_PRESENCA_MT"] == 0)) * 100
renda_grp = df_2023_eda.groupby("Q006", as_index=False)["Abstencao_Geral"].mean().sort_values("Q006")

sns.lineplot(data=renda_grp, x="Q006", y="Abstencao_Geral", marker="o", linewidth=2.5, color="#d95f02", ax=axes[1, 0])
axes[1, 0].set_title("3. Abstenção por Faixa de Renda Q006 (A=Nenhuma até Q=+20 SM | 2023)")
axes[1, 0].set_xlabel("Faixa de Renda Familiar (Q006)")
axes[1, 0].set_ylabel("Taxa de Abstenção (%)")
axes[1, 0].set_ylim(0, 55)

# GRÁFICO 4: Abstenção por Situação de Conclusão do Ensino Médio (2023)
mapa_conc = {
    1: "Já concluí o EM",
    2: "Concluindo em 2023",
    3: "Concluindo após 2023",
    4: "Não concluí / Não cursando"
}
df_2023_eda["Situacao_EM"] = df_2023_eda["TP_ST_CONCLUSAO"].map(mapa_conc)
conc_grp = df_2023_eda.groupby("Situacao_EM", as_index=False)["Abstencao_Geral"].mean().sort_values("Abstencao_Geral", ascending=False)

sns.barplot(data=conc_grp, x="Situacao_EM", y="Abstencao_Geral", ax=axes[1, 1], palette="coolwarm")
axes[1, 1].set_title("4. Abstenção por Situação no Ensino Médio (DF | 2023)")
axes[1, 1].tick_params(axis="x", rotation=15)
axes[1, 1].set_ylim(0, 45)
for container in axes[1, 1].containers:
    axes[1, 1].bar_label(container, fmt="%.1f%%", fontsize=9, padding=2)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

print("\n=== TABELA RESUMO: EVOLUÇÃO DA ABSTENÇÃO NO DF (2023–2025) ===")
print(df_evol.round(2).to_string(index=False))

#2.3
import pandas as pd

print("AUDITORIA DE QUALIDADE DOS DADOS\n")

# Percentual de nulos nas variáveis nos 3 anos (2023-2025)
cols_comuns = [
    "CO_MUNICIPIO_ESC", "SG_UF_ESC", "TP_DEPENDENCIA_ADM_ESC",
    "TP_LOCALIZACAO_ESC", "TP_SIT_FUNC_ESC", "CO_MUNICIPIO_PROVA",
    "TP_PRESENCA_CN", "TP_PRESENCA_CH", "TP_PRESENCA_LC", "TP_PRESENCA_MT", "TP_LINGUA"
]

nulos_resumo = {}
for ano, df in [(2023, df_2023), (2024, df_2024_res), (2025, df_2025_res)]:
    nulos_resumo[f"Nulos_{ano} (%)"] = (df[cols_comuns].isna().mean() * 100).round(2)

print("-1. TAXA DE VALORES OMISSOS (NaN) NAS VARIÁVEIS COMUNS (2023–2025)")
print(pd.DataFrame(nulos_resumo).to_string())

# Verificar casos da categoria 'Municipal' (código 3) no DF
print("\n2. AUDITORIA DA CATEGORIA 'MUNICIPAL' (TP_DEPENDENCIA_ADM_ESC == 3)")
for ano, df in [(2023, df_2023), (2024, df_2024_res), (2025, df_2025_res)]:
    mun = df[df["TP_DEPENDENCIA_ADM_ESC"] == 3]
    print(f"{ano}: {len(mun)} registros | UFs de origem: {mun['SG_UF_ESC'].value_counts().to_dict()}")

# Inconsistências de presença (ex: presente em CH mas faltou em LC no mesmo dia)
print("\n 3. INCONSISTÊNCIAS DE PRESENÇA NO MESMO DIA")
for ano, df in [(2023, df_2023), (2024, df_2024_res), (2025, df_2025_res)]:
    diff_d1 = (df["TP_PRESENCA_CH"] != df["TP_PRESENCA_LC"]).sum()
    diff_d2 = (df["TP_PRESENCA_CN"] != df["TP_PRESENCA_MT"]).sum()
    print(f"{ano}: Divergência Dia 1 (CH != LC) = {diff_d1} | Divergência Dia 2 (CN != MT) = {diff_d2}")

# Nulos na base socioeconômica completa de 2023
print("\n 4. NULOS NAS VARIÁVEIS SOCIOECONÔMICAS (2023)")
cols_socio = ["TP_FAIXA_ETARIA", "TP_SEXO", "TP_ESTADO_CIVIL", "TP_COR_RACA", "TP_ST_CONCLUSAO", "IN_TREINEIRO", "Q001", "Q002", "Q006", "Q024", "Q025"]
print((df_2023[cols_socio].isna().mean() * 100).round(2).to_string())
