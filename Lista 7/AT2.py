# Definindo a matriz M
M = [
    [1, 5, 9, 2, 5],
    [7, 4, 13, 21, 6],
    [8, -3, 5, 7, 12]
]

# Multiplicando todos os elementos por 7
for i in range(len(M)):
    for j in range(len(M[i])):
        M[i][j] *= 7

# Imprimindo a matriz multiplicada
for linha in M:
    for elemento in linha:
        print(elemento, end=' ')
    print()  # Para pular para a próxima linha
