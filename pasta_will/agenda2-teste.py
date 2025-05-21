import sys

"""
Agenda 2025 - CLI
Autor: Gustavo Razzera
Atualizado: 21/05/2025
"""

minha_agenda = {}

# ==== Model ====

def cadastrar(agenda, email, nome, idade, endereco, favorito=False):
    if email not in agenda:
        agenda[email] = [nome, idade, endereco, favorito]
        return (True, email)
    return (False, email)

def atualizar(agenda, email, nome, idade, endereco, favorito=False):    
    if email in agenda:
        agenda[email] = [nome, idade, endereco, favorito]
        return (True, email)
    return (False, email)

def favoritar(agenda, email):
    if email in agenda:
        agenda[email][3] = True
        return (True, email)
    return (False, email)

def apagar(agenda, email):
    if email in agenda:
        del agenda[email]
        return (True, email)
    return (False, email)

def consultar(agenda, email):
    if email in agenda:
        return (True, agenda[email])
    return (False, None)

def listagem(agenda):
    return (True, agenda.items())

def agenda_init():
    cadastrar(minha_agenda, 'srx@email.com', 'Sr. X', 30, 'Rua x')
    cadastrar(minha_agenda, 'sry@email.com', 'Sr. Y', 31, 'Rua y', True)

# ==== View ====

def imprimir(registros):
    for email, dados in registros:
        print(f'''e-mail: {email}
    Nome: {dados[0]}
    Idade: {dados[1]}
    Endereço: {dados[2]}
    Favorito: {dados[3]}
    ''')

def imprimir_um(registro):
    email, dados = registro
    print(f'''e-mail: {email}
    Nome: {dados[0]}
    Idade: {dados[1]}
    Endereço: {dados[2]}
    Favorito: {dados[3]}
    ''')

def imprimir_ajuda():
    ajuda = '''
SINTAXE
agenda.py <comando> [parâmetros]

Comandos disponíveis:
ajuda                - mostra esta ajuda
listar               - lista todos os contatos
consultar <email>    - consulta contato pelo e-mail
cadastrar            - cadastra novo contato interativamente
atualizar            - atualiza um contato existente
apagar               - apaga um contato pelo e-mail
favoritar            - marca um contato como favorito
'''
    print(ajuda)

# ==== Controladores ====

def ctrl_ajuda():
    imprimir_ajuda()

def ctrl_listar():
    ok, registros = listagem(minha_agenda)
    if ok:
        imprimir(registros)
    else:
        print("Agenda vazia.")

def ctrl_consultar(email):
    ok, dados = consultar(minha_agenda, email)
    if ok:
        imprimir_um((email, dados))
    else:
        print("Registro não encontrado.")

def ctrl_cadastrar_interativo():
    try:
        email = input("E-mail: ").strip()
        nome = input("Nome: ").strip()
        idade = int(input("Idade: ").strip())
        endereco = input("Endereço: ").strip()
        favorito_input = input("Favorito (s/n): ").strip().lower()
        favorito = favorito_input == 's'

        ok, email = cadastrar(minha_agenda, email, nome, idade, endereco, favorito)
        if ok:
            print(f'{email} cadastrado com sucesso.')
        else:
            print(f'Não cadastrado: {email} já existe na agenda.')
    except Exception as e:
        print(f"Erro no cadastro: {e}")

def ctrl_atualizar_interativo():
    try:
        email = input("E-mail do contato a atualizar: ").strip()
        if email not in minha_agenda:
            print("E-mail não encontrado.")
            return

        nome = input("Novo nome: ").strip()
        idade = int(input("Nova idade: ").strip())
        endereco = input("Novo endereço: ").strip()
        favorito_input = input("Favorito (s/n): ").strip().lower()
        favorito = favorito_input == 's'

        ok, email = atualizar(minha_agenda, email, nome, idade, endereco, favorito)
        if ok:
            print(f'{email} atualizado com sucesso.')
        else:
            print("Erro ao atualizar.")
    except Exception as e:
        print(f"Erro: {e}")

def ctrl_apagar_interativo():
    email = input("E-mail do contato a apagar: ").strip()
    ok, _ = apagar(minha_agenda, email)
    if ok:
        print(f"{email} removido com sucesso.")
    else:
        print("Contato não encontrado.")

def ctrl_favoritar_interativo():
    email = input("E-mail do contato a favoritar: ").strip()
    ok, _ = favoritar(minha_agenda, email)
    if ok:
        print(f"{email} marcado como favorito.")
    else:
        print("Contato não encontrado.")

# ==== Execução Principal ====

agenda_init()
print("Agenda 2025 (CLI) - v.0.3.0 - SENAC Tech - POA/RS")

try:
    comando = sys.argv[1]
except IndexError:
    ctrl_ajuda()
    sys.exit(0)

# Roteador de Comandos
if comando == 'listar':
    ctrl_listar()
elif comando == 'ajuda':
    ctrl_ajuda()
elif comando == 'consultar':
    try:
        email = sys.argv[2]
        ctrl_consultar(email)
    except IndexError:
        print("Informe o e-mail para consultar.")
elif comando == 'cadastrar':
    ctrl_cadastrar_interativo()
elif comando == 'atualizar':
    ctrl_atualizar_interativo()
elif comando == 'apagar':
    ctrl_apagar_interativo()
elif comando == 'favoritar':
    ctrl_favoritar_interativo()
else:
    print("Comando inválido.")
    ctrl_ajuda()
