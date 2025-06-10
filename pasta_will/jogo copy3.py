class Personagem:
    """
    Representa um personagem no jogo, seja o herói ou um inimigo.
    """
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.forca = forca
        self.vida_maxima = vida # Armazena a vida máxima inicial para o limite de cura

    def atacar(self, inimigo):
        """
        Realiza um ataque contra um inimigo, diminuindo a vida dele.
        """
        print(f"{self.nome} ataca {inimigo.nome} causando {self.forca} de dano!")
        inimigo.vida -= self.forca
        if inimigo.vida <= 0:
            inimigo.vida = 0 # Garante que a vida não fique negativa
            print(f"{inimigo.nome} foi derrotado!")
        else:
            print(f"{inimigo.nome} tem {inimigo.vida} de vida restante.")

    def curar(self):
        """
        Cura o personagem, aumentando sua vida, mas sem ultrapassar a vida máxima.
        """
        self.vida += 20
        if self.vida > self.vida_maxima:
            self.vida = self.vida_maxima # Limita a cura à vida máxima
        print(f"{self.nome} se curou! Vida agora é {self.vida}.")

    def status(self):
        """
        Exibe o status atual do personagem (nome, vida e força).
        """
        print(f"{self.nome} - Vida: {self.vida}/{self.vida_maxima} | Força: {self.forca}")

# --- INÍCIO DO JOGO ---

# ESCOLHA DE PERSONAGEM
print("Bem-vindo(a) à aventura!")
print("Escolha seu personagem:")
print("1 - Guerreiro (Vida: 120, Força: 25) - Ótimo em combate corpo a corpo.")
print("2 - Mago (Vida: 50, Magia: 40) - Especialista em magia, mas menos vida.")
print("3 - Arqueiro (Vida: 80, Forca: 20) - Preciso e ágil, com bom equilíbrio.")

heroi = None
# Loop para garantir que o usuário escolha uma opção válida
while heroi is None:
    opcao = input("Escolha 1, 2 ou 3: ")
    if opcao == "1":
        heroi = Personagem("Guerreiro", 120, 25)
    elif opcao == "2":
        heroi = Personagem("Mago", 50, 40)
    elif opcao == "3":
        heroi = Personagem("Arqueiro", 80, 20)
    else:
        print("Opção inválida! Por favor, escolha 1, 2 ou 3.")

print(f"\nVocê escolheu o **{heroi.nome}**! Prepare-se para a batalha.")
heroi.status()

# Criação do monstro
monstro = Personagem("Goblim", 100, 20)
print(f"\nDe repente, um **{monstro.nome}** surge das sombras!")
monstro.status()

# ... (código da classe Personagem e escolha de personagem permanecem os mesmos) ...

# Criação do monstro (se você estiver colando apenas esta parte, certifique-se que 'monstro' e 'heroi' estão definidos)
# monstro = Personagem("Monstro Malvado", 100, 15)
# print(f"\nDe repente, um **{monstro.nome}** surge das sombras!")
# monstro.status()

# Variável para controlar se o monstro já usou a habilidade de aumento de força
# Isso evita que ele aumente a força a cada turno quando estiver com a vida baixa
monstro_ja_fortalecido = False

# --- LOOP PRINCIPAL DO JOGO ---
while heroi.vida > 0 and monstro.vida > 0:
    print("\n--- SEU TURNO ---")
    heroi.status()
    monstro.status()
    print("\nO que deseja fazer?")
    print("1 - Atacar")
    print("2 - Curar")
    print("3 - Sair da aventura")

    escolha = input("Sua ação: ")

    if escolha == "1":
        heroi.atacar(monstro)
    elif escolha == "2":
        heroi.curar()
    elif escolha == "3":
        print("Você decidiu sair da aventura. Até a próxima!")
        break # Sai do loop do jogo
    else:
        print("Escolha inválida. Por favor, selecione uma opção válida.")
        continue # Continua o loop para pedir uma nova entrada

    # Turno do monstro só ocorre se ele e o herói ainda estiverem vivos
    if monstro.vida > 0 and heroi.vida > 0:
        print("\n--- TURNO DO MONSTRO ---")
        # Lógica de decisão do monstro:
        # Se a vida do monstro for menor ou igual a 30 E ele ainda não tiver usado o aumento de força
        if monstro.vida <= 30 and not monstro_ja_fortalecido:
            print(f"{monstro.nome} sente a derrota se aproximando e Ruge! Sua força aumenta!")
            monstro.forca += 10 # Aumenta a força do monstro em 10 (você pode ajustar este valor)
            monstro_ja_fortalecido = True # Marca que ele já usou essa habilidade
            print(f"A força de {monstro.nome} agora é {monstro.forca}!")
            # O monstro ataca logo após o aumento de força para não perder o turno
            monstro.atacar(heroi)
        else:
            monstro.atacar(heroi)

# --- FIM DO JOGO ---