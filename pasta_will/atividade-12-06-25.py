import random

def gerar_nome_item():
    """
    Gera um nome aleatório para um item de jogo do tipo rogue
    misturando qualidades, nomes e complementos aleatoriamente.
    """
    
    # Lista de qualidades
    qualidades = [
        "Lilás", "Arcaica", "Assassina", "Silenciosa", "Flamejante", 
        "Gélida", "Venenosa", "Sagrada", "Sombria", "Élfica", "Anã",
        "Mágica", "Ancestral", "Perdida", "Lendária", "Maldita", 
        "Brilhante", "Etérea", "Mortal", "Divina", "Rustica", 
        "Reluzente", "Quebrada", "Misteriosa", "Poderosa"
    ]
    
    # Lista de nomes/itens base
    nomes = [
        "Gema", "Espada", "Pedra", "Rocha", "Lâmina", "Escudo", "Anel", 
        "Amuleto", "Poção", "Pergaminho", "Cristal", "Orbe", "Bastão",
        "Adaga", "Arco", "Martelo", "Machado", "Cajado", "Elmo", "Armadura",
        "Coroa", "Corda", "Lança", "Capa", "Bota", "Chave", "Boneca",
        "Taça", "Caixa", "Varinha", "Faca", "Moeda", "Pena", "Veneno"
    ]
    
    # Lista de complementos
    complementos = [
        "de Mangur", "de Minos", "perfeita", "rota", "de Ezod",
        "dos Ventos", "das Chamas", "do Gelo", "da Morte", "da Vida",
        "do Dragão", "da Serpente", "do Lobo", "da Águia", "do Leão",
        "das Trevas", "da Luz", "do Abismo", "dos Céus", "da Terra",
        "das Sombras", "de Ferro", "de Cristal", "Élfica", "Dourada",
        "da Invisibilidade", "de Velocidade", "de Poder", "do Tempo", 
        "do Destino", "de Pano", "da Sorte", "de Fênix", "de Cobra",
        "Benta", "de Caça", "de Ouro", "de Prata", "Lacrada", "Mágica"
    ]
    
    # Sortear um elemento de cada lista
    qualidade_escolhida = random.choice(qualidades)
    nome_escolhido = random.choice(nomes)
    complemento_escolhido = random.choice(complementos)
    
    # Misturar e combinar as partes para formar o nome final
    nome_final = f"{qualidade_escolhida} {nome_escolhido} {complemento_escolhido}"
    
    return nome_final

# Exemplo de uso

print("=== GERADOR DE NOMES DE ITENS (MISTURADOS) ===")
print()
    
    # Gerar alguns exemplos

print()
print("=== TESTE INDIVIDUAL ===")
nome_do_item = gerar_nome_item()
print(f"Nome gerado: {nome_do_item}")
    