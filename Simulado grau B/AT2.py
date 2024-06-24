import random

# Função para criar um tabuleiro vazio
def cria_tabuleiro_vazio():
    tabuleiro = [['~' for _ in range(8)] for _ in range(8)]
    return tabuleiro

# Função para imprimir o tabuleiro
def imprime_tabuleiro(tabuleiro):
    print("\nTabuleiro:")
    print("  1 2 3 4 5 6 7 8")
    letras = 'ABCDEFGH'
    for i in range(8):
        print(letras[i], ' '.join(tabuleiro[i]))

# Função para inicializar a matriz de controle com os navios
def inicializa_matriz_controle():
    matriz_controle = [['~' for _ in range(8)] for _ in range(8)]
    
    # Posicionamento dos navios aleatório (exemplo)
    posicoes_navios = [
        ('A', 0), ('B', 2), ('C', 4), ('D', 6), ('E', 1)
    ]
    
    for letra, coluna in posicoes_navios:
        matriz_controle[ord(letra) - ord('A')][coluna] = 'N'  # 'N' representa um navio
    
    return matriz_controle

# Função para verificar se o jogador acertou todos os navios
def todos_navios_afundados(tabuleiro):
    for linha in tabuleiro:
        if 'N' in linha:
            return False
    return True

# Função principal do jogo
def batalha_naval():
    # Inicializações
    jogadas = 0
    matriz_controle = inicializa_matriz_controle()
    tabuleiro_exibicao = cria_tabuleiro_vazio()
    
    # Loop principal do jogo
    while not todos_navios_afundados(matriz_controle):
        # Mostra o tabuleiro para o jogador
        imprime_tabuleiro(tabuleiro_exibicao)
        
        # Recebe a jogada do jogador
        jogada = input("\nInforme a posição (por exemplo, 'A 5'): ").strip().upper()
        
        # Validação da jogada
        if len(jogada) != 3 or jogada[0] < 'A' or jogada[0] > 'H' or jogada[2] < '1' or jogada[2] > '8' or jogada[1] != ' ':
            print("Jogada inválida. Tente novamente.")
            continue
        
        linha = ord(jogada[0]) - ord('A')
        coluna = int(jogada[2]) - 1
        
        # Verifica se a posição possui um navio
        if matriz_controle[linha][coluna] == 'N':
            print("BOOOM! Você acertou um navio!")
            tabuleiro_exibicao[linha][coluna] = 'X'  # 'X' representa um acerto
        else:
            print("SPLASH! Você errou.")
        
        # Contabiliza a jogada
        jogadas += 1
    
    # Fim do jogo - todos os navios foram afundados
    print("\nParabéns! Você afundou todos os navios!")
    print(f"Número de jogadas: {jogadas}")

# Execução do jogo
batalha_naval()
