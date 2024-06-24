import random

# Função para gerar uma matriz 10x3 com notas aleatórias entre 0.0 e 10.0
def gerar_matriz_notas():
    matriz = []
    for _ in range(10):
        grau_a = random.uniform(0.0, 10.0)  # Gerar nota do Grau A
        grau_b = random.uniform(0.0, 10.0)  # Gerar nota do Grau B
        media_parcial = (grau_a + grau_b) / 2  # Calcular média parcial
        matriz.append([grau_a, grau_b, media_parcial])
    return matriz

# Gerar matriz 10x3 com notas aleatórias e calcular médias parciais
matriz_notas = gerar_matriz_notas()

# Imprimir matriz com as notas e médias parciais formatadas
print("Matriz com informações das notas de 10 alunos:")
print("Grau A | Grau B | Grau Parcial")
for linha in matriz_notas:
    print(f"{linha[0]:.1f}    | {linha[1]:.1f}    | {linha[2]:.1f}")
