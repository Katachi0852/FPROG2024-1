# Exercicio 1
numero1 = int (input('Digite um número: '))
numero2 = int (input('Digite mais um número: '))

divisao= numero1 / numero2

if numero1 == 0 or numero2 == 0:
    print('Digite um número diferente de 0')

else:
    print('\nO resultado da divisão entre esses dois números é igual a',divisao)

# Exercicio 2

def verifica_soma(A,B,C):
    if A + B < A + C:
        print('A soma de A+B é menor que A+C')
    else:
        print('A soma de A+B não é menor que A+C')

A = float(input('Digite o valor de A: '))
B = float(input('Digite o valor de B: '))
C = float(input('Digite o valor de C: '))

verifica_soma(A,B,C)

# Exercicio 3

def dobrar_ou_triplicar(numero):
    if numero > 0:
        resultado = numero * 2
        print('O dobro do número', numero, 'é: ', resultado)
    elif numero < 0:
        resultado = numero * 3
        print('O triplo do número', numero, 'é: ', resultado)
    else:
        print('O número é zero.')

numero = float(input('Digite um número: '))

dobrar_ou_triplicar(numero)

# Exercicio 4

def verifica_divisibilidade_por_3(numero):
    if numero % 3 == 0:
        print(numero,'é divisível por 3.')
    else:
        print(numero,'não é divisível por 3.')

numero = int(input('Digite um número inteiro: '))

verifica_divisibilidade_por_3(numero)

# Exercicio 5

def verifica_par_ou_impar(numero):
    if numero % 2 == 0:
        print(numero,'é um número par.')
    else:
        print(numero,'é um número ímpar.')

numero = int(input('Digite um número: '))

verifica_par_ou_impar(numero)

# Exercicio 6

import random

escolha_usuario = input('Você aposta em Par ou Ímpar? [P/I]: ').strip().upper()

while escolha_usuario not in ['P','I']:
    escolha_usuario = input('Escolha inválida. por favor, digite P para Par ou I para Ímpar: ').strip().upper()

numero_usuario = int(input('Digite um número de 0 a 5: '))

while numero_usuario < 0 or numero_usuario > 5:
    numero_usuario = int(input('Número inválido. Por favor, digite um número de 0 a 5: '))

numero_programa = random.randint(0,5)

soma = numero_usuario + numero_programa
print('Você jogou ',numero_usuario,'e o programa jogou',numero_programa,'Total de',soma,'que é: ', 'par' if soma % 2 == 0 else 'ímpar')

if (soma % 2 == 0 and escolha_usuario == 'P') or (soma % 2 != 0 and escolha_usuario == 'I'):
    print('Você venceu!')
else:
    print('O programa venceu!')

# Exercicio 7

def calcular_desconto_previdenciario(salario):
    desconto = salario * 0.11
    desconto_maximo = 318.20
    if desconto > desconto_maximo:
        return desconto_maximo
    else:
        return desconto

# Solicitar o salário do usuário
salario = float(input('Digite o salário do funcionário: R$:'))

# Calcular o desconto previdenciário
desconto = calcular_desconto_previdenciario(salario)

# Exibir o valor do desconto
print('O desconto previdenciário é de: R$:',desconto,)

# Exercicio 8

def calcular_valor_venda(valor_compra):
    if valor_compra < 20:
        valor_venda = valor_compra * 1.45
    elif valor_compra <= 50:
        valor_venda = valor_compra * 1.35
    else:
        valor_venda = valor_compra * 1.25
    
    return valor_venda

# Entrada do valor do produto
valor_compra = float(input('Digite o valor de compra do produto: R$:'))

# Cálculo do valor de venda
valor_venda = calcular_valor_venda(valor_compra)

# Exibindo o valor de venda
print('O valor de venda do produto deve ser: R$',valor_venda)

# Exercicio 9

# Solicitação das cotações
cotacao_dolar = float(input('Informe a cotação do Dólar: '))
cotacao_euro = float(input('Informe a cotação do Euro: '))

# Menu de opções
print('\nEscolha uma opção de converção:')
print('1) Converter de Real para Euro')
print('2) Converter de Real para Dólar')
print('3) Converter de Euro para Dólar')
print('4) Converter de Euro para Real')
print('5) Converter de Dólar para Euro')
print('6) Converter de Dólar para Real')

opcao = int(input('Opção: '))
valor = float(input('Informe o valor a ser convertido: '))

# Processamento e impressão do resultado
if opcao == 1:
    resultado = valor / cotacao_euro
    print('Valor convertido em euro: ',resultado)
elif opcao == 2:
    resultado = valor / cotacao_dolar
    print('Valor convertido em Dólar: ',resultado)
elif opcao == 3:
    resultado = (valor * cotacao_euro) / cotacao_dolar
    print('Valor convertido em Dólar: ',resultado)
elif opcao == 4:
    resultado = valor * cotacao_euro
    print('Valor convertido em Real: ',resultado)
elif opcao == 5:
    resultado = (valor * cotacao_dolar) / cotacao_euro
    print('Valor convertido em Euro: ',resultado)
elif opcao == 6:
    resultado = valor * cotacao_dolar
    print('Valor convertido em Real: ',resultado)
else:
    print('Opção inválida.')

# Exercicio 10

import random

# Solicita ao usuário o número de faces do dado
faces = int(input('Informe o número de faces do dado (4,6,8,10,12, ou 16): '))

# Verifica se o número de faces é valido
if faces in [4,6,8,10,12,16]:
    # Realiza o sorteio
    resultado = random.randint(1,faces)
    print('Resultado do sorteio:',resultado)
else:
    print('Número de faces inválido.')

# Exercicio 11

# Solicita ao usuário o valor
valor = int(input('Informe o valor em R$: '))

# Notas disponíveis
notas = [100,50,20,10,5,1]

# Calcula a quantidade de cada nota
for nota in notas:
    quantidade_notas = valor // nota
    valor -= quantidade_notas * nota
    if quantidade_notas > 0:
        print(str(quantidade_notas)+'nota(s) de R$'+ str(nota)+'.')

# Exercicio 12

# Recebe a idade do nadador
idade = int(input('Informe a idade do nadador: '))

# Verifica a categoria correspondente
if 5 <= idade <= 7:
    categoria = 'Infantil A'
elif 8 <= idade <= 10:
    categoria = 'Infantil B'
elif 11 <= idade <= 13:
    categoria = 'Juvenil A'
elif 14 <= idade <= 17:
    categoria = 'Juvenil B'
elif idade >= 18:
    categoria = 'Sênior'
else:
    categoria = 'Idade fora das categorias de competição'

# Imprime a categoria
print('Categoria',categoria)

# Exercicio 13

nota_a = float(input('Nota do Grau A: '))
nota_b = float(input('Nota do Grau B: '))
media = (nota_a + nota_b) / 2

print('Média: ',media)

if media >= 7:
    print('Passou por média.')
else:
    print('Recuperaçao.')
    escolha = input('Substituir nota A ou B? (a/b): ')
    nota_c = float(input('Nota do Grau C: '))

    if escolha == 'a':
        media = (nota_c + nota_b) / 2
    elif escolha == 'b':
        media = (nota_a + nota_c) / 2
    
    print('Nova média: ',media)
    if media >= 6:
        print('Aprovado.')
    else:
        print('Reprovado.')

# Exercicio 14

# Valor base do plano de saúde
valor_base = 300

# Entrada para o número de dependentes
numero_dependentes = int(input('Quantidade dependentes?'))

# Inicialização do valor adicional
adicional_dependentes = 0

#Loop para calcular o adicional por dependente
for _ in range(numero_dependentes):
    idade = int(input('Idade do dependente: '))
    if idade < 10:
        adicional_dependentes += 100
    elif idade <= 30:
        adicional_dependentes += 220
    elif idade <= 60:
        adicional_dependentes += 395
    else:
        adicional_dependentes += 480

# Cálculo do valor total a ser pago
valor_total = valor_base + adicional_dependentes

# Exibição do resultado
print('Valor total a ser pago: R$',valor_total)

# Exercicio 15

# Entrada do preço do produto
preco_produto = float(input("Preço do produto: R$ "))

# Entrada da condição de pagamento
print("Condições de pagamento:")
print("1 - À vista em dinheiro, recebe 15% de desconto")
print("2 - À vista no cartão de crédito, recebe 10% de desconto")
print("3 - Em duas vezes, preço normal de etiqueta sem juros")
print("4 - Em três vezes, preço normal de etiqueta mais juros de 10%")
condicao_pagamento = int(input("Escolha a condição de pagamento (1, 2, 3 ou 4): "))

# Cálculo do valor a ser pago com base na condição de pagamento
if condicao_pagamento == 1:
    valor_final = preco_produto * 0.85 # Desconto de 15%
elif condicao_pagamento == 2:
    valor_final = preco_produto * 0.90 # Desconto de 10%
elif condicao_pagamento == 3:
    valor_final = preco_produto # Preço normal em duas vezes
elif condicao_pagamento == 4:
    valor_final = preco_produto * 1.10 # Preço com juros de 10%
else:
    print("Opção de pagamento inválida. Por favor, escolha uma opção válida.")
    exit() # Encerra o programa se a opção for inválida

# Exibição do resultado formatado com duas casas decimais
print("Valor a ser pago: R$", round(valor_final, 2))
