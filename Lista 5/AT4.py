import random

def sorteio(inicio, fim):
    """Função para sortear um número dentro de um intervalo fechado [inicio, fim]"""
    return random.randint(inicio, fim)

# Exemplo de uso da função sorteio
inicio_intervalo = int(input("Digite o valor inicial do intervalo: "))
fim_intervalo = int(input("Digite o valor final do intervalo: "))

numero_sorteado = sorteio(inicio_intervalo, fim_intervalo)
print("Número sorteado:", numero_sorteado)
