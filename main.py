import pygame
import button

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
LOWER_MARGIN = 100
SIDE_MARGIN = 300

screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
pygame.display.set_caption('Level Editor')

ROWS = 16
MAX_COLS = 150
TILE_SIZE = SCREEN_HEIGHT // ROWS
TILE_TYPES = 21
current_tile = 0
scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1

pine1_img = pygame.image.load('assets/Background/pine1.png').convert_alpha()
pine2_img = pygame.image.load('assets/Background/pine2.png').convert_alpha()
mountain_img = pygame.image.load('assets/Background/mountain.png').convert_alpha()
sky_img = pygame.image.load('assets/Background/sky_cloud.png').convert_alpha()

img_list = []
for x in range(TILE_TYPES):
    img = pygame.image.load(f"assets/tile/{x}.png")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)

GREEN = (65, 106, 41)
WHITE = (255, 255, 255)
RED = (200, 25, 25)

def draw_bg():
    screen.fill(GREEN)
    width = sky_img.get_width()
    for x in range(4):
        screen.blit(sky_img, ((x * width) - scroll * 0.25, 0))
        screen.blit(mountain_img, ((x * width) - scroll * 0.5, SCREEN_HEIGHT - mountain_img.get_height() - 320))
        screen.blit(pine1_img, ((x * width) - scroll * 0.75, SCREEN_HEIGHT - pine1_img.get_height() - 155))
        screen.blit(pine2_img, ((x * width) - scroll * 1.5, SCREEN_HEIGHT - pine2_img.get_height()))


def draw_grid():
    for c in range(MAX_COLS + 1):
        pygame.draw.line(screen, WHITE, (c * TILE_SIZE - scroll, 0), (c * TILE_SIZE  - scroll, SCREEN_HEIGHT))
    for r in range(ROWS + 1):
        pygame.draw.line(screen, WHITE, (0, r * TILE_SIZE), (SCREEN_WIDTH, r * TILE_SIZE))


button_list = []
button_col = 0
button_row = 0
for i in range(len(img_list)):
    tile_button = button.Button(SCREEN_WIDTH + (75 * button_col) + 50, 75 * button_row + 50, img_list[i], 1)
    button_list.append(tile_button)
    button_col += 1
    if button_col == 3:
        button_row += 1
        button_col = 0


run = True
while run:

    clock.tick(FPS)

    draw_bg()
    draw_grid()

    pygame.draw.rect(screen, GREEN, (SCREEN_WIDTH, 0, SIDE_MARGIN, SCREEN_HEIGHT))

    button_count = 0
    for button_count, i in enumerate(button_list):
        if i.draw(screen):
            current_tile = button_count

    pygame.draw.rect(screen, RED, button_list[current_tile].rect, 3)

    if scroll_left == True and scroll > 0:
        scroll -= 5 * scroll_speed
    if scroll_right == True:
        scroll += 5 * scroll_speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                scroll_left = True
            if event.key == pygame.K_RIGHT:
                scroll_right = True
            if event.key == pygame.K_LSHIFT:
                scroll_speed = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False
            if event.key == pygame.K_LSHIFT:
                scroll_speed = 1

    pygame.display.update()

pygame.quit()