def converter_maiusculas(frase):
    frase_maiusculas = frase.upper()
    return frase_maiusculas

# Exemplo de uso:
frase_original = input("Digite uma frase em minúsculas: ")
frase_convertida = converter_maiusculas(frase_original)

print("Frase original:", frase_original)
print("Frase convertida para maiúsculas:", frase_convertida)
