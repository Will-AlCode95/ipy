# heroi nome altair vida 100hp ataque 20
#inimigo monstro zumbi vida 100  ataque 20
#personagens possuiem nome, vida, ataque

import random

class Personagem:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.forca = forca

    def atacar(self, inimigo):
        print(f"\n{self.nome} ataca {inimigo.nome} causando {self.forca} de dano!")
        inimigo.vida -= self.forca
        if inimigo.vida <= 0:
            inimigo.vida = 0
            print(f"{inimigo.nome} foi derrotado!")
        else:
            print(f"{inimigo.nome} tem {inimigo.vida} de vida restante.")

    def curar(self):
        cura = random.randint(10, 25)
        self.vida += cura
        print(f"\n{self.nome} se curou em {cura} pontos! Vida atual: {self.vida}")

    def status(self):
        print(f"{self.nome} - Vida: {self.vida} | Força: {self.forca}")

menu = -0

while menu != 0:

    print("Escolha seu personagem:")
    print("1 - Guerreiro ⚔️ (Vida alta, força média)")
    print("2 - Mago 🧙 (Vida média, força alta)")
    print("3 - Arqueiro 🏹 (Vida baixa, força razoável)")0

    goblim = Personagem("goblim", 100, 15)
    menu = int(input("Digite 1, 2 ou 3: "))

    if menu == "1":
        heroi = Personagem("Guerreiro", 120, 18)
    elif menu == "2":
        heroi = Personagem("Mago", 90, 25)
    elif menu == "3":
        heroi = Personagem("Arqueiro", 80, 20)
    else:
        print("Opção inválida! Tente novamente.")
        
goblim = Personagem("goblim", 100, 15)

while heroi.vida > 0 and goblim.vida > 0:
    print("\n--- STATUS ---")
    heroi.status()
    goblim.status()

    print("\n--- SUA VEZ ---")
    print("1 - Atacar")
    print("2 - Curar")
    print("3 - Sair")
    escolha = input("Escolha sua ação: ")   
    
    import random

class Personagem:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.forca = forca

    def atacar(self, inimigo):
        print(f"\n{self.nome} ataca {inimigo.nome} causando {self.forca} de dano!")
        inimigo.vida -= self.forca
        if inimigo.vida <= 0:
            inimigo.vida = 0
            print(f"{inimigo.nome} foi derrotado!")
        else:
            print(f"{inimigo.nome} tem {inimigo.vida} de vida restante.")

    def curar(self):
        cura = random.randint(10, 25)
        self.vida += cura
        print(f"\n{self.nome} se curou em {cura} pontos! Vida atual: {self.vida}")

    def status(self):
        print(f"{self.nome} - Vida: {self.vida} | Força: {self.forca}")

# 🎮 ESCOLHA DO PERSONAGEM
print("Escolha seu personagem:")
print("1 - Guerreiro ⚔️ (Vida alta, força média)")
print("2 - Mago 🧙 (Vida média, força alta)")
print("3 - Arqueiro 🏹 (Vida baixa, força razoável)")

opcao = input("Digite 1, 2 ou 3: ")

if opcao == "1":
    heroi = Personagem("Guerreiro", 120, 18)
elif opcao == "2":
    heroi = Personagem("Mago", 90, 25)
elif opcao == "3":
    heroi = Personagem("Arqueiro", 80, 20)
else:
    print("Opção inválida! Você será um Guerreiro por padrão.")
    heroi = Personagem("Guerreiro", 120, 18)

# 👾 Criando inimigo
goblim = Personagem("goblim", 100, 15)

# 🔁 LOOP DO JOGO
while heroi.vida > 0 and goblim.vida > 0:
    print("\n--- STATUS ---")
    heroi.status()
    goblim.status()

    print("\n--- SUA VEZ ---")
    print("1 - Atacar")
    print("2 - Curar")
    print("3 - Sair")
    escolha = input("Escolha sua ação: ")

    if escolha == "1":
        heroi.atacar(goblim)
    elif escolha == "2":
        heroi.curar()
    elif escolha == "3":
        print("Você fugiu da batalha!")
        break
    else:
        print("Escolha inválida. Tente novamente.")
        continue

    # Monstro revida se ainda estiver vivo
    if goblim.vida > 0:
        print("\n--- TURNO DO MONSTRO ---")
        goblim.atacar(heroi)

# 🏁 Fim de jogo
print("\n--- FIM DE JOGO ---")
if heroi.vida <= 0:
    print("☠️ Você foi derrotado!")
elif goblim.vida <= 0:
    print(f"🎉 {heroi.nome} venceu a batalha!")
