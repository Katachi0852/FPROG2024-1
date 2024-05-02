# Solicitar ao usuário que insira cinco nomes
nomes = []
for i in range(5):
    nome = input("Digite um nome: ")
    nomes.append(nome)

# Encontrar o primeiro nome em ordem alfabética
primeiro_nome = min(nomes)

# Imprimir o primeiro nome em ordem alfabética
print("O primeiro nome em ordem alfabética é:", primeiro_nome)
