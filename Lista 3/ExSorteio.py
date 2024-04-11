import random

numeroSorteado = random.randint(1,20)

numeroLido = int(input('Digite um número de 1 a 20: '))

if numeroLido == numeroSorteado:
    print('Certo')
else:
    print('ERROOOUUU! O numero sorteado era ',numeroSorteado)