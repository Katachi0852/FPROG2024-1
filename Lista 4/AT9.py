# Solicitar ao usuário que insira o número de linhas
n = int(input("Entre com um número: "))

# Solicitar ao usuário que insira o caractere desejado
caracter = input("Entre com um caractere: ")

# Loop para imprimir as linhas com base no número fornecido
for i in range(1, n + 1):
    print(caracter * i)
