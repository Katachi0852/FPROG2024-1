def calcular_tabuada(numero):
    print('Tabuada de multiplicação do',numero,': ')
    for i in range(1,11):
        resultado = numero * i
        print(numero,'x',i,'=',resultado)

def main():
    calcular_outro = 's'
    while calcular_outro.lower() == 's':
        try:
            numero = int(input('Entre com um número de 1 a 9: '))
            if 1 <= numero <= 9:
                calcular_tabuada(numero)
            else:
                print('Número fora do intervalo válido (1 a 9).')
        except ValueError:
            print('Entrada inválida. Digite um número válido.')
        
        calcular_outro = input('Calcular outro número (s/n)? ')
    
    print('Programa encerrado.')

if __name__ == '__main__':
    main()