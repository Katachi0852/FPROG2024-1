def matriz_identidade(n):
    # Criar uma matriz vazia com zeros
    matriz = [[0] * n for _ in range(n)]
    
    # Preencher a diagonal principal com uns
    for i in range(n):
        matriz[i][i] = 1
    
    return matriz

# Gerar matriz identidade 4x4
matriz_4x4 = matriz_identidade(4)

# Imprimir a matriz identidade 4x4
for linha in matriz_4x4:
    print(linha)
