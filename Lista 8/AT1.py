# Receber a frase do usuário
frase = input("Digite uma frase: ")

# Contar a quantidade total de letras
# Remover espaços em branco para contar apenas letras
frase_sem_espacos = frase.replace(" ", "")
quantidade_letras = len(frase_sem_espacos)

# Contar a quantidade total de palavras
palavras = frase.split()  # Dividir a frase em palavras
quantidade_palavras = len(palavras)

# Exibir os resultados na tela
print(f"A frase '{frase}' tem:")
print(f" - {quantidade_letras} letras")
print(f" - {quantidade_palavras} palavras")
