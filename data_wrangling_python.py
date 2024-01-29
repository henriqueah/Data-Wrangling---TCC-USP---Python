import pandas as pd
df = pd.read_excel("LOA_PPA_PLOA_detalhada.xlsx")

# Ler o Excel com Pandas
df_xlsx = pd.ExcelFile("LOA_PPA_PLOA_detalhada.xlsx")
print(df_xlsx)

# Iterar por cada aba e salvar como CSV
for aba in df_xlsx.sheet_names:
    df = pd.read_excel(df_xlsx, aba)
    # Criar um nome de arquivo CSV baseado no nome da aba
    nome_arquivo_csv = f"{aba}.csv"
    df.to_csv(nome_arquivo_csv, index=False)  # index=False para não incluir o índice do DataFrame no CSV








