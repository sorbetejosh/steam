import pygame 
import random
import sys 

pygame.init()
# Dimensiones de la pantalla y el personaje
width, height = 900, 500#dimension de la pantalla
player_width, player_height = 50, 50#tamaño de el personaje
# Configuración de la pantalla
pantalla = pygame.display.set_mode((width, height))#configura la pantalla de ancho y altura
pygame.mixer.music.load(r"C:\Users\BACO\Downloads\y2mate.com - Married Life.mp3")#carga la musica de el juego
pygame.mixer.music.play(-1)#este genera un loop en el juego
pygame.display.set_caption("zapotron👽")#nombre del juego
# Carga de imágenes
background = pygame.image.load("background.png")#es para cargar la imagen de fondo
background = pygame.transform.scale(background, (width, height))#transormar la escala de la imagen a el limite establecido 
imagen1 = pygame.image.load(r"C:\Users\BACO\Desktop\sprites\spriteup.png")#esto es el archivo con el personaje o el sprite
imagen1 = pygame.transform.scale(imagen1, (player_width, player_height)) #esto es para la escala de el personaje
# Define los límites de la pantalla
x_min, x_max = 0, width - player_width
y_min, y_max = 0, height - player_height
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector2(width / 2, height / 2)
#representa el objeto que el personaje debe esquivar
class Obstacle:
    def __init__(self):
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # Rellena el objeto con color rojo
        self.rect = self.image.get_rect()
        self.reset()
    def reset(self):
        # Reinicia la posición del obstaculo y al momento de salir de derecha a izquierda para esquivar
        self.rect.x = random.choice([-self.rect.width, width])
        self.rect.y = random.randint(50, height - 50)
    def update(self):
        self.rect.x -= 400 * dt
        if self.rect.right < 0:
            self.reset()
# Crear el objeto que el personaje debe esquivar
obstacle = Obstacle()
obstacle2 = Obstacle()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pantalla.blit(background, (0, 0))
    pantalla.blit(imagen1, player_pos)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos.y -= 600 * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 600 * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= 600 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 600 * dt

    # Actualiza la posición del personaje con los límites
    player_pos.x = max(x_min, min(player_pos.x, x_max))
    player_pos.y = max(y_min, min(player_pos.y, y_max))

    # Actualiza y pone el objeto que el personaje debe esquivar al momento de salir 
    obstacle.update()
    pantalla.blit(obstacle.image, obstacle.rect)

    # Verificar si el personaje colisiona con el objeto
    if player_pos.x + player_width > obstacle.rect.x and player_pos.x < obstacle.rect.x + obstacle.rect.width and player_pos.y + player_height > obstacle.rect.y and player_pos.y < obstacle.rect.y + obstacle.rect.height:#este fragmento lo que hace es que comprueba si el objeto colisiona con el personaje gracias al hitbox del personaje u del obstaculo
        font = pygame.font.Font(None, 64)
        game_over_text = font.render("PERDISTE, MALO", True, (255, 255, 255))
        pantalla.blit(game_over_text, (width/2 - game_over_text.get_width()/2, height/2 - game_over_text.get_height()/2))
        pygame.display.flip()

        # Espera unos segundos antes de cerrar el juego
        pygame.time.wait(200)
        pygame.quit()
        sys.exit()

    pygame.display.flip()
    dt = clock.tick(60) / 1000
    print(player_pos)

pygame.quit()
