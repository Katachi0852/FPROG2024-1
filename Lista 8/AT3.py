def cebolinha(frase):
    frase_modificada = frase.replace('r', 'l')
    return frase_modificada

# Exemplo de uso:
frase_original = input("Digite uma frase: ")
frase_modificada = cebolinha(frase_original)

print("Frase modificada:", frase_modificada)

