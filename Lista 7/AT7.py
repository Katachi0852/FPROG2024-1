import random

# Função para gerar uma matriz 5x5 com números inteiros aleatórios entre -10 e 10
def gerar_matriz():
    matriz = []
    for _ in range(5):
        linha = [random.randint(-10, 10) for _ in range(5)]
        matriz.append(linha)
    return matriz

# Função para transformar os números negativos em positivos e vice-versa na matriz
def transformar_matriz(matriz):
    for i in range(5):
        for j in range(5):
            if matriz[i][j] < 0:
                matriz[i][j] = abs(matriz[i][j])  # Transforma negativo em positivo
            else:
                matriz[i][j] = -matriz[i][j]  # Transforma positivo em negativo (incluindo zero)

# Função para imprimir a matriz
def imprimir_matriz(matriz, mensagem):
    print(mensagem)
    for linha in matriz:
        print(linha)
    print()

# Gerar matriz 5x5 com números inteiros aleatórios
matriz_original = gerar_matriz()

# Imprimir matriz original
imprimir_matriz(matriz_original, "Matriz Original:")

# Transformar a matriz (negativos em positivos e vice-versa)
transformar_matriz(matriz_original)

# Imprimir matriz modificada
imprimir_matriz(matriz_original, "Matriz Modificada (números negativos transformados em positivos e vice-versa):")
