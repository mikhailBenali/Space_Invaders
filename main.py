import pygame
from random import randint
from pygame import mixer

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
# Initialisation de la musique de fond
mixer.music.load("background.wav")
mixer.music.play(-1)

# Joueur
player_img = pygame.image.load("space-invaders.png")
player_x = 368
player_y = 500
x_change = 0

# Enemies
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
nb_of_enemies = 6

for i in range(nb_of_enemies):
    enemy_img.append(pygame.image.load("enemy.png"))
    enemy_x.append(randint(0, 800 - 64))
    enemy_y.append(randint(50, 150))
    enemy_x_change.append(1)

# Balle
bullet_img = pygame.image.load("bullet.png")
bullet_x = player_x
bullet_y = player_y
bullet_y_change = 2
bullet_state = "ready"  # "Ready" = Pas encore tiré / "Fired" = Sur l'écran

score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)

scoreX = 15
scoreY = 15

hit = False


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(player_img, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))


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
                x_change = -1.5
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                x_change = 1.5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_sound = mixer.Sound("laser.wav")
                bullet_sound.play()
                fire_bullet(player_x, bullet_y)
                bullet_x = player_x

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

    # Modification de la position de l'ennemi
    for i in range(nb_of_enemies):
        if not hit:
            enemy_x[i] += enemy_x_change[i]

            if enemy_x[i] <= 0:
                enemy_x_change[i] = 1
                enemy_x[i] = 0
                enemy_y[i] += 64
            elif enemy_x[i] >= 800 - 64:
                enemy_x[i] = 800 - 64
                enemy_x_change[i] = -1
                enemy_y[i] += 40

    # Affichage des ennemis
    for i in range(nb_of_enemies):
        if not hit:
            enemy(enemy_x[i], enemy_y[i], i)

    # Affiche le joueur
    if not hit:
        player(player_x, player_y)

    # Tirs multiples
    if bullet_y <= 0:
        bullet_y = player_y
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    # S'il y a une collision entre une balle et un ennemi
    for i in range(nb_of_enemies):
        if enemy_x[i] <= bullet_x <= enemy_x[i] + 64 and enemy_y[i] + 64 >= bullet_y >= enemy_y[i]:
            enemy_x[i] = randint(0, 800 - 64)
            enemy_y[i] = randint(50, 150)
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
            bullet_y = player_y
            bullet_state = "ready"
            score_value += 1

    for i in range(nb_of_enemies):
        if (player_x <= enemy_x[i] <= player_x + 64) and (player_y <= enemy_y[i] + 64 <= player_y + 64):  # S'il entre en collision avec le joueur
            hit = True

    # Affichage du score

    if not hit:  # Si le joueur n'a pas encore été touché
        show_score(scoreX, scoreY)
    else:
        show_score(350, 250)

    pygame.display.update()
