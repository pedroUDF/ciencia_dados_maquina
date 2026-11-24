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