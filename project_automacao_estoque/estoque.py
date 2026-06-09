# Estoque: Visualização de Dicionário em que a chave é o nome do produto.
# Justificativa do uso de um Dicionário: optei por usar um dicionário onde a chave é o nome do produto. Pois em um
# sistema de estoque as operações mais comuns são verificar a existência de um item e pesquisar pelo nome do  item.

estoque = {
     "Notebook": {
        "quantidade": 15,
        "preco": 3500.00
     },
     "Mouse Sem Fio": {
        "quantidade": 50,
        "preco": 85.90
     },
     "Teclado Mecânico": {
        "quantidade": 30,
        "preco": 250.00
     }
}

# Estoque usando o laço de repetição while com os prints necessários para formar o menu
# A condição é sempre verdadeira então o código abaixo vai rodar repetidamente até encontrar o break
while True:
# Os prints servem para a interface, desenhando um menu legível e organizado para o usuário
   print("\n" + "="*30) #Imprime a linha separadora com 30 sinais de igual
   print("   SISTEMA DE GESTÃO DE ESTOQUE") #Exibe o título
   print("="*30) # linha separadora
   print("1 - Visualizar Estoque Atual") # mostra a opção 1
   print("2 - Registrar Entrada de Produto") # mostra a opção 2
   print("3 - Registrar Saída de Produto") # mostra a opção 3
   print("4 - Sair do Sistema") # mostra a opção 4
   print("="*30) #Linha para fechar o menu

# Variável com mensagem (input) para o usuário escolher a opção que deseja para seguir o fluxo dos outros inputs
# Todos os inputs estão devidamente identificados com o tipo de dado necessário
   opcao = int(input("Escolha uma opção (1-4): "))

# Se o usuário escolher a opção 1 será exibido o menu com o estoque atual
   if opcao == 1:
      print("\n ESTOQUE ATUAL")
# Para todos os produtos em estoque organizei por nome do produto, quantidade e preço
      for prod, info in estoque.items():
        print(f"Produto: {prod}, Quantidade: {info['quantidade']}, Preço: R${info['preco']:.2f}")

# Se o usuário escolher a opção 2 será exibida uma mensagem para o usuário registrar a entrada do produto
# O registro é composto por 2 vertentes: nome do produto e a quantidade do produto que está entrando
# Usei elif
   elif opcao == 2:
      print("\n REGISTRAR ENTRADA DE PRODUTO")
      produto = input("Digite o nome do produto: ")
      quantidade_entrada = int(input("Digite a quantidade que está entrando: "))
# Implementação da verificação: se o produto estiver em estoque vai somar a quantidade de entrada
# No final retorna o usuário
      if produto in estoque:
          estoque[produto]["quantidade"] += quantidade_entrada
          print(f"Sucesso! Foram adicionadas {quantidade_entrada} unidades ao estoque de {produto}")
      else: 
          print("Produto não encontrado")

# Se o usuário escolher a opção 3 será exibida uma mensagem para o usuário registrar a saída do produto
# O registro é composto por 2 vertentes: nome do produto e a quantidade do produto que está saindo
   elif opcao == 3:
      print("\n REGISTRAR SAÍDA DE PRODUTO")
      produto = input("Digite o nome do produto: ")
      quantidade_saida = int(input("Digite a quantidade que está saindo: "))
      if produto in estoque:
         #Validação se a quantidade do estoque está disponível, atualização e quantidade de unidades retiradas pelo usuário
         if estoque[produto]["quantidade"] >= quantidade_saida:
                   estoque[produto]["quantidade"] -= quantidade_saida
                   print(f"Sucesso! Retiradas {quantidade_saida} unidades do estoque de {produto}.")
                   print(f"Saldo atualizado de {produto}: {estoque[produto]['quantidade']} unidades.")
         else:
                   # Erro: Mensagem que aparece para o usuário quando tenta tirar mais do que o disponível
                   print("Estoque insuficiente")
                   
# Se o usuário escolher a opção 4 o sistema vai encerrar e será exibida a mensagem de encerramento do sistema
# O sistema encerra
   elif opcao == 4:
      print("\nSistema encerrado.")
      break
      # Se o usuário digitar uma opção inválida surgirá uma mensagem de erro informando o usuário
   else: 
      print("\nOpção inválida! Por favor, escolha um número de 1 a 4.")