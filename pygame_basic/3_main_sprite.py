import pygame

pygame.init()  #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480  #가로 크기
screen_height = 640  #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("강철 게임")  #게임 이름

#배경 이미지 불러오기
background = pygame.image.load(
    "/Users/igangcheol/Desktop/iron_git/python_game/pygame_basic/background.png"
)

#캐릭터 (스프라이트) 불러오기
character = pygame.image.load(
    "/Users/igangcheol/Desktop/iron_git/python_game/pygame_basic/character.png"
)
character_size = character.get_rect().size  # 이미지의 전체적인 (틀)을 구해옴

character_width = character_size[0]  #캐릭터의 가로 크기 지정
character_height = character_size[1]  #캐릭터의 세로 크기 지정

character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height  #화면 세로 크기 가장 아래에 해당하는 곳 위치 (세로)
# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    for event in pygame.event.get():  # 어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 창이 닫히는 이벤트가 발생하면 게임종료 !

    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  #캐릭터 그리기

    pygame.display.update()  #게임화면을 계속 그리기!
# 강철게임 종료
pygame.quit()