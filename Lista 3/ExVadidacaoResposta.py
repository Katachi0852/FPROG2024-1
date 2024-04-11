#
while resposta != 'S' and resposta != 'N':
    resposta = input('Resposta Sim (S) ou Não (N): ')
    
    if resposta == 'S':
        print('Como você respondeu sim ...')
    elif resposta == 'N':
        print('Como você respondeu não ...')
    else:
        print('Resposta inválida')

#ExContadorWhile

nome = input('Digite seu nome: ')

cont = 0

while cont < 10:
    print(nome)
    cont = cont + 1