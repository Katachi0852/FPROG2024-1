def somar(num1, num2):
    """Função para somar dois números"""
    return num1 + num2

def subtrair(num1, num2):
    """Função para subtrair dois números"""
    return num1 - num2

def multiplicar(num1, num2):
    """Função para multiplicar dois números"""
    return num1 * num2

def dividir(num1, num2):
    """Função para dividir dois números"""
    if num2 != 0:
        return num1 / num2
    else:
        return "Erro: Divisão por zero!"

def exibir_menu():
    """Função para exibir o menu de opções"""
    print("Escolha a operação:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

# Programa principal
while True:
    exibir_menu()
    opcao = input("Digite o número da operação desejada: ")

    if opcao == '5':
        print("Programa encerrado.")
        break
    elif opcao in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == '1':
            print("Resultado da soma:", somar(num1, num2))
        elif opcao == '2':
            print("Resultado da subtração:", subtrair(num1, num2))
        elif opcao == '3':
            print("Resultado da multiplicação:", multiplicar(num1, num2))
        elif opcao == '4':
            print("Resultado da divisão:", dividir(num1, num2))
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")
