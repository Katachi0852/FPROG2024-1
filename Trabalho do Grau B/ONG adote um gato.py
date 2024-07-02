import csv

# Função para carregar os dados do arquivo CSV
def carregar_dados(arquivo_csv):
    felinos = []
    with open(arquivo_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            felinos.append(dict(row))
    return felinos

def menu_principal():
    print("\n=== MENU PRINCIPAL ===")
    print("1) Cadastrar felino")
    print("2) Alterar status de felino")
    print("3) Consultar informações sobre felino")
    print("4) Apresentar estatísticas gerais")
    print("5) Filtragem de dados")
    print("6) Salvar e sair")
    print("7) Sair do programa")
    opcao = input("Escolha uma opção: ")
    return opcao

import csv

# Função para carregar os dados do arquivo CSV
def carregar_dados(arquivo_csv):
    felinos = []
    try:
        with open(arquivo_csv, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                felinos.append(dict(row))
    except FileNotFoundError:
        print(f"Arquivo '{arquivo_csv}' não encontrado. Criando um novo arquivo.")
    return felinos

# Função para salvar os dados de volta ao arquivo CSV
def salvar_dados(arquivo_csv, felinos):
    chaves = felinos[0].keys() if felinos else []
    with open(arquivo_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=chaves)
        writer.writeheader()
        writer.writerows(felinos)
    print(f"Dados salvos em '{arquivo_csv}'.")

# Função para cadastrar um novo felino
def cadastrar_felino(felinos):
    novo_felino = {}
    print("\n=== CADASTRO DE FELINO ===")
    novo_felino['Nome'] = input("Nome: ")
    novo_felino['Sexo'] = input("Sexo (M/F): ").upper()
    novo_felino['Idade'] = input("Idade: ")
    novo_felino['Raça'] = input("Raça: ")
    novo_felino['Cor Predominante'] = input("Cor predominante: ")
    novo_felino['Castrado'] = input("Castrado (Sim/Não): ").capitalize()
    novo_felino['FIV+'] = input("FIV+ (Sim/Não): ").capitalize()
    novo_felino['FELV+'] = input("FELV+ (Sim/Não): ").capitalize()
    novo_felino['Data de Resgate'] = input("Data de Resgate (DD/MM/AAAA): ")
    novo_felino['Adotado'] = input("Adotado (Sim/Não): ").capitalize()
    novo_felino['Lar Temporário'] = input("Lar Temporário (Sim/Não): ").capitalize()
    novo_felino['Data de Adoção/Hospedagem'] = input("Data de Adoção/Hospedagem (DD/MM/AAAA): ")
    novo_felino['Tutor'] = input("Tutor: ")
    novo_felino['Contato'] = input("Contato do tutor: ")
    novo_felino['Data da Última Vacina'] = input("Data da Última Vacina (DD/MM/AAAA): ")
    novo_felino['Data da Última Desvermifugação'] = input("Data da Última Desvermifugação (DD/MM/AAAA): ")
    novo_felino['Data do Último Antipulgas'] = input("Data do Último Antipulgas (DD/MM/AAAA): ")
    novo_felino['Informações Extras'] = input("Informações Extras: ")

    felinos.append(novo_felino)
    print("Felino cadastrado com sucesso!")

# Função para alterar status de um felino
def alterar_status_felino(felinos):
    if not felinos:
        print("Nenhum felino cadastrado.")
        return
    
    print("\n=== ALTERAR STATUS DE FELINO ===")
    for idx, felino in enumerate(felinos):
        print(f"{idx + 1}) {felino['Nome']}")

    escolha = int(input("Escolha o felino pelo número: ")) - 1
    if escolha < 0 or escolha >= len(felinos):
        print("Escolha inválida.")
        return
    
    felino = felinos[escolha]
    print("\nInformações do felino selecionado:")
    for key, value in felino.items():
        print(f"{key}: {value}")
    
    opcao = input("Escolha qual informação deseja alterar ou pressione Enter para sair: ")
    while opcao:
        if opcao in felino:
            felino[opcao] = input(f"Novo valor para {opcao}: ")
        else:
            print("Opção inválida.")
        
        opcao = input("Escolha qual informação deseja alterar ou pressione Enter para sair: ")

    print("Alterações salvas!")

# Função para consultar informações de um felino
def consultar_informacoes_felino(felinos):
    if not felinos:
        print("Nenhum felino cadastrado.")
        return
    
    print("\n=== CONSULTAR INFORMAÇÕES DE FELINO ===")
    for idx, felino in enumerate(felinos):
        print(f"{idx + 1}) {felino['Nome']}")

    escolha = int(input("Escolha o felino pelo número: ")) - 1
    if escolha < 0 or escolha >= len(felinos):
        print("Escolha inválida.")
        return
    
    felino = felinos[escolha]
    print("\nInformações do felino:")
    for key, value in felino.items():
        print(f"{key}: {value}")

# Função para apresentar estatísticas gerais dos felinos
def apresentar_estatisticas_gerais(felinos):
    if not felinos:
        print("Nenhum felino cadastrado.")
        return
    
    total_felinos = len(felinos)
    machos = sum(1 for felino in felinos if felino['Sexo'] == 'M')
    femeas = total_felinos - machos
    
    adotados = sum(1 for felino in felinos if felino['Adotado'] == 'Sim')
    nao_adotados = total_felinos - adotados
    
    total_fiv = sum(1 for felino in felinos if felino['FIV+'] == 'Sim')
    total_felv = sum(1 for felino in felinos if felino['FELV+'] == 'Sim')
    apenas_fiv = sum(1 for felino in felinos if felino['FIV+'] == 'Sim' and felino['FELV+'] == 'Não')
    apenas_felv = sum(1 for felino in felinos if felino['FELV+'] == 'Sim' and felino['FIV+'] == 'Não')
    ambos = sum(1 for felino in felinos if felino['FIV+'] == 'Sim' and felino['FELV+'] == 'Sim')
    
    percent_machos = (machos / total_felinos) * 100 if total_felinos > 0 else 0
    percent_femeas = (femeas / total_felinos) * 100 if total_felinos > 0 else 0
    percent_adotados = (adotados / total_felinos) * 100 if total_felinos > 0 else 0
    percent_nao_adotados = (nao_adotados / total_felinos) * 100 if total_felinos > 0 else 0
    percent_apenas_fiv = (apenas_fiv / total_felinos) * 100 if total_felinos > 0 else 0
    percent_apenas_felv = (apenas_felv / total_felinos) * 100 if total_felinos > 0 else 0
    percent_ambos = (ambos / total_felinos) * 100 if total_felinos > 0 else 0
    
    print("\n=== ESTATÍSTICAS GERAIS ===")
    print(f"Porcentagem de machos: {percent_machos:.2f}%")
    print(f"Porcentagem de fêmeas: {percent_femeas:.2f}%")
    print(f"Porcentagem de adotados: {percent_adotados:.2f}%")
    print(f"Porcentagem de não adotados: {percent_nao_adotados:.2f}%")
    print(f"Porcentagem de felinos FIV+: {percent_apenas_fiv:.2f}%")
    print(f"Porcentagem de felinos FELV+: {percent_apenas_felv:.2f}%")
    print(f"Porcentagem de felinos FIV+ e FELV+: {percent_ambos:.2f}%")

# Função para realizar filtragem de dados
def realizar_filtragem(felinos):
    if not felinos:
        print("Nenhum felino cadastrado.")
        return
    
    print("\n=== FILTRAGEM DE DADOS ===")
    print("1) Consultar gatos resgatados por período")
    print("2) Consultar gatos adotados por período")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        ano_inicio = input("Digite o ano de início para filtragem de resgate: ")
        ano_fim = input("Digite o ano de fim para filtragem de resgate: ")
        
        felinos_filtrados = [felino for felino in felinos if ano_inicio <= felino['Data de Resgate'][-4:] <= ano_fim]
        if felinos_filtrados:
            print("\n=== RESULTADOS DA FILTRAGEM ===")
            for felino in felinos_filtrados:
                print(f"Nome: {felino['Nome']}, Data de Resgate: {felino['Data de Resgate']}")
        else:
            print("Nenhum felino encontrado no período especificado.")
        
    elif opcao == '2':
        ano_inicio = input("Digite o ano de início para filtragem de adoção: ")
        ano_fim = input("Digite o ano de fim para filtragem de adoção: ")
        
        felinos_filtrados = [felino for felino in felinos if felino['Adotado'] == 'Sim' and ano_inicio <= felino['Data de Adoção/Hospedagem'][-4:] <= ano_fim]
        if felinos_filtrados:
            print("\n=== RESULTADOS DA FILTRAGEM ===")
            for felino in felinos_filtrados:
                print(f"Nome: {felino['Nome']}, Data de Adoção/Hospedagem: {felino['Data de Adoção/Hospedagem']}")
        else:
            print("Nenhum felino encontrado no período especificado.")
    
    else:
        print("Opção inválida.")

# Função principal para executar o programa
def main():
    arquivo_csv = 'felinos.csv'
    felinos = carregar_dados(arquivo_csv)
    
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1) Cadastrar felino")
        print("2) Alterar status de felino")
        print("3) Consultar informações sobre felino")
        print("4) Apresentar estatísticas gerais")
        print("5) Filtragem de dados")
        print("6) Salvar")
        print("7) Sair do programa")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_felino(felinos)
        elif opcao == '2':
            alterar_status_felino(felinos)
        elif opcao == '3':
            consultar_informacoes_felino(felinos)
        elif opcao == '4':
            apresentar_estatisticas_gerais(felinos)
        elif opcao == '5':
            realizar_filtragem(felinos)
        elif opcao == '6':
            salvar_dados(arquivo_csv, felinos)
        elif opcao == '7':
            salvar_dados(arquivo_csv, felinos)
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
