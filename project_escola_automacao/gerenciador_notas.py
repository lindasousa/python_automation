#A função 1 vai calcular a média das notas, esta função recebe uma lista de notas flutuantes e retorna o seu valor médio
def calcular_media(notas):

  #o len conta as notas da lista, se a lista tiver vazia, para evitar erro, retorna 0
  if len(notas) == 0:
    return 0.0
  #declaração de variáveis, len para contagem das notas de cada aluno e cálculo da média
  soma_das_notas = sum(notas)
  quantidade_de_notas = len(notas)
  media = soma_das_notas / quantidade_de_notas
  return media


#A função 2 vai verificar a aprovação do aluno com base na media das de todas as notas, a função recebe a média obtida e a média mínima
#Esta função vai funcionar tendo em conta as condicionais para aprovação, como a media mínima de 7.0 para aprovação
#Após a avaliação automatizada com condicionais, a função retornará em string com exatidão 'Aprovado' ou 'Reprovado', pelo valor booleano True ou False
def verificar_aprovacao(media, media_minima=7.0):
  #Se a média mínima for maior ou igual a 7.0 o aluno é Aprovado, se não é Reprovado
  if media >= media_minima:
    print("Aprovado")
    return True 
  else:
    print("Reprovado")
    return False


#A função 3 será capaz de receber a estrutura completa de estudantes e apresentar no terminal o nome, a respectiva média processada
# e a situação de aprovação de cada um de forma nítida e organizada
def gerar_relatorio(alunos):
  #Título do relatório
  print("\n========================================")
  print("    RELATÓRIO DE DESEMPENHO ACADÊMICO   ")
  print("========================================")
  #Para aluno em alunos declarei as variáveis necessárias para o relatório (o nome, média e aprovação ou não de cada   aluno)
  for aluno in alunos:
    nome = aluno["nome"]
    media = aluno["media"]
  #Se o aluno for aprovado retorna True situação Aprovada no relatório e se for reprovado o contrário
  #Todas as informações necessárias do relatório, para o usuário, serão exibidas na tela
    if aluno["aprovado"] == True:
      situacao = "Aprovado"
    else:
      situacao = "Reprovado"
    print(f"Aluno(a): {nome}")
    print(f"Média...: {media:.2f}")
    print(f"Situação: {situacao}")
    print("----------------------------------------")

#inputs para o usuário digitar os dados de cada aluno 
nome = input("Indique o nome do aluno: ")
turma = input("Indique a turma do aluno (A ou B): ")
curso = input("Indique o curso do aluno: ")
notas = float(input("Indique a nota do aluno (0-10): "))

#lista com dicionário para o armazenamento chave/valor de cada aluno/atributos necessários
lista_alunos = [
  {
     "nome": nome,
     "turma": turma,
     "curso": curso,
     "notas": [],
     "media": 0.0,
     "aprovado": True
  }
]