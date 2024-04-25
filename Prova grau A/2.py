def divisao (dividendo,divisor):
    if divisor != 0:
        valor = dividendo % divisor
        if valor == 0:
            print('O número ',dividendo,'é divisivel por ',divisor)
            return True
        else:
            print('O número ',dividendo,'não é divisivel por ',divisor)
            return False



dividendo = int(input('Digite um número que será dividido: '))
divisor = int(input('Digite um número que será dividido: '))

divisao (dividendo,divisor)