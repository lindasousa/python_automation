## 1. IMPORTAR BIBILIOTECAS

# Manipulação e análise de dados (tabelas)
import pandas as pd

# Banco de dados SQL leve que salva em arquivo
import sqlite3

# Cálculos matemáticos e geração de dados aleatórios
import numpy

#Lidar com datas e horários
from datetime import datetime 


## 2. CONECTAR AO BANCO DE DADOS (SQLITE)

# caminho completo até ao banco de dados
conn = sqlite3.connect(r'C:\Users\linre\Downloads\Ciência da Computação\projeto_sql\projeto_SQL_ecommerce.db')
## 3. EXTRAÇÃO DE DADOS

query = "SELECT * FROM vendas"
df = pd.read_sql_query(query, conn) 
print(f"Total de linhas antes da limpeza: {len(df)}")

## 3. TRANSFORMAÇÃO DOS DADOS
# A. Limpeza de Duplicadas
# O keep='first' mantém a primeira ocorrência e deleta as repetidas
df = df.drop_duplicates(keep='first')
print(f"Total de linhas após remover duplicadas: {len(df)}")

# B. Tratamento de Valores Nulos
# Remove linhas onde o ID do cliente ou o valor da venda estejam vazios
df = df.dropna(subset=['id_venda', 'valor_total'])

# C. Formatação de Datas
# Garante que a coluna de data seja entendida pelo Python como tempo (datetime)
df['data_venda'] = pd.to_datetime(df['data_venda'])

# 4. CARREGAMENTO (Load) 

# Salvando o resultado em uma nova tabela chamada 'tb_rfm_limpa'
# Assim você não mexe nos seus dados originais (boa prática profissional!)
df.to_sql('vendas_limpas', conn, if_exists='replace', index=True)


# 5. Confirmação no terminal do processo concluído com sucesso!
print("✅ Processo concluído! Tabela 'vendas_limpas' pronta para o Power BI.")

# 6. Fechando a conexão para liberar o arquivo
conn.close()
