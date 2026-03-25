# # 1. Importar bibliotecas
import shutil

import os

# # 2. Caminhos das variáveis
origem = r"C:\Users\nome\Desktop\dados"
destino_pasta = r"C:\Users\nome\Desktop\centraldedados"
destino_final = r"C:\Users\nome\Desktop\centraldedados\dados"

# # 3. Lógica de automação
try:
    if not os.path.exists(destino_pasta):
         os.makedirs(destino_pasta)
         print(f"Pasta {destino_pasta} criada com sucesso.")
    shutil.move(origem, destino_final)
    print("Sucesso! O arquivo foi movido pelo robô.")
except FileNotFoundError:
    print("Erro: O arquivo original não foi encontrado na Área de Trabalho.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
