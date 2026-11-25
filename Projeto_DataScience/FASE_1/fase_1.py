# Nota: Este script é um espelho modular para leitura rápida e organização por fase do CRISP-DM.
# Para executar o pipeline completo com saídas visuais e análises, acesse os notebooks em `notebooks/`.

#Checagem de Colunas
import os
import pandas as pd

# Percorre todas as subpastas dentro de Downloads\ENEM
for raiz, pastas, arquivos in os.walk("."):
    for arq in arquivos:
        if arq.endswith(".csv") and "ITENS" not in arq.upper():
            caminho = os.path.join(raiz, arq)
            tamanho_mb = os.path.getsize(caminho) / (1024 * 1024)
            print(f"Arquivo: {caminho} | Tamanho: {tamanho_mb:.2f} MB")

            # Se não estiver vazio (0 KB), lê apenas as 2 primeiras linhas para ver as colunas
            if tamanho_mb > 0:
                df_head = pd.read_csv(caminho, sep=";", encoding="latin-1", nrows=2)
                print(f"  -> Qtd colunas: {len(df_head.columns)}")
                print(f"  -> Primeiras colunas: {list(df_head.columns[:8])}\n")
            else:
                print("  -> [ALERTA] Arquivo vazio (0 KB)! Precisa reextrair do ZIP.\n")

# Inspeciona as Pastas
import pandas as pd

for arq in [
    r".\microdados_enem_2024\DADOS\PARTICIPANTES_2024.csv",
    r".\microdados_enem_2024\DADOS\RESULTADOS_2024.csv",
    r".\microdados_enem_2025\DADOS\RESULTADOS_2025.csv",
]:
    cols = list(pd.read_csv(arq, sep=";", encoding="latin-1", nrows=1).columns)
    print(f"=== {arq} ({len(cols)} cols) ===")
    print(cols, "\n")

# Extrai os DataFrame final
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

print("\nRELATÓRIO COLETA INICIAL (DF)")
print(pd.DataFrame(resumo).to_string(index=False))
