# Solicita ao usuário o valor do divisor
divisor = int(input("Entre com o valor do divisor: "))

# Solicita ao usuário o valor inicial do intervalo
inicio_intervalo = int(input("Início do intervalo: "))

# Solicita ao usuário o valor final do intervalo
final_intervalo = int(input("Final do intervalo: "))

# Mostra a mensagem inicial
print("Números divisíveis por", divisor, "no intervalo de", inicio_intervalo, "a", final_intervalo, ":")

# Loop pelos números no intervalo especificado
for numero in range(inicio_intervalo, final_intervalo + 1):
    # Verifica se o número é divisível pelo divisor
    if numero % divisor == 0:
        print(numero, end=" ")
