import random

# Função para simular o lançamento do dado viciado
def lancar_dado_viciado(n_lancamentos):
    # Inicializa o array para contar o número de ocorrências de cada face
    ocorrencias = [0] * 6
    
    # Define as probabilidades de cada face do dado viciado (soma das probabilidades deve ser 1)
    probabilidades = [0.1, 0.2, 0.2, 0.2, 0.2, 0.1]  # Exemplo de probabilidades, ajuste conforme necessário
    
    # Realiza os lançamentos
    for _ in range(n_lancamentos):
        resultado = random.choices(range(1, 7), weights=probabilidades)[0]
        ocorrencias[resultado - 1] += 1
    
    # Calcula e imprime o percentual de cada face
    total_lancamentos = sum(ocorrencias)
    print("Resultado dos lançamentos:")
    for i, ocorrencia in enumerate(ocorrencias):
        percentual = (ocorrencia / total_lancamentos) * 100
        print(f"Face {i + 1}: {percentual:.2f}%")

# Lendo o número de lançamentos do usuário
n_lancamentos = int(input("Digite o número de lançamentos do dado: "))

# Chamando a função para simular os lançamentos
lancar_dado_viciado(n_lancamentos)
