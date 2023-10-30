import random
import pygame


screen_width = 480
screen_height = 700

image_width = 58
image_height = 62

def randomPositions(num_images, selected_characters, bottom_screen):
    positions = []
    for _ in range(num_images):
        random_image = random.choice(selected_characters)
        x = random.randint(0, (screen_width) - 58)
        y = random.randint(0, (screen_height/2) - 58)
        positions.append((x, y))
        image_surface = pygame.image.fromstring(random_image[0].tobytes(), random_image[0].size, random_image[0].mode)
        bottom_screen.blit(image_surface, (x, y))
    return positions

def arrangeImagesUniformly(selected_characters, bottom_screen):
    num_columns = 8
    num_rows = 6
    image_width = 58
    image_height = 62

    x_spacing = (screen_width - (num_columns * image_width)) // (num_columns - 1)
    y_spacing = ((screen_height // 2) - (num_rows * image_height)) // (num_rows - 1)

    positions = []
    for row in range(num_rows):
        for col in range(num_columns):
            random_image = random.choice(selected_characters)
            x = col * (image_width + x_spacing)
            y = row * (image_height + y_spacing)
            positions.append((x, y))
            image_surface = pygame.image.fromstring(random_image[0].tobytes(), random_image[0].size, random_image[0].mode)
            bottom_screen.blit(image_surface, (x, y))
    return positions

def waitUntilClicked(positions_list,screen):
    clock = pygame.time.Clock()
    clicked = False

    while not clicked:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for x, y in positions_list:
                    if x <= mouse_x <= x + image_width and (y/2) <= mouse_y <= y + image_height:
                        clicked = True
                        break


        for x, y in positions_list:
            pygame.draw.rect(screen, (0, 0, 255), (x, y, image_width, image_height))

        pygame.display.flip()
        clock.tick(60)


