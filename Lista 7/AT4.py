import random

# Função para gerar uma matriz 4x6 com valores aleatórios entre -10 e 10
def gerar_matriz():
    matriz = []
    for _ in range(4):
        linha = [random.randint(-10, 10) for _ in range(6)]
        matriz.append(linha)
    return matriz

# Função para calcular as somas especificadas
def calcular_somas(matriz):
    # a. Soma dos elementos da segunda linha
    soma_segunda_linha = sum(matriz[1])

    # b. Soma dos elementos da quinta coluna
    soma_quinta_coluna = sum(matriz[i][4] for i in range(4))

    # c. Soma da multiplicação dos elementos da primeira linha pelos elementos da quarta linha
    soma_multiplicacao_linhas = sum(matriz[0][j] * matriz[3][j] for j in range(6))

    # d. Soma dos elementos só das colunas com índices pares
    soma_colunas_pares = sum(matriz[i][j] for i in range(4) for j in range(6) if j % 2 == 0)

    # e. Soma dos elementos só das linhas com índices ímpares
    soma_linhas_impares = sum(sum(matriz[i]) for i in range(1, 4, 2))

    # Retornar as somas calculadas
    return soma_segunda_linha, soma_quinta_coluna, soma_multiplicacao_linhas, soma_colunas_pares, soma_linhas_impares

# Gerar matriz aleatória
matriz = gerar_matriz()

# Imprimir matriz
print("Matriz 4x6:")
for linha in matriz:
    print(linha)

# Calcular e imprimir as somas
soma_segunda_linha, soma_quinta_coluna, soma_multiplicacao_linhas, soma_colunas_pares, soma_linhas_impares = calcular_somas(matriz)

print("\nSomas:")
print(f"a. Soma da segunda linha: {soma_segunda_linha}")
print(f"b. Soma da quinta coluna: {soma_quinta_coluna}")
print(f"c. Soma da multiplicação dos elementos da primeira linha pelos elementos da quarta linha: {soma_multiplicacao_linhas}")
print(f"d. Soma dos elementos só das colunas com índices pares: {soma_colunas_pares}")
print(f"e. Soma dos elementos só das linhas com índices ímpares: {soma_linhas_impares}")
