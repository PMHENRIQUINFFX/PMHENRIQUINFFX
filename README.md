import random
import time
class Personagem:
    def __init__(self, nome, vida, energia, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.energia = energia
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, inimigo):
        dano = random.randint(self.ataque - 5, self.ataque + 5)
        dano -= inimigo.defesa // 2
        dano = max(dano, 0)
        inimigo.vida -= dano
        print(f"{self.nome} ataca {inimigo nome} e causa {dano} de dano!")

    def usar_tecnica(self, inimigo):
        if self.energia < 20:
            print(f"{self.nome} tentou usar uma técnica, mas não tem energia suficiente!")
            return
        dano = random.randint(30, 50)
        self.energia -= 20
        inimigo.vida -= dano
        print(f"{self.nome} usa uma Técnica Amaldiçoada em {inimigo.nome} causando {dano} de dano!")

    def restaurar_energia(self):
        recuperado = random.randint(10, 20)
        self.energia += recuperado
        print(f"{self.nome} canaliza energia amaldiçoada e recupera {recuperado} de energia.")

    def status(self):
        print(f"{self.nome} - Vida: {self.vida} | Energia: {self.energia}")

def batalha(jogador, inimigo):
    print("\n⚔️ Batalha Iniciada!\n")
    while jogador.vida > 0 and inimigo.vida > 0:
        jogador.status()
        inimigo.status()

        print("\nEscolha sua ação:")
        print("1 - Ataque Normal")
        print("2 - Técnica Amaldiçoada")
        print("3 - Canalizar Energia")
        escolha = input("-> ")

        if escolha == "1":
            jogador.atacar(inimigo)
        elif escolha == "2":
            jogador.usar_tecnica(inimigo)
        elif escolha == "3":
            jogador.restaurar_energia()
        else:
            print("Escolha inválida!")

        time.sleep(1)

        if inimigo.vida > 0:
            acao_inimigo = random.choice(["atacar", "tecnica", "energia"])
            if acao_inimigo == "atacar":
                inimigo.atacar(jogador)
            elif acao_inimigo == "tecnica":
                inimigo.usar_tecnica(jogador)
            else:
                inimigo.restaurar_energia()

        time.sleep(1)

    print("\n⚔️ Batalha Encerrada!")
    if jogador.vida > 0:
        print("🎉 Você venceu a maldição!")
    else:
        print("💀 Você foi derrotado...")

# Criar o personagem do jogador
print("Bem-vindo ao RPG de Jujutsu Kaisen!")
nome = input("Escolha o nome do seu feiticeiro: ")
jogador = Personagem(nome, vida=100, energia=50, ataque=20, defesa=10)

# Criar um inimigo maldição
maldição = Personagem("Maldição de Grau Especial", vida=120, energia=50, ataque=18, defesa=8)

# Começar a batalha
batalha(jogador, maldição)
