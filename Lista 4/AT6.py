import random

# Lista para armazenar os valores sorteados
valores_sorteados = []

# Sortear 5 valores entre 0 e 100
for _ in range(5):
    valor = random.randint(0, 100)
    valores_sorteados.append(valor)

# Imprimir os valores sorteados
print("Valores sorteados:", valores_sorteados)

# Encontrar o menor valor
menor_valor = min(valores_sorteados)
print("Menor valor sorteado:", menor_valor)

# Encontrar o maior valor
maior_valor = max(valores_sorteados)
print("Maior valor sorteado:", maior_valor)

# Calcular a média dos valores
media_valores = sum(valores_sorteados) / len(valores_sorteados)
print("Média dos valores sorteados:", media_valores)
