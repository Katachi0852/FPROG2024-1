# Função para calcular a média considerando o sistema de notas da Unisinos
def calcular_media_unisinos(a, b):
    return (a + b) / 2

# Número de alunos
num_alunos = int(input("Digite o número de alunos: "))

# Variável para armazenar a média geral
media_geral = 0

# Loop para cada aluno
for aluno in range(num_alunos):
    print(f"\nAluno {aluno + 1}:")
    
    # Ler as notas do grau A e B
    nota_a = float(input("Digite a nota do grau A: "))
    nota_b = float(input("Digite a nota do grau B: "))
    
    # Calcular a média
    media = calcular_media_unisinos(nota_a, nota_b)
    
    # Verificar se o aluno está aprovado
    if media >= 6.0:
        print("APROVADO")
    else:
        # Ler a nota do grau C e qual nota (A ou B) deve ser substituída
        nota_c = float(input("Digite a nota do grau C: "))
        nota_substituir = input("Qual nota deve ser substituída (A ou B)? ").upper()
        
        # Substituir a nota A ou B e recalcular a média
        if nota_substituir == 'A':
            nova_media = calcular_media_unisinos(nota_c, nota_b)
        elif nota_substituir == 'B':
            nova_media = calcular_media_unisinos(nota_a, nota_c)
        
        # Verificar se o aluno está aprovado após a substituição
        if nova_media >= 6.0:
            print("APROVADO")
        else:
            print("REPROVADO")
    
    # Adicionar a média do aluno à média geral
    media_geral += media

# Calcular e imprimir a média geral dos alunos
media_geral /= num_alunos
print("\nMédia geral dos alunos:", media_geral)
