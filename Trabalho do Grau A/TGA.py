import random

# Variáveis de jogadores
pos_jogador1 = 0
pos_jogador2 = 0
filhos_jogador1 = 0
filhos_jogador2 = 0
dinheiro_jogador1 = 0
dinheiro_jogador2 = 0
casado_jogador1 = False
casado_jogador2 = False
famoso_jogador1 = False
famoso_jogador2 = False
vivo_jogador1 = True
vivo_jogador2 = True

# Definição do tabuleiro
tabuleiro = [
    "Iniciou a Jornada", "Casou", "Teve 1 filho", "Perdeu o emprego", 
    "Cursou a faculdade", "Ganhou na loteria", "Comprou uma casa", 
    "Ficou famoso", "Foi para a prisão", "Se divorciou", "Perdeu na bolsa de valores",
    "Adotou uma criança", "Viajou o mundo", "Perdeu a casa", "Venceu uma competição",
    "Ficou doente", "Perdeu o negócio", "Enriqueceu", "Teve gêmeos", 
    "Voltou a estudar", "Teve uma vida longa e próspera!"
]

# Função para realizar uma rodada de jogo para um jogador
def rodada_jogo(jogador):
    global pos_jogador1, pos_jogador2, filhos_jogador1, filhos_jogador2, dinheiro_jogador1, dinheiro_jogador2
    global casado_jogador1, casado_jogador2, famoso_jogador1, famoso_jogador2, vivo_jogador1, vivo_jogador2
    
    # Simular a roleta (gerar um número aleatório de 1 a 6)
    resultado_roleta = random.randint(1, 6)
    
    # Atualizar posição do jogador
    if jogador == 1:
        pos_jogador1 += resultado_roleta
    else:
        pos_jogador2 += resultado_roleta
    
    # Verificar ação da casa
    casa_atual = tabuleiro[pos_jogador1] if jogador == 1 else tabuleiro[pos_jogador2]
    if casa_atual == "Casou":
        if jogador == 1:
            casado_jogador1 = True
        else:
            casado_jogador2 = True
    elif casa_atual == "Teve 1 filho":
        if jogador == 1:
            filhos_jogador1 += 1
        else:
            filhos_jogador2 += 1
    # Implemente as outras ações do tabuleiro
    
    # Feedback para o jogador
    print("Jogador", jogador)
    print("Resultado da roleta:", resultado_roleta)
    print("Posição atual:", pos_jogador1 if jogador == 1 else pos_jogador2)
    print("Ação da casa:", casa_atual)
    # Adicione mais feedbacks conforme necessário

# Função principal do jogo
def jogo_da_vida():
    while pos_jogador1 < 21 and pos_jogador2 < 21:
        rodada_jogo(1)
        if pos_jogador1 < 21:
            rodada_jogo(2)
    if pos_jogador1 >= 21:
        print("Jogador 1 venceu!")
    else:
        print("Jogador 2 venceu!")

# Executar o jogo
jogo_da_vida()
