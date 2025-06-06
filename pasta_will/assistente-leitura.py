import json
import os
from datetime import datetime

class AssistenteLeitura:
    def __init__(self, arquivo_dados='livros.json'):
        self.arquivo_dados = arquivo_dados
        self.livros = self.carregar_dados()
    
    def carregar_dados(self):
        """Carrega os dados dos livros do arquivo JSON"""
        if os.path.exists(self.arquivo_dados):
            try:
                with open(self.arquivo_dados, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def salvar_dados(self):
        """Salva os dados dos livros no arquivo JSON"""
        with open(self.arquivo_dados, 'w', encoding='utf-8') as f:
            json.dump(self.livros, f, ensure_ascii=False, indent=2)
    
    def cadastrar_livro(self):
        """Cadastra um novo livro"""
        print("\n=== CADASTRAR NOVO LIVRO ===")
        titulo = input("Título do livro: ").strip()
        
        if not titulo:
            print("❌ Título não pode estar vazio!")
            return
            
        if titulo in self.livros:
            print("❌ Este livro já está cadastrado!")
            return
        
        try:
            autor = input("Autor: ").strip()
            total_paginas = int(input("Total de páginas: "))
            
            if total_paginas <= 0:
                print("❌ O total de páginas deve ser maior que zero!")
                return
                
        except ValueError:
            print("❌ Por favor, digite um número válido para as páginas!")
            return
        
        self.livros[titulo] = {
            'autor': autor,
            'total_paginas': total_paginas,
            'pagina_atual': 0,
            'data_cadastro': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        self.salvar_dados()
        print(f"✅ Livro '{titulo}' cadastrado com sucesso!")
    
    def registrar_progresso(self):
        """Registra o progresso de leitura de um livro"""
        if not self.livros:
            print("❌ Nenhum livro cadastrado ainda!")
            return
            
        print("\n=== REGISTRAR PROGRESSO DE LEITURA ===")
        print("Livros disponíveis:")
        
        livros_lista = list(self.livros.keys())
        for i, titulo in enumerate(livros_lista, 1):
            livro = self.livros[titulo]
            print(f"{i}. {titulo} - Página atual: {livro['pagina_atual']}/{livro['total_paginas']}")
        
        try:
            escolha = int(input("\nEscolha o número do livro: ")) - 1
            
            if escolha < 0 or escolha >= len(livros_lista):
                print("❌ Opção inválida!")
                return
                
            titulo_escolhido = livros_lista[escolha]
            livro = self.livros[titulo_escolhido]
            
            print(f"\nLivro selecionado: {titulo_escolhido}")
            print(f"Página atual: {livro['pagina_atual']}")
            print(f"Total de páginas: {livro['total_paginas']}")
            
            nova_pagina = int(input("Em que página você está agora? "))
            
            if nova_pagina < 0:
                print("❌ A página não pode ser negativa!")
                return
            elif nova_pagina > livro['total_paginas']:
                print("❌ A página não pode ser maior que o total de páginas do livro!")
                return
                
            self.livros[titulo_escolhido]['pagina_atual'] = nova_pagina
            self.salvar_dados()
            
            if nova_pagina == livro['total_paginas']:
                print(f"🎉 Parabéns! Você terminou de ler '{titulo_escolhido}'!")
            else:
                restantes = livro['total_paginas'] - nova_pagina
                print(f"✅ Progresso atualizado! Restam {restantes} páginas para terminar.")
                
        except ValueError:
            print("❌ Por favor, digite números válidos!")
    
    def calcular_estatisticas(self, livro):
        """Calcula estatísticas de um livro"""
        total = livro['total_paginas']
        atual = livro['pagina_atual']
        restantes = total - atual
        percentual = (atual / total) * 100 if total > 0 else 0
        
        return {
            'restantes': restantes,
            'percentual': percentual
        }
    
    def listar_todos_livros(self):
        """Lista todos os livros com suas estatísticas"""
        if not self.livros:
            print("❌ Nenhum livro cadastrado ainda!")
            return
            
        print("\n=== TODOS OS LIVROS ===")
        print(f"{'Título':<30} {'Autor':<20} {'Progresso':<15} {'Páginas Rest.':<12} {'% Lido':<8}")
        print("-" * 85)
        
        for titulo, livro in self.livros.items():
            stats = self.calcular_estatisticas(livro)
            progresso = f"{livro['pagina_atual']}/{livro['total_paginas']}"
            
            print(f"{titulo[:29]:<30} {livro['autor'][:19]:<20} {progresso:<15} "
                  f"{stats['restantes']:<12} {stats['percentual']:.1f}%")
    
    def listar_por_status(self, status):
        """Lista livros filtrados por status"""
        if not self.livros:
            print("❌ Nenhum livro cadastrado ainda!")
            return
        
        livros_filtrados = []
        
        for titulo, livro in self.livros.items():
            if status == 'encerradas' and livro['pagina_atual'] == livro['total_paginas']:
                livros_filtrados.append((titulo, livro))
            elif status == 'em_curso' and 0 < livro['pagina_atual'] < livro['total_paginas']:
                livros_filtrados.append((titulo, livro))
            elif status == 'nao_iniciadas' and livro['pagina_atual'] == 0:
                livros_filtrados.append((titulo, livro))
        
        if not livros_filtrados:
            status_nome = {'encerradas': 'encerradas', 'em_curso': 'em curso', 'nao_iniciadas': 'não iniciadas'}
            print(f"❌ Nenhuma leitura {status_nome[status]} encontrada!")
            return
        
        status_titulo = {'encerradas': 'LEITURAS ENCERRADAS', 'em_curso': 'LEITURAS EM CURSO', 'nao_iniciadas': 'LEITURAS NÃO INICIADAS'}
        print(f"\n=== {status_titulo[status]} ===")
        print(f"{'Título':<30} {'Autor':<20} {'Progresso':<15} {'Páginas Rest.':<12} {'% Lido':<8}")
        print("-" * 85)
        
        for titulo, livro in livros_filtrados:
            stats = self.calcular_estatisticas(livro)
            progresso = f"{livro['pagina_atual']}/{livro['total_paginas']}"
            
            print(f"{titulo[:29]:<30} {livro['autor'][:19]:<20} {progresso:<15} "
                  f"{stats['restantes']:<12} {stats['percentual']:.1f}%")
    
    def excluir_livro(self):
        """Exclui um livro do sistema"""
        if not self.livros:
            print("❌ Nenhum livro cadastrado ainda!")
            return
            
        print("\n=== EXCLUIR LIVRO ===")
        print("Livros disponíveis:")
        
        livros_lista = list(self.livros.keys())
        for i, titulo in enumerate(livros_lista, 1):
            print(f"{i}. {titulo}")
        
        try:
            escolha = int(input("\nEscolha o número do livro para excluir: ")) - 1
            
            if escolha < 0 or escolha >= len(livros_lista):
                print("❌ Opção inválida!")
                return
                
            titulo_escolhido = livros_lista[escolha]
            
            confirmacao = input(f"Tem certeza que deseja excluir '{titulo_escolhido}'? (s/N): ").lower()
            
            if confirmacao == 's':
                del self.livros[titulo_escolhido]
                self.salvar_dados()
                print(f"✅ Livro '{titulo_escolhido}' excluído com sucesso!")
            else:
                print("❌ Exclusão cancelada.")
                
        except ValueError:
            print("❌ Por favor, digite um número válido!")
    
    def mostrar_menu(self):
        """Exibe o menu principal"""
        print("\n" + "="*50)
        print("📚 ASSISTENTE DE LEITURA")
        print("="*50)
        print("1. Cadastrar novo livro")
        print("2. Registrar progresso de leitura")
        print("3. Listar todos os livros")
        print("4. Listar leituras encerradas")
        print("5. Listar leituras em curso")
        print("6. Listar leituras não iniciadas")
        print("7. Excluir livro")
        print("0. Sair")
        print("-"*50)
    
    def executar(self):
        """Executa o programa principal"""
        print("📚 Bem-vindo ao Assistente de Leitura!")
        
        while True:
            self.mostrar_menu()
            
            try:
                opcao = input("Escolha uma opção: ").strip()
                
                if opcao == '1':
                    self.cadastrar_livro()
                elif opcao == '2':
                    self.registrar_progresso()
                elif opcao == '3':
                    self.listar_todos_livros()
                elif opcao == '4':
                    self.listar_por_status('encerradas')
                elif opcao == '5':
                    self.listar_por_status('em_curso')
                elif opcao == '6':
                    self.listar_por_status('nao_iniciadas')
                elif opcao == '7':
                    self.excluir_livro()
                elif opcao == '0':
                    print("👋 Obrigado por usar o Assistente de Leitura!")
                    break
                else:
                    print("❌ Opção inválida! Tente novamente.")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Programa encerrado pelo usuário.")
                break
            except Exception as e:
                print(f"❌ Erro inesperado: {e}")

# Execução do programa
if __name__ == "__main__":
    assistente = AssistenteLeitura()
    assistente.executar()