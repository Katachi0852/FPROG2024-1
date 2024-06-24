def eh_palindromo(palavra):
    # Normalizar a palavra para minúsculas
    palavra = palavra.lower()
    
    # Inverter a palavra
    palavra_invertida = palavra[::-1]
    
    # Verificar se a palavra original é igual à palavra invertida
    if palavra == palavra_invertida:
        return True
    else:
        return False

# Exemplos de uso:
palavra1 = "Ana"
palavra2 = "osso"
palavra3 = "arara"
palavra4 = "python"

print(f"A palavra '{palavra1}' é um palíndromo? {eh_palindromo(palavra1)}")
print(f"A palavra '{palavra2}' é um palíndromo? {eh_palindromo(palavra2)}")
print(f"A palavra '{palavra3}' é um palíndromo? {eh_palindromo(palavra3)}")
print(f"A palavra '{palavra4}' é um palíndromo? {eh_palindromo(palavra4)}")
