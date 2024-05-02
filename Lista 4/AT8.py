def calcular_fatorial(numero):
    """Função para calcular o fatorial de um número"""
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

while True:
    # Solicitar ao usuário que insira um número
    numero = int(input("Entre com um número: "))

    # Calcular o fatorial do número fornecido
    resultado = calcular_fatorial(numero)

    # Imprimir o resultado
    print(f"O fatorial de {numero} é {resultado}")

    # Perguntar ao usuário se deseja calcular outro número
    continuar = input("Calcular outro número (s/n)? ").lower()
    if continuar != 's':
        break
