import pygame
import random


pygame.init()

#colors
white = (255, 255, 255)
red = (155, 0, 0)
green = (0, 255, 0)
black = (0,0,0)
score_color = (133,133,244)

#rectangle configurations to represent the snake 
disp_length, disp_width = 600, 400

dis=pygame.display.set_mode((disp_length,disp_width))

pygame.display.set_caption('Snake Game')


snake_block = 10
snake_speed = 25 # Higher the value of snake_speed==> faster the game is

clock = pygame.time.Clock()

#Font Class with size 50
font_style = pygame.font.SysFont("bahnschrift", 25)

score_font = pygame.font.SysFont("comicsansms", 35)
 
def your_score(score):
    value = score_font.render("score: " + str(score), True, score_color)
    dis.blit(value, [0, 0])

#To display msgs like you lost your score etc we use this method msg
def message(msg, color):
    msg = font_style.render(msg, True, color)
    dis.blit(msg, [disp_length/6, disp_width/3])


def food_pos(disp_length, disp_width, snake_block):
    foodx = round(random.randrange(snake_block, disp_length - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(snake_block, disp_width - snake_block) / 10.0) * 10.0
    return foodx, foody

#for updating the length and its position of the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def start_game():
    game_over = False
    game_close = False
    
    x, y = disp_length/2, disp_width/2
    
    x_change = 0
    y_change = 0
    
    snake_list = []
    snake_length = 1
    
    d = {None: None, 1073741905: 1073741906, 1073741906: 1073741905, 1073741904: 1073741903, 1073741903: 1073741904}

    #Let us randomly produce the x and y coordinates where food is to be placed using random func
    foodx, foody = food_pos(disp_length, disp_width, snake_block)
    past_key = None
    present_key = None
    while not game_over:
        while game_close:
            dis.fill(white)
            message("YOU LOST: press Q- QUIT and C-Play again", red)
            pygame.display.update()
            
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    game_over = True
                    game_close = False
                    
                if(event.type == pygame.KEYDOWN):
                    
                    if(event.key == pygame.K_q or event.key == pygame.K_ESCAPE):
                        game_over = True
                        game_close = False
                    if(event.key == pygame.K_c):
                        start_game()
        
        for event in pygame.event.get():
            #to Quit
            if(event.type == pygame.QUIT):
                game_over = True
            if(event.type == pygame.KEYDOWN):
                past_key = present_key
                if(event.key == pygame.K_DOWN and (event.key != d[past_key] or snake_length== 1)):
                    present_key = pygame.K_DOWN
                    x_change = 0
                    y_change = snake_block
                    
                if(event.key == pygame.K_UP and (event.key != d[past_key] or snake_length== 1)):
                    present_key = pygame.K_UP
                    x_change = 0
                    y_change = -snake_block
                    
                if(event.key == pygame.K_LEFT and (event.key != d[past_key] or snake_length== 1)):
                    present_key = pygame.K_LEFT
                    x_change = -snake_block
                    y_change = 0
         
                if(event.key == pygame.K_RIGHT and (event.key != d[past_key] or snake_length== 1)):
                    present_key = pygame.K_RIGHT
                    x_change = snake_block
                    y_change = 0
        
        
        if(x < 0 or x >= disp_length or y >= disp_width or y < 0):
            game_close = True
            
         
        x += x_change
        y += y_change
        
        dis.fill(white) #used to change the background color
        #rectangle for representing food
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        your_score(snake_length - 1)
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        
        if(len(snake_list) > snake_length):
            del snake_list[0]
        
        if(d[past_key] != present_key):
            for i in snake_list[:-1]:
                if i == snake_head:
                    game_close = True
 
        our_snake(snake_block, snake_list)
        pygame.display.update()
        
        if(x == foodx and y == foody):
            snake_length += 1
            foodx, foody = food_pos(disp_length, disp_width, snake_block)
        

        # greater the value of clock ==> faster the snake ==> HIGHER DIFFICULTY
        clock.tick(snake_speed) 
        
    pygame.quit()


start_game()