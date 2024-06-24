# Definindo os vetores dados
v1 = [1, 5, 9, 2, 5]
v2 = [7, 4, 13, 21, 6]
v3 = [8, -3, 5, 7, 12]

# Criando a matriz M
M = [v1, v2, v3]

# Imprimindo a matriz M
for linha in M:
    for elemento in linha:
        print(elemento, end=' ')
    print()  # Para pular para a próxima linha

