import pandas as pd

for arq in [
    r".\microdados_enem_2024\DADOS\PARTICIPANTES_2024.csv",
    r".\microdados_enem_2024\DADOS\RESULTADOS_2024.csv",
    r".\microdados_enem_2025\DADOS\RESULTADOS_2025.csv",
]:
    cols = list(pd.read_csv(arq, sep=";", encoding="latin-1", nrows=1).columns)
    print(f"=== {arq} ({len(cols)} cols) ===")
    print(cols, "\n")
