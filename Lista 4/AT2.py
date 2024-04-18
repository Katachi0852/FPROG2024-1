import random

# Sorteia um número de 1 a 10
numero_sorteado = random.randint(1,10)
tentativas = 3

for tentativa in range(tentativas):
    palpite = int(input('Adivinhe o número entre 1 e 10: '))
    if palpite == numero_sorteado:
        print('Parabéns! Você acertou o número!')
        break
    elif palpite < numero_sorteado:
        print('O número sorteado é maior do que o seu palpite.')
    else:
        print('O número sorteado é menor do que o seu palpite.')
    
    # Informa o número de tentativas restantes, exceto na última tentativa
    if tentativa < tentativas -1:
        print('Você não acertou o número. O número era: ',numero_sorteado)