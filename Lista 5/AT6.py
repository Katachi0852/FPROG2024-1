import random

# Variáveis para armazenar o número de itens de cada tipo coletados
itens_comuns = 0
itens_raros = 0
itens_lendarios = 0

def abrir_caixa():
    """Função para simular a abertura de uma caixa e coletar um item"""
    global itens_comuns, itens_raros, itens_lendarios
    item = random.choices(['comum', 'raro', 'lendario'], weights=[80, 19, 1], k=1)[0]
    if item == 'comum':
        itens_comuns += 1
    elif item == 'raro':
        itens_raros += 1
    elif item == 'lendario':
        itens_lendarios += 1
    print(f"Você coletou 1 item {item}!")

def consultar_itens():
    """Função para consultar os itens coletados pelo jogador"""
    print(f"Itens comuns: {itens_comuns}")
    print(f"Itens raros: {itens_raros}")
    print(f"Itens lendários: {itens_lendarios}")

# Programa principal
while True:
    print("\n1 – Abrir uma caixa")
    print("2 – Consultar itens")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '0':
        print("Programa encerrado.")
        break
    elif opcao == '1':
        abrir_caixa()
    elif opcao == '2':
        consultar_itens()
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")
