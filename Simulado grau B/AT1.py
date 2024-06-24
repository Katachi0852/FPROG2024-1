def correcao_prova(gabarito, respostas_estudante):
    # Inicializar variáveis para contagem de acertos e armazenamento de resultados
    num_acertos = 0
    resultado = []

    # Comparar cada questão
    for i in range(len(gabarito)):
        if gabarito[i] == respostas_estudante[i]:
            num_acertos += 1
            resultado.append(f"Questão {i+1}: resposta correta")
        else:
            resultado.append(f"Questão {i+1}: resposta incorreta. A resposta correta é {gabarito[i]}.")

    # Calcular pontuação final
    pontuacao_final = num_acertos * 10 / len(gabarito)

    # Imprimir resultados
    print("\nRespostas do estudante:")
    for resposta in resultado:
        print(resposta)

    print(f"\nA pontuação do estudante é {num_acertos}/{len(gabarito)} ou {pontuacao_final:.1f}/10.")

# Exemplo de uso:
gabarito = ['a', 'f', 'c', 'd', 'd', 'a', 'e', 'e', 'b', 'a']
respostas_estudante = ['a', 'f', 'a', 'd', 'f', 'a', 'e', 'e', 'c', 'a']

correcao_prova(gabarito, respostas_estudante)
