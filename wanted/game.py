import pygame
import sys
from PIL import Image
import time
import random
from generateFaces import arrangeImagesUniformly, randomPositions, waitUntilClicked


screen_width = 480
screen_height = 700

timer = 10

wantedSign = pygame.image.load("wantedsign.png")
wantedSign = pygame.transform.scale(wantedSign, ((screen_width, screen_height // 2)))
mario = [Image.open("mario.png"),Image.open("mariomain.png")]
wario = [Image.open("wario.png"),Image.open("wariomain.png")]
luigi = [Image.open("luigi.png"),Image.open("luigimain.png")]
yoshi = [Image.open("yoshi.png"),Image.open("yoshimain.png")]


images = [mario, wario, luigi,yoshi]

for i in range(len(images)):
    images[i][0] = images[i][0].resize((58, 62))

selected_characters = random.sample(images, 3)

excluded_character = None

for character in images:
    if character not in selected_characters:
        excluded_character = character
        break

clock = pygame.time.Clock()

num_images = 48

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))

black = (0, 0, 0)
white = (255, 255, 255)

# Create top and bottom screens
top_screen = pygame.Surface((screen_width, screen_height // 2))
bottom_screen = pygame.Surface((screen_width, screen_height // 2))

black_surface = pygame.Surface((screen_width, screen_height))
black_surface.fill(black)

font = pygame.font.Font("mario64ds.ttf", 10)

high_scores = ["Player 1: 1000", "Player 2: 800", "Player 3: 600", "Player 4: 400", "Player 5: 200"]


show_high_scores = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if show_high_scores and event.pos[1] >= screen_height // 2:
                show_high_scores = False

    
    top_screen.fill(black)
    bottom_screen.fill(black)

    if show_high_scores:
        for i, score in enumerate(high_scores):
            text = font.render(score, True, white)
            y = i * 40 + 10
            top_screen.blit(text, (50, y))
    else:
        top_screen.blit(wantedSign, (0, 0))
        characterMain = pygame.image.fromstring(excluded_character[1].tobytes(), excluded_character[1].size, excluded_character[1].mode)

        top_screen.blit(characterMain, (130, 0))
        screen.blit(black_surface, (0, 0))

        positions = randomPositions(num_images,selected_characters,bottom_screen)

        screen.blit(bottom_screen, (0, screen_height // 2))
        screen.blit(top_screen, (0, 0))
        pygame.display.flip()

        waitUntilClicked(positions,bottom_screen)


            
    

        pygame.display.flip()
        

    
    screen.blit(top_screen, (0, 0))
    screen.blit(bottom_screen, (0, screen_height // 2))

    pygame.display.flip()

pygame.quit()
sys.exit()