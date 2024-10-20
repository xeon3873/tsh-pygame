import pygame

pygame.init()

screen_width = 1170
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("TSH Pygame")

background = pygame.image.load("배경.jpg")
background = pygame.transform.scale(background, (screen_width, screen_height))

character = pygame.image.load("character/캐릭터-총X버전-removebg-preview.png")
character = pygame.transform.scale(character, (150, 150))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = 500
character_y_pos = 400
character_to_x = 0
character_to_y = 0

weapon = pygame.image.load("총알-누끼버전.png")
weapon = pygame.transform.scale(weapon, (50, 50))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_height = weapon_size[1]
weapon_speed = 10
weapons = []

game_font = pygame.font.Font(None, 40)

ball_images = [
    pygame.image.load("ball/가장큰것.png"),
    pygame.image.load("ball/중간사이즈.png"),
    pygame.image.load("ball/가장작은사이즈.png")
]

balls = []

# 공 크기에 따른 최초 속도
ball_speed_y = [-18, -15, -12, -12]

balls.append({
    "pos_x" : 50, # 공의 x 좌표
    "pos_y" : 50, # 공의 y 좌표
    "img_idx" : 0, # 공의 이미지 인덱스
    "to_x": 3, # x축 이동방향, -3 이면 왼쪽으로, 3 이면 오른쪽으로
    "to_y": -6, # y축 이동방향
    "init_spd_y": ball_speed_y[0]})# y 최초 속도

total_time = 30

game_result = "Game Over"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= 0.8
            elif event.key == pygame.K_RIGHT:
                character_to_x += 0.8
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos], [weapon_y_pos])
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

        character_rect = character.get_rect()
        character_rect.left = character_x_pos
        character_rect.top = character_y_pos

        
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    if character_x_pos > 1000:
        character_x_pos = 1000

    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons]

    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()