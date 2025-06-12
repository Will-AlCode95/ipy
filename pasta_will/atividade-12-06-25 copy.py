import random

def gerar_nome_item():
    """
    Gera um nome aleatório para um item de jogo do tipo rogue
    sorteando de uma lista de nomes prontos.
    """
    
    # Lista com nomes completos de itens prontos
    nomes_itens = [
        "Lilás Gema de Mangur",
        "Arcaica Espada de Minos", 
        "Assassina Pedra perfeita",
        "Silenciosa Rocha rota",
        "Flamejante Lâmina de Ezod",
        "Gélida Espada das Chamas",
        "Venenosa Adaga do Gelo",
        "Sagrada Armadura da Morte",
        "Sombria Gema da Vida",
        "Élfica Lâmina do Dragão",
        "Anã Machado da Serpente",
        "Mágica Poção do Lobo",
        "Ancestral Pergaminho da Águia",
        "Perdida Espada do Leão",
        "Lendária Gema das Trevas",
        "Maldita Adaga da Luz",
        "Brilhante Cristal do Abismo",
        "Etérea Orbe dos Céus",
        "Mortal Bastão da Terra",
        "Divina Armadura dos Ventos",
        "Arcaica Poção das Sombras",
        "Flamejante Escudo de Ferro",
        "Gélida Coroa de Cristal",
        "Venenosa Corda Élfica",
        "Sagrada Lança Dourada",
        "Sombria Capa da Invisibilidade",
        "Mágica Bota de Velocidade",
        "Ancestral Anel de Poder",
        "Perdida Chave do Tempo",
        "Lendária Espada do Destino",
        "Maldita Boneca de Pano",
        "Brilhante Pedra da Sorte",
        "Etérea Pena de Fênix",
        "Mortal Veneno de Cobra",
        "Divina Água Benta",
        "Rustica Faca de Caça",
        "Reluzente Moeda de Ouro",
        "Quebrada Taça de Prata",
        "Misteriosa Caixa Lacrada",
        "Poderosa Varinha Mágica"
    ]
    
    # Sortear e retornar um nome da lista
    nome_sorteado = random.choice(nomes_itens)
    return nome_sorteado


print("=== GERADOR DE NOMES DE ITENS ===")
print()
    
    # Gerar alguns exemplos
for gera in range(10):
    nome_item = gerar_nome_item()
    print(f"Item {gera+1}: {nome_item}")
    
