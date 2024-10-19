import pygame

pygame.init()

screen = pygame.display.set_mode((1170, 720))

pygame.display.set_caption("TSH Pygame")

background = pygame.image.load("배경.jpg")
background = pygame.transform.scale(background, (1170, 720))

character = pygame.image.load("character/캐릭터-총X버전-removebg-preview.png")
character = pygame.transform.scale(character, (150, 150))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = 500
character_y_pos = 400
character_to_x = 0
character_to_y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= 1
            elif event.key == pygame.K_RIGHT:
                character_to_x += 1
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
    
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_to_x > 2500:
        character_to_x = 2500

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()