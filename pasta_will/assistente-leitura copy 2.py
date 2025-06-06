titulos = []          # Lista dos títulos dos livros
autores = []          # Lista dos autores
total_paginas = []    # Lista do total de páginas de cada livro
paginas_atuais = []   # Lista da página atual de cada livro
total_livros = 0    

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

