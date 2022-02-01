import pygame

# Initialisation
pygame.init()

# Initialisation de la fenêtre
screen = pygame.display.set_mode((800, 600))  # Attention à bien rentrer un tuple

# Initialisation de l'icône et du titre
pygame.display.set_caption("Space invaders")
icone = pygame.image.load("fleche.jpg")
pygame.display.set_icon(icone)

# Joueur
img_joueur = pygame.image.load("space-invaders.png")
joueurX = 368
joueurY = 500

# Variables pour le déplacement
x_change = 0
y_change = 0


def joueur(x, y):
    screen.blit(img_joueur, (x, y))


# Variable de conditionnement, pour arrêter le programme on passera cette variable à false
running = True

while running:
    # Mise de l'arrière-plan en violet (RGB)
    screen.fill((50, 50, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Déplacements
        # Lorsque les flèches sont pressées
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -0.1
            if event.key == pygame.K_RIGHT:
                x_change = 0.1
            if event.key == pygame.K_DOWN:
                y_change = 0.1
            if event.key == pygame.K_UP:
                y_change = -0.1

        # Lorsque les flèches sont relâchées
        if event.type == pygame.KEYUP:
            x_change = 0
            y_change = 0

    joueurX += x_change
    joueurY += y_change
    joueur(joueurX, joueurY)

    pygame.display.update()
