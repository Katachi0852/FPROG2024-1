def mediaUnisinos(notaA, notaB):
    """Função para calcular a média final no sistema de notas da Unisinos"""
    return (notaA + notaB) / 2

# Exemplo de uso da função mediaUnisinos
nota_A = float(input("Digite a nota do Grau A: "))
nota_B = float(input("Digite a nota do Grau B: "))

resultado_final = mediaUnisinos(nota_A, nota_B)
print("Resultado do Grau Final:", resultado_final)
