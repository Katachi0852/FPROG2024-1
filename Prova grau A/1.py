def verifica_divisibilidade_po_2(numero):
    if numero % 2 == 0:
        print(numero,'é divisivel por 2.')
    else:
        print(numero,'não é divisivel por 2.')

numero = int(input('Digite um número inteiro: '))

verifica_divisibilidade_po_2(numero)