import sys
import json
import os

"""
Agenda CLI com persistência em arquivo JSON
Autor: Gustavo Razzera
Versão: 0.3.0 - 21/05/2025
"""

ARQUIVO_AGENDA = 'agenda.json'

def salvar_agenda(agenda):
    with open(ARQUIVO_AGENDA, 'w', encoding='utf-8') as f:
        json.dump(agenda, f, ensure_ascii=False, indent=4)

def carregar_agenda():
    if os.path.exists(ARQUIVO_AGENDA):
        with open(ARQUIVO_AGENDA, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

minha_agenda = carregar_agenda()

def cadastrar(agenda, email, nome, idade, endereco, favorito=False):
    status = False
    if email not in agenda:
        agenda[email] = {
            'nome': nome,
            'idade': idade,
            'endereco': endereco,
            'favorito': favorito
        }
        salvar_agenda(agenda)
        status = True
    return (status, email)

def atualizar(agenda, email, nome, idade, endereco, favorito=False):    
    if email in agenda:
        agenda[email] = {
            'nome': nome,
            'idade': idade,
            'endereco': endereco,
            'favorito': favorito
        }
        salvar_agenda(agenda)
        return (True, email)
    return (False, email)

def favoritar(agenda, email):
    if email in agenda:
        agenda[email]['favorito'] = True
        salvar_agenda(agenda)
        return (True, email)
    return (False, email)

def apagar(agenda, email):
    if email in agenda:
        del agenda[email]
        salvar_agenda(agenda)
        return (True, email)
    return (False, email)

def consultar(agenda, email):
    if email in agenda:
        return (True, agenda[email])
    return (False, {})

def listagem(agenda):
    return (True, agenda.items())

"""
View da agenda
"""
def imprimir(registros):
    for email, dados in registros:        
        print(f'''e-mail: {email}
    Nome: {dados['nome']}        
    Endereço: {dados['endereco']}
    Idade: {dados['idade']}
    Favorito: {dados['favorito']}        
    ''')

def imprimir_um(registro):
    email, dados = registro
    print(f'''e-mail: {email}
    Nome: {dados['nome']}        
    Endereço: {dados['endereco']}
    Idade: {dados['idade']}
    Favorito: {dados['favorito']}        
    ''')

def imprimir_ajuda():
    ajuda = '''
SINTAXE
agenda.py <comando>

comandos disponíveis:
ajuda       - mostra esta ajuda
listar      - lista todos os contatos
cadastrar   - adiciona um novo contato
consultar   - consulta um contato pelo e-mail
apagar      - remove um contato pelo e-mail
favoritar   - marca um contato como favorito
'''
    print(ajuda)

"""
Controlador da Agenda
"""
def ctrl_ajuda():
    imprimir_ajuda()

def ctrl_listar():   
    ok, registros = listagem(minha_agenda)
    if ok:
        imprimir(registros)
    else:
        print("Erro ao listar contatos.")

def ctrl_cadastrar():
    email = input("E-mail: ")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    endereco = input("Endereço: ")
    favorito = input("Favorito? (s/n): ").strip().lower() == 's'
    
    ok, email = cadastrar(minha_agenda, email, nome, idade, endereco, favorito)
    if ok:
        print(f'{email} cadastrado com sucesso')
    else:
        print(f'{email} já existe na agenda')

def ctrl_consultar():
    email = input("E-mail para consulta: ")
    ok, dados = consultar(minha_agenda, email)
    if ok:
        imprimir_um((email, dados))
    else:
        print("Registro não encontrado")

def ctrl_apagar():
    email = input("E-mail para exclusão: ")
    ok, email = apagar(minha_agenda, email)
    if ok:
        print(f'{email} excluído com sucesso')
    else:
        print(f'{email} não encontrado')

def ctrl_favoritar():
    email = input("E-mail para favoritar: ")
    ok, email = favoritar(minha_agenda, email)
    if ok:
        print(f'{email} foi marcado como favorito!')
    else:
        print(f'{email} não existe na agenda')

###############################
# Início da execução programa #
###############################

print("Agenda 2025 (CLI) - v.0.3.0 - SENAC Tech - POA/RS")

try:
    comando = sys.argv[1].lower()
except IndexError:
    ctrl_ajuda()    
    sys.exit(0)

if comando == 'listar':
    ctrl_listar()
elif comando == 'ajuda':
    ctrl_ajuda()
elif comando == 'cadastrar':
    ctrl_cadastrar()
elif comando == 'consultar':
    ctrl_consultar()
elif comando == 'apagar':
    ctrl_apagar()
elif comando == 'favoritar':
    ctrl_favoritar()
else:
    print("Comando desconhecido.")
    ctrl_ajuda()
