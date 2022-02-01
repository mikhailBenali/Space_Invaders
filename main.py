import pygame
from random import randint

# Initialisation
pygame.init()

# Initialisation de la fenêtre
screen = pygame.display.set_mode((800, 600))  # Attention à bien rentrer un tuple

# Initialisation de l'icône et du titre
pygame.display.set_caption("Space invaders")
icon = pygame.image.load("fleche.jpg")
pygame.display.set_icon(icon)
# Initialisation du fond d'écran
background = pygame.image.load("background.jpg")

# Joueur
player_img = pygame.image.load("space-invaders.png")
player_x = 368
player_y = 500
x_change = 0

# Ennemi
enemy_img = pygame.image.load("enemy.png")
enemy_x = randint(0, 800 - 64)
enemy_y = randint(50, 150)
enemy_x_change = 0.4

# Balle
bullet_img = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 0
bullet_y_change = 0.4
bullet_state = "ready"  # "Ready" = Pas encore tiré / "Fired" = Sur l'écran


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y):
    screen.blit(enemy_img, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))


# Variable de conditionnement, pour arrêter le programme on passera cette variable à false
running = True

while running:
    # Apparition du fond d'écran
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Déplacements
        # Lorsque les flèches sont pressées
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                x_change = -0.5
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                x_change = 0.5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                fire_bullet(player_x, player_y)

            # On quitte le programme e appuyant sur escape
            elif event.key == pygame.K_ESCAPE:
                running = False

        # Lorsque les flèches sont relâchées
        if event.type == pygame.KEYUP:
            # Si les flèches gauche et droite sont relâchées
            if event.key == pygame.K_LEFT or event.key == pygame.K_q or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                # Le déplacement horizontal devient nul
                x_change = 0

    # Modification de la position
    player_x += x_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= 800 - 64:  # Taille horizontale de l'écran - Taille horizontale de l'image
        player_x = 800 - 64

    enemy_x += enemy_x_change

    if enemy_x <= 0:
        enemy_x_change = 0.4
        enemy_x = 0
        enemy_y += 64
    elif enemy_x >= 800 - 64:
        enemy_x = 800 - 64
        enemy_x_change = -0.4
        enemy_y += 40

    if bullet_state == "fire":
        bullet_y -= bullet_y_change
        fire_bullet(player_x, player_y)

    player(player_x, player_y)
    enemy(enemy_x, enemy_y)

    pygame.display.update()
