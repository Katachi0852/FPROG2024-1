import re

def senha_valida(senha):
    # Padrão para verificar pelo menos uma letra maiúscula
    padrao_maiuscula = r'[A-Z]'

    # Padrão para verificar pelo menos um caractere numérico
    padrao_numerico = r'\d'

    # Padrão para verificar pelo menos um dos símbolos especiais: *, !, $, #
    padrao_simbolos = r'[*!$#]'

    # Verificar se a senha atende a todos os critérios
    if (re.search(padrao_maiuscula, senha) and
        re.search(padrao_numerico, senha) and
        re.search(padrao_simbolos, senha)):
        return True
    else:
        return False

# Exemplos de uso:
senha1 = "Senha123*"
senha2 = "senha123*"
senha3 = "Senhavalida#"
senha4 = "senhavalida"

print(f"A senha '{senha1}' é válida? {senha_valida(senha1)}")
print(f"A senha '{senha2}' é válida? {senha_valida(senha2)}")
print(f"A senha '{senha3}' é válida? {senha_valida(senha3)}")
print(f"A senha '{senha4}' é válida? {senha_valida(senha4)}")
