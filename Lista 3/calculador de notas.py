# Solicita ao usuário o valor
valor = int(input('Informe o valor em R$: '))

# Notas disponíveis
notas = [100,50,20,10,5,2]

# Calcula a quantidade de cada nota
for nota in notas:
    quantidade_notas = valor // nota
    valor -= quantidade_notas * nota
    if quantidade_notas > 0:
        print(str(quantidade_notas)+'nota(s) de R$'+ str(nota)+'.')