import pandas as pd
import numpy as np

df_limites = pd.read_excel('OneDrive\\Documentos\\Felipe\\Codes\\qrt\\STATS DATA\\stats_xle.xlsx', usecols='A:I')
df_clean_1 = pd.read_excel('OneDrive\\Documentos\\Felipe\\Codes\\qrt\\PERFORMANCE DATA\\depuracion_performance\\depuracion_xle.xlsx',sheet_name=5, skiprows=4)
columnas = df_clean_1.columns.difference(['Date','Total','Close'])
df_dates_1 = pd.DataFrame(data = columnas)
df_dates_1.insert(1,'Fecha de corte',np.nan)

df_clean_2 = pd.read_excel('OneDrive\\Documentos\\Felipe\\Codes\\qrt\\PERFORMANCE DATA\\depuracion_performance\\depuracion_xle.xlsx',sheet_name=5, skiprows=4)
df_dates_2 = pd.DataFrame(data = columnas)
df_dates_2.insert(1,'Fecha de corte',np.nan)

Inf1 = df_limites.at[3, 'Inf1']
Inf2 = df_limites.at[3, 'Inf2']
index_col = 0

for col in columnas:
    i=df_clean_1[col].le(Inf1).idxmax()
    j=df_clean_2[col].le(Inf2).idxmax()
    if i != 0:
        df_clean_1.loc[i:, col] = 0
        df_dates_1.loc[index_col, 'Fecha de corte'] = df_clean_1.loc[i,'Date']
        if j != 0:
            df_clean_2.loc[j:, col] = 0
            df_dates_2.loc[index_col, 'Fecha de corte'] = df_clean_2.loc[j,'Date']
    index_col+=1

df_clean_1.drop(columns=['Total'], inplace=True)
df_clean_1.insert(1, 'Total' ,0)
df_clean_1['Total'] = df_clean_1.iloc[:,3:].sum(axis=1)
df_dates_1.rename(columns={0:'Trade'},inplace=True)

df_clean_2.drop(columns=['Total'], inplace=True)
df_clean_2.insert(1, 'Total' ,0)
df_clean_2['Total'] = df_clean_2.iloc[:,3:].sum(axis=1)
df_dates_2.rename(columns={0:'Trade'},inplace=True)

df_clean_1.to_csv('OneDrive\\Documentos\\Felipe\\Codes\\qrt\\python_output\\xle_corte1.csv', index=False)
df_dates_1.to_csv('OneDrive\\Documentos\\Felipe\\Codes\\qrt\\python_output\\xle_fechascorte1.csv',index=False)
df_clean_2.to_csv('OneDrive\\Documentos\\Felipe\\Codes\\qrt\\python_output\\xle_corte2.csv', index=False)
df_dates_2.to_csv('OneDrive\\Documentos\\Felipe\\Codes\\qrt\\python_output\\xle_fechascorte2.csv', index=False)