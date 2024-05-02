def tabuada(numero):
    """Função para imprimir a tabuada de um número"""
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Exemplo de uso da função tabuada
num = int(input("Digite um número inteiro para calcular a tabuada: "))
tabuada(num)
