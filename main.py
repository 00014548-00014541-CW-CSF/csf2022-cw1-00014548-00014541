import pygame
import random

pygame.init()

white = (245, 245, 245)
yellow = (255, 215, 0)
black = (0, 0, 0)
red = (255,0,0)
green = (124,252,0)
blue = (30, 144, 255)
mediumaquamarine = (255,0,255)
mediumspringgreen = (60,179,113)
mediumvioletred = (0,250,154)
mintcream = (245,255,250)
moccasin = (15,95,250)
navy = (255,228,181)
olive = (0,0,128)
orange = (128,128,0)
orchid = (255,165,0)
palegreen = (218,112,214)
palevioletred = (255,218,185)
peachpuff = (219,112,147)
pink = (255,192,203)
powderblue = (176,224,230)
royalblue = (65,105,225)
salmon = (250,128,114)
seagreen = (46,139,87)
sienna = (160,82,45)
skyblue = (135,206,235)
slategray = (112,128,144)
springgreen = (0,255,127)
tan = (210,180,140)
thistle = (216,191,216)
turquoise = (64,224,208)

colors = [yellow, red, green, blue, mediumaquamarine, mediumspringgreen, mediumvioletred, mintcream, moccasin, navy, olive, orange,
         orchid, palegreen, palevioletred, pink, powderblue, royalblue, salmon, seagreen, sienna, skyblue, slategray, thistle, turquoise]

dis_width = 600
dis_height = 500

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 15)


def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0, 0])
#
# def timer(counter):
#     text = score_font.render("TIMER:" + str(counter), True, red)
#     dis.blit(text, [100, 100])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def game_win(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def our_food(snake_block, food, colors):
    try:
        for x in range(len(colors)):
            pygame.draw.rect(dis, colors[x], [food[f'foodx{x}'], food[f'foody{x}'], snake_block, snake_block])
    except Exception as ex:
        print(ex)

def gameLoop():
    counter = 30
    text = score_font.render("TIMER:" + str(counter), True, red)

    timer_event = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_event, 1000)

    game_over = False
    game_close = False
    game_win = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    food = {}

    for i in range(0, 25):
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        d2 = {k: v for k, v in ((f'foodx{i}', foodx), (f'foody{i}', foody))}
        food.update(d2)

    while not game_over:
        clock.tick(60)
        while game_close == True:
            dis.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        while game_win == True:
            dis.fill(black)
            message("You won! Press C-play Again or Q-quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == timer_event:
                counter -= 1
                text = score_font.render("TIMER:" + str(counter), True, red)
                if counter == 0:
                    pygame.time.set_timer(timer_event, 0)
                    game_close = True
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        dis.blit(text, [530, 0])
        our_food(snake_block, food, colors)
        our_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)

        pygame.display.update()

        for x in range(0, 25):
            if x1 == food[f'foodx{x}'] and y1 == food[f'foody{x}']:
                food[f'foodx{x}'] = -100
                food[f'foody{x}'] = -100
                Length_of_snake += 1
        if Length_of_snake == 5:
            game_win = True
        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()