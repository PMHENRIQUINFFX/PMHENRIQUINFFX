import pygame
import random


def init_pygame():
    pygame.init()
    largura, altura = 800, 600
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("RPG 2D Evoluído")
    fonte = pygame.font.SysFont(None, 24)
    clock = pygame.time.Clock()
    return tela, fonte, clock, largura, altura


# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 200, 0)
VERMELHO = (200, 0, 0)
AMARELO = (200, 200, 0)


class Player:
    def __init__(self, x=100, y=100):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.vida = 100.0
        self.vel = 5
        self.inventario = []
        self.xp = 0
        self.nivel = 1

    def mover(self, teclas, largura, altura):
        if teclas[pygame.K_w]:
            self.rect.y -= self.vel
        if teclas[pygame.K_s]:
            self.rect.y += self.vel
        if teclas[pygame.K_a]:
            self.rect.x -= self.vel
        if teclas[pygame.K_d]:
            self.rect.x += self.vel

        self.rect.x = max(0, min(self.rect.x, largura - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, altura - self.rect.height))

    def atacar(self, inimigos):
        # Dano simples: reduz vida do inimigo ao colidir
        for i in inimigos[:]:
            if self.rect.colliderect(i.rect):
                i.vida -= 10
                if i.vida <= 0:
                    drop_x, drop_y = i.rect.center
                    inimigos.remove(i)
                    self.xp += 2
                    return drop_x, drop_y
        return None

    def desenhar(self, tela):
        pygame.draw.rect(tela, VERDE, self.rect)


class Enemy:
    def __init__(self, largura, altura):
        self.rect = pygame.Rect(
            random.randint(0, largura - 40), random.randint(0, altura - 40), 40, 40
        )
        self.vida = 20

    def atacar(self, player):
        if self.rect.colliderect(player.rect):
            player.vida -= 0.2

    def desenhar(self, tela):
        pygame.draw.rect(tela, VERMELHO, self.rect)


class Item:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x - 10, y - 10, 20, 20)
        self.tipo = random.choice(["Poção", "Ouro"])

    def desenhar(self, tela):
        pygame.draw.rect(tela, AMARELO, self.rect)


class Quest:
    def __init__(self, objetivo=5):
        self.objetivo = objetivo
        self.progresso = 0
        self.completa = False

    def atualizar(self):
        if self.progresso >= self.objetivo:
            self.completa = True


def main():
    tela, fonte, clock, LARGURA, ALTURA = init_pygame()

    player = Player()
    quest = Quest()
    inimigos = [Enemy(LARGURA, ALTURA) for _ in range(3)]
    itens = []

    rodando = True
    while rodando:
        clock.tick(60)
        tela.fill(PRETO)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                rodando = False

        teclas = pygame.key.get_pressed()
        player.mover(teclas, LARGURA, ALTURA)

        if teclas[pygame.K_SPACE]:
            drop = player.atacar(inimigos)
            if drop:
                quest.progresso += 1
                if random.random() < 0.7:
                    itens.append(Item(drop[0], drop[1]))

        for inimigo in inimigos:
            inimigo.atacar(player)

        for item in itens[:]:
            if player.rect.colliderect(item.rect):
                player.inventario.append(item.tipo)
                itens.remove(item)

        if len(inimigos) < 5:
            inimigos.append(Enemy(LARGURA, ALTURA))

        quest.atualizar()

        # Desenhar
        player.desenhar(tela)
        for inimigo in inimigos:
            inimigo.desenhar(tela)
        for item in itens:
            item.desenhar(tela)

        # HUD
        tela.blit(fonte.render(f"Vida: {int(player.vida)}", True, BRANCO), (10, 10))
        tela.blit(fonte.render(f"XP: {player.xp}", True, BRANCO), (10, 30))
        tela.blit(
            fonte.render(f"Quest: {quest.progresso}/{quest.objetivo}", True, BRANCO),
            (10, 50),
        )

        if quest.completa:
            tela.blit(fonte.render("QUEST COMPLETA! 🎉", True, BRANCO), (300, 10))

        if player.vida <= 0:
            tela.blit(fonte.render("GAME OVER", True, BRANCO), (350, 300))
            pygame.display.update()
            pygame.time.delay(2000)
            rodando = False

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
