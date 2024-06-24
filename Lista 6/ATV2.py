# Função para ler os valores e imprimir o resultado da multiplicação
def multiplicar_por_posicao(valores):
    for i, valor in enumerate(valores):
        resultado = i * valor
        print(f"{valor} multiplicado pela posição {i} resulta em: {resultado}")

# Lendo os valores para dentro do vetor
valores = []
for i in range(5):
    valor = int(input(f"Digite o {i+1}º valor: "))
    valores.append(valor)

# Chamando a função para imprimir o resultado
multiplicar_por_posicao(valores)
