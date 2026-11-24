import os
import pandas as pd

os.makedirs("dados_df", exist_ok=True)

arquivos = [
    ("2023_completo", r".\microdados_enem_2023\DADOS\MICRODADOS_ENEM_2023.csv"),
    ("2024_participantes", r".\microdados_enem_2024\DADOS\PARTICIPANTES_2024.csv"),
    ("2024_resultados", r".\microdados_enem_2024\DADOS\RESULTADOS_2024.csv"),
    ("2025_participantes", r".\microdados_enem_2025\DADOS\PARTICIPANTES_2025.csv"),
    ("2025_resultados", r".\microdados_enem_2025\DADOS\RESULTADOS_2025.csv"),
]

resumo = []

for nome, caminho in arquivos:
    print(f"Extraindo DF de: {nome}...")
    total_br = 0
    chunks_df = []

    for chunk in pd.read_csv(caminho, sep=";", encoding="latin-1", chunksize=100_000, low_memory=False):
        total_br += len(chunk)
        df_sub = chunk[chunk["SG_UF_PROVA"] == "DF"].copy()
        if not df_sub.empty:
            chunks_df.append(df_sub)

    df_final = pd.concat(chunks_df, ignore_index=True)
    saida = f"dados_df/{nome}_df.parquet"
    df_final.to_parquet(saida, index=False)

    resumo.append({
        "Base": nome,
        "Total_Brasil": total_br,
        "Total_DF": len(df_final),
        "Perc_DF (%)": round((len(df_final) / total_br) * 100, 2),
        "Colunas": df_final.shape[1],
        "Tamanho_Parquet_MB": round(os.path.getsize(saida) / (1024 * 1024), 2)
    })

print("\n=== RELATÓRIO DA SUBFASE 2.1: COLETA INICIAL (DF) ===")
print(pd.DataFrame(resumo).to_string(index=False))