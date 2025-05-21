import sys

"""
Model da Agenda
autor: william
refatorado: 21/05/2025
"""

minha_agenda = {}

def cadastrar(agenda, email, nome, idade, endereco, favorito=False):
    status = False
    if email not in agenda:
        agenda[email] = {
            'nome': nome,
            'idade': idade,
            'endereco': endereco,
            'favorito': favorito
        }
        status = True
    return (status, email)

def atualizar(agenda, email, nome, idade, endereco, favorito=False):    
    status = True
    try:
        agenda[email] = {
            'nome': nome,
            'idade': idade,
            'endereco': endereco,
            'favorito': favorito
        }
    except KeyError:
        status = False
    return (status, email)

def favoritar(agenda, email):
    status = True
    try:
        agenda[email]['favorito'] = True        
    except KeyError:
        status = False
    return (status, email)

def apagar(agenda, email):
    status = True
    try:
        del agenda[email]
    except KeyError:
        status = False
    return (status, email)

def consultar(agenda, email):
    status = True
    dados = {}
    try:
        dados = agenda[email]
    except KeyError:
        status = False
    return(status, dados)

def listagem(agenda):
    return (True, agenda.items())

def agenda_init():
    cadastrar(minha_agenda, 'srx@email.com', 'Sr. X', 30, 'Rua x')
    cadastrar(minha_agenda, 'sry@email.com', 'Sr. Y', 31, 'Rua y', True)

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

comandos:
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

agenda_init()
print("Agenda 2025 (CLI) - v.0.2.0 - SENAC Tech - POA/RS")

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
