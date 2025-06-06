class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, inimigo):
        print(f"{self.nome} ataca {inimigo.nome} causando {self.ataque} de dano!")
        inimigo.vida -= self.ataque  #-= diferente
        if inimigo.vida <= 0:
            print(f"{inimigo.nome} foi derrotado!")
        else:
            print(f"{inimigo.nome} tem {inimigo.vida} de vida restante.")

    def status(self):
        print(f"{self.nome} - Vida: {self.vida} | Força: {self.ataque}")

# Criando personagens
heroi = Personagem("Herói", 100, 20)
monstro = Personagem("Monstro", 80, 15)

# Mostra status dos personagens
heroi.status()
monstro.status()

print("\n--- Batalha ---")
heroi.atacar(monstro)  # Herói ataca Monstro
monstro.atacar(heroi)  # Monstro revida

