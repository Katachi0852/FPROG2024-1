import random

# A. Gerar e escrever todos os números inteiros do intervalo [0,100]
print('Números inteiros de 0 a 100: ')
for num in range(101):
    print(num,end='')
print('\n')

# B. Gerar e escrever os números pares do intervalo [20,50]
print('Números pares de 20 a 50: ')
for num in range(20,51,2):
    print(num,end='')
print('\n')

# C. Gerar e escrever os números inteiros do intervalo [25,70] em ordem decrescente
print('Números de 25 a 70 em ordem decrescente: ')
for num in range(70,24,-1):
    print(num,end='')
print('\n')

# D. Gerar e escrever os números ímpares do intervalo [25,95] em ordem decrescente
print('Números ímpares de 25 a 95 em ordem decrescente: ')
for num in range(95,24,-1):
    if num % 2 != 0:
       print(num,end='')
print('\n')

# E. Ler 15 números e escrever a soma e a média dos números lidos
numeros = []
for _ in range(10):
    numero = float(input('Digite um número: '))
    numeros.append(numero)

soma = sum(numeros)
media = soma / len(numeros)
print('Soma dos números: ',soma)
print('Média dos números: ',media,'\n')

# F. Ler 10 números inteiros e escrever a quantidade de números pares e a quantidade de números ímpares lidos
pares = 0
impares = 0
for _ in range(10):
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print('Quantidade de números pares: ',pares)
print('Quantidade de números ímpares: ',impares,'\n')

# G. Sortear 20 números inteiros entre -10 e 10 e imprimi-los acompanhados da mensagem “POSITIVO”, “NEGATIVO”, ou “NULO”, conforme o caso. No final, imprimir a quantidade de números positivos e negativos lidos
positivos = 0
negativos = 0
print('Números sorteados com classificação: ')
for _ in range(20):
    numero = random.randint(-10,10)
    if numero > 0:
        print(numero,'-POSITIVO')
        positivos += 1
    elif numero < 0:
        print(numero,'-NEGATIVO')
        negativos += 1
    else:
        print(numero,'-NULO')

print('Qunatidade de números positivos: ',positivos)
print('Quantidade de números negativos: ',negativos,'\n')

# H. Ler n números e imprimir no final a soma dos números lidos (obs.: n é a quantidade de números que deverão ser lidos e também deve ser lido do teclado)
n = int(input(' Quantos números você deseja ler? '))
soma_total = 0
for _ in range(n):
    numero = float(input('Digite um número: '))
    soma_total += numero

print('Soma dos',n,'números lidos: ',soma_total)