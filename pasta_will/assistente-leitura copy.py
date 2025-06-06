# Assistente de Leitura - Versão Simples (estilo VisuAlg)

# Variáveis globais (como no VisuAlg)
titulos = []          # Lista dos títulos dos livros
autores = []          # Lista dos autores
total_paginas = []    # Lista do total de páginas de cada livro
paginas_atuais = []   # Lista da página atual de cada livro
total_livros = 0      # Contador de livros

def mostrar_menu():
    print("\n" + "="*40)
    print("    ASSISTENTE DE LEITURA")
    print("="*40)
    print("1 - Cadastrar livro")
    print("2 - Registrar progresso")
    print("3 - Listar todos os livros")
    print("4 - Leituras encerradas")
    print("5 - Leituras em curso")
    print("6 - Leituras não iniciadas")
    print("0 - Sair")
    print("-"*40)

def cadastrar_livro():
    global total_livros
    
    print("\n--- CADASTRAR LIVRO ---")
    
    # Entrada de dados
    titulo = input("Título: ")
    autor = input("Autor: ")
    
    # Validação do número de páginas
    while True:
        try:
            paginas = int(input("Total de páginas: "))
            if paginas > 0:
                break
            else:
                print("Digite um número maior que zero!")
        except:
            print("Digite apenas números!")
    
    # Adicionar nas listas
    titulos.append(titulo)
    autores.append(autor)
    total_paginas.append(paginas)
    paginas_atuais.append(0)  # Começa na página 0
    total_livros = total_livros + 1
    
    print(f"Livro '{titulo}' cadastrado com sucesso!")

def registrar_progresso():
    if total_livros == 0:
        print("Nenhum livro cadastrado!")
        return
    
    print("\n--- REGISTRAR PROGRESSO ---")
    
    # Mostrar livros disponíveis
    print("Livros disponíveis:")
    for i in range(total_livros):
        print(f"{i+1} - {titulos[i]} ({paginas_atuais[i]}/{total_paginas[i]} páginas)")
    
    # Escolher livro
    while True:
        try:
            escolha = int(input("Escolha o número do livro: "))
            if 1 <= escolha <= total_livros:
                escolha = escolha - 1  # Converter para índice (0, 1, 2...)
                break
            else:
                print(f"Digite um número entre 1 e {total_livros}!")
        except:
            print("Digite apenas números!")
    
    # Mostrar informações do livro escolhido
    print(f"\nLivro: {titulos[escolha]}")
    print(f"Página atual: {paginas_atuais[escolha]}")
    print(f"Total de páginas: {total_paginas[escolha]}")
    
    # Registrar nova página
    while True:
        try:
            nova_pagina = int(input("Em que página você está? "))
            if 0 <= nova_pagina <= total_paginas[escolha]:
                paginas_atuais[escolha] = nova_pagina
                break
            else:
                print(f"Digite um número entre 0 e {total_paginas[escolha]}!")
        except:
            print("Digite apenas números!")
    
    # Verificar se terminou o livro
    if nova_pagina == total_paginas[escolha]:
        print("Parabéns! Você terminou o livro!")
    else:
        restantes = total_paginas[escolha] - nova_pagina
        print(f"Progresso atualizado! Restam {restantes} páginas.")

def calcular_percentual(pagina_atual, total):
    if total == 0:
        return 0
    else:
        return (pagina_atual * 100) // total  # Usar // para divisão inteira

def listar_todos():
    if total_livros == 0:
        print("Nenhum livro cadastrado!")
        return
    
    print("\n--- TODOS OS LIVROS ---")
    print(f"{'Título':<25} {'Autor':<20} {'Progresso':<12} {'Restam':<8} {'% Lido'}")
    print("-" * 75)
    
    for i in range(total_livros):
        # Calcular estatísticas
        restantes = total_paginas[i] - paginas_atuais[i]
        percentual = calcular_percentual(paginas_atuais[i], total_paginas[i])
        progresso = f"{paginas_atuais[i]}/{total_paginas[i]}"
        
        # Exibir linha
        print(f"{titulos[i][:24]:<25} {autores[i][:19]:<20} {progresso:<12} {restantes:<8} {percentual}%")

def listar_encerradas():
    print("\n--- LEITURAS ENCERRADAS ---")
    encontrou = False
    
    for i in range(total_livros):
        if paginas_atuais[i] == total_paginas[i]:  # Terminou o livro
            if not encontrou:  # Primeira vez que encontra
                print(f"{'Título':<25} {'Autor':<20} {'Total Páginas'}")
                print("-" * 55)
                encontrou = True
            print(f"{titulos[i][:24]:<25} {autores[i][:19]:<20} {total_paginas[i]}")
    
    if not encontrou:
        print("Nenhuma leitura encerrada!")

def listar_em_curso():
    print("\n--- LEITURAS EM CURSO ---")
    encontrou = False
    
    for i in range(total_livros):
        if 0 < paginas_atuais[i] < total_paginas[i]:  # Começou mas não terminou
            if not encontrou:
                print(f"{'Título':<25} {'Progresso':<12} {'Restam':<8} {'% Lido'}")
                print("-" * 55)
                encontrou = True
            
            restantes = total_paginas[i] - paginas_atuais[i]
            percentual = calcular_percentual(paginas_atuais[i], total_paginas[i])
            progresso = f"{paginas_atuais[i]}/{total_paginas[i]}"
            
            print(f"{titulos[i][:24]:<25} {progresso:<12} {restantes:<8} {percentual}%")
    
    if not encontrou:
        print("Nenhuma leitura em curso!")

def listar_nao_iniciadas():
    print("\n--- LEITURAS NÃO INICIADAS ---")
    encontrou = False
    
    for i in range(total_livros):
        if paginas_atuais[i] == 0:  # Não começou ainda
            if not encontrou:
                print(f"{'Título':<25} {'Autor':<20} {'Total Páginas'}")
                print("-" * 55)
                encontrou = True
            print(f"{titulos[i][:24]:<25} {autores[i][:19]:<20} {total_paginas[i]}")
    
    if not encontrou:
        print("Todas as leituras já foram iniciadas!")

# PROGRAMA PRINCIPAL (como algoritmo no VisuAlg)
def main():
    print("Bem-vindo ao Assistente de Leitura!")
    
    while True:
        mostrar_menu()
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            registrar_progresso()
        elif opcao == "3":
            listar_todos()
        elif opcao == "4":
            listar_encerradas()
        elif opcao == "5":
            listar_em_curso()
        elif opcao == "6":
            listar_nao_iniciadas()
        elif opcao == "0":
            print("Obrigado por usar o programa!")
            break
        else:
            print("Opção inválida!")
        
        input("\nPressione ENTER para continuar...")

# Executar o programa
if __name__ == "__main__":
    main()