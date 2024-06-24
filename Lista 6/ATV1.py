import random

# Função para criar um vetor de 10 números aleatórios entre 10 e 90
def criar_vetor():
    return [random.randint(10, 90) for _ in range(10)]

# Função para imprimir o vetor
def imprimir_vetor(vetor):
    print("Vetor:", vetor)

# Função para verificar se o valor 50 está presente no vetor
def verificar_50(vetor):
    if 50 in vetor:
        print("O valor 50 foi encontrado no vetor.")
    else:
        print("O valor 50 não foi encontrado no vetor.")

# Função para contar o número de ocorrências do valor 50 no vetor
def contar_50(vetor):
    return vetor.count(50)

# Função para calcular a média dos valores do vetor
def calcular_media(vetor):
    return sum(vetor) / len(vetor)

# Função para encontrar o maior e o menor valor do vetor
def encontrar_maior_menor(vetor):
    return max(vetor), min(vetor)

# Função para imprimir a soma e o produto acumulado dos valores do vetor
def soma_produto(vetor):
    soma = sum(vetor)
    produto = 1
    for num in vetor:
        produto *= num
    print("Soma dos valores:", soma)
    print("Produto acumulado dos valores:", produto)

# Função para imprimir o vetor em ordem inversa
def imprimir_inverso(vetor):
    print("Vetor em ordem inversa:", vetor[::-1])

# Função para copiar os elementos em ordem inversa para outro vetor
def copiar_inverso(vetor):
    return vetor[::-1]

# Função para separar elementos pares e ímpares em vetores distintos
def separar_pares_impares(vetor):
    pares = [num for num in vetor if num % 2 == 0]
    impares = [num for num in vetor if num % 2 != 0]
    return pares, impares

# Criando o vetor inicial
vetor = criar_vetor()

# a. Imprimir o vetor
imprimir_vetor(vetor)

# b. Verificar se o valor 50 está presente no vetor
verificar_50(vetor)

# c. Verificar o número de ocorrências do valor 50 no vetor
ocorrencias_50 = contar_50(vetor)
print("Número de ocorrências do valor 50:", ocorrencias_50)

# d. Calcular a média dos valores do vetor
media = calcular_media(vetor)
print("Média dos valores do vetor:", media)

# e. Encontrar o maior e o menor valor do vetor
maior, menor = encontrar_maior_menor(vetor)
print("Maior valor do vetor:", maior)
print("Menor valor do vetor:", menor)

# f. Imprimir a soma e o produto acumulado dos valores do vetor
soma_produto(vetor)

# g. Imprimir o vetor em ordem inversa
imprimir_inverso(vetor)

# h. Copiar os elementos em ordem inversa para outro vetor
vetor_inverso = copiar_inverso(vetor)
print("Vetor copiado em ordem inversa:", vetor_inverso)

# i. Separar elementos pares e ímpares em vetores distintos
vetor_pares, vetor_impares = separar_pares_impares(vetor)
print("Vetor de números pares:", vetor_pares)
print("Vetor de números ímpares:", vetor_impares)
