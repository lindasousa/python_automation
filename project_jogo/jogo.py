# Importei a biblioteca random para usar as palavras secretas de maneira aleatória
import random

# Lista das palavras definidas para o jogo
palavras = ["PYTHON", "VARIAVEL", "ESCOPO", "LISTA"]

# Função para iniciar o jogo
# Utilizei esta função para escolher a palavra secreta aleatoriamente e preparar o status inicial do jogo com a lista de lacunas vazias ("-")
def inicializar_jogo(lista_palavras):
  """
  Escolhe uma palavra secreta aleatoriamente da lista e gera as lacunas correspondentes.
  
  Argumentos:
      lista_palavras (list): Lista com as strings das palavras do jogo.
      
  Retorna:
      A palavra secreta (str) e a lista de lacunas (list).
  """
  # Variável para de forma aleatória guardar uma palavra da lista
  palavra = random.choice(lista_palavras)
  # Variável que multiplica cada espaço por cada letra da palavra
  lacunas = ["_"] * len(palavra) 
  # Return devolve os resultados da função 
  return palavra, lacunas

# Função para processar a tentativa do usuário (atualizar as letras corretas e retornar verdadeiro ou falso, se o usuário acertou ou se errou)
def processar_tentativa(chute, palavra_secreta, letras_descobertas):
  """
  Verifica se a letra digitada pertence à palavra secreta e atualiza a lista de lacunas.
  
  Argumentos:
      chute (str): Letra digitada pelo usuário.
      palavra_secreta (str): A palavra que deve ser adivinhada.
      letras_descobertas (list): Lista com o status atual das lacunas do jogo.
      
  Retorna:
      bool: True se o jogador acertou a letra, False caso contrário.
  """
  # Se o chute, que é a variável que vai guardar o letra digitada pelo usuário puder preencher algum espaço da palavra secreta atualiza a palavra e retorna verdadeiro,
  # caso contrário retorna falso
  if chute in palavra_secreta:
     for indice, letra in enumerate(palavra_secreta):
        if letra == chute:
           letras_descobertas[indice] = chute  
     return True
  else:
     return False
  
# chamada da função de inicialização
palavra_secreta, letras_descobertas = inicializar_jogo(palavras)
# Criei um conjunto (set) para guardar as letras tentadas
# Escolhi usar conjuntos pois o conjunto guarda a letra uma única vez, a lista pode repetir
letras_tentadas = set()
# Criei uma variável para as tentativas possíveis do jogo
tentativas_restantes = 6
# Exibe a mensagem de entrada do jogo ao usuário
print("BEM-VINDO AO JOGO DA FORCA!")

# Usei o laço de repetição while para rodar as tentativas do jogo e exibir as saídas necessárias para o usuário com diferentes condições
while tentativas_restantes > 0 and "_" in letras_descobertas:

  # Usei o " ".join para juntar os elementos (letras) da lista(palavra) com espaço entre si e exibir o resultado na tela 
  print("\nPalavra:", " ".join(letras_descobertas))

  # Exibe as tentativas restantes quando o usuário erra a letra da palavra
  print(f"Tentativas restantes:  {tentativas_restantes}")

  # Exibe as letras já tentadas, usei ' ,  '.join para as separar as letras entre si por virgula e um espaço
  print(f"Letras já tentadas:  {' ,  '.join(letras_tentadas)}")

  # Criei esta variável para guardar a letra digitada pelo o usuário e exibir a mensagem através do input
  #usei o .upper() para transformar todo o texto digitado em letras maiúsculas
  chute = input("Digite uma letra: ").upper()
  
  # Verifica se a letra (variável chute) que o usuário digitou é algo diferente ou é uma letra, exibirá a mensagem de aviso
  if len(chute) != 1 or not chute.isalpha():
     print("Por favor, digite apenas uma única letra.")
     # Usei continue para continuar o jogo e o usuário digitar de novo
     continue

  # Verifica se a letra está no conjunto (set) das letras já tentadas pelo usuário e exibe a mensagem de aviso
  if chute in letras_tentadas:
     print("Você já tentou essa letra! Tente outra.")
     continue

  # .add(): insere um novo elemento nos conjuntos
  letras_tentadas.add(chute)

  # Chamada da função para processar a tentativa do jogador
  # Esta variável recebe o resultado da função processar tentativa
  acertou = processar_tentativa(chute, palavra_secreta, letras_descobertas)

  # Se o jogador/usuário acertou ou errou exibirá uma mensagem de sucesso na tela 
  if acertou:
     print(f"Muito bem! A letra '{chute}' está na palavra.")
  else:
     print(f"Que pena! A letra '{chute}' não está na palavra.")
     # As tentativas vão diminuindo quando o jogador erra
     tentativas_restantes -= 1

# Se o usuário preencheu todos os espaços, não existindo mais espaços para preencher, a palavra foi descoberta
# Exibirá a mensagem de sucesso na tela.
# De outra forma, quando acabam as tentativas, o usuário perdeu o jogo 
# Exibirá também a mensagem de derrota do jogo na tela.
if "_" not in letras_descobertas:
   print("\nPARABÉNS! VOCÊ VENCEU!")
   print(f"A palavra era:  {palavra_secreta}")
else: 
   print("\nGAME OVER! Você perdeu!")
   print(f"As tentativas acabaram. A palavra secreta era:  {palavra_secreta}")