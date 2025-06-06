class Personagem:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.forca = forca

    def atacar(self, inimigo):
        print(f"{self.nome} ataca {inimigo.nome} causando {self.forca} de dano!")
        inimigo.vida -= self.forca
        if inimigo.vida <= 0:
            inimigo.vida = 0
            print(f"{inimigo.nome} foi derrotado!")
        else:
            print(f"{inimigo.nome} tem {inimigo.vida} de vida restante.")

    def curar(self):
        self.vida += 15
        print(f"{self.nome} se curou! Vida agora é {self.vida}.")

    def status(self):
        print(f"{self.nome} - Vida: {self.vida} | Força: {self.forca}")

# ESCOLHA DE PERSONAGEM - isso só roda uma vez
print("Escolha seu personagem:")
print("1 - Guerreiro")
print("2 - Mago")
print("3 - Arqueiro")

opcao = input("Escolha 1, 2 ou 3: ")

if opcao == "1":
    heroi = Personagem("Guerreiro", 120, 18)
elif opcao == "2":
    heroi = Personagem("Mago", 60, 25)
elif opcao == "3":
    heroi = Personagem("Arqueiro", 80, 20)
else:
    print("Opção inválida! Personagem padrão escolhido.")
    heroi = Personagem("Guerreiro", 120, 18)

monstro = Personagem("Monstro", 100, 15)

# LOOP PRINCIPAL DO JOGO
while heroi.vida > 0 and monstro.vida > 0:
    print("\n--- MENU ---")
    print("1 - Atacar")
    print("2 - Curar")
    print("3 - Sair")

    escolha = input("O que deseja fazer? ")

    if escolha == "1":
        heroi.atacar(monstro)
    elif escolha == "2":
        heroi.curar()
    elif escolha == "3":
        print("Você saiu do jogo.")
        break
    else:
        print("Escolha inválida.")
        continue

    if monstro.vida > 0:
        print("\nTurno do monstro:")
        monstro.atacar(heroi)

# FIM DE JOGO
print("\n--- FIM ---")
if heroi.vida <= 0:
    print("GAME OVER!")
elif monstro.vida <= 0:
    print("YOU WIN!")
