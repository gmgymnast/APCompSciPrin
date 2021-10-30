import pygame, sys, random, os
from pygame.math import Vector2

pygame.mixer.pre_init(44100, -16, 2, 512)   
pygame.init()
CURRENT_PATH = "c:/APCompSciPrin/10-26-21_RandomNumbers/Assignment/Snake/"
cell_size, cell_number = 40, 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock, framerate = pygame.time.Clock(), 480
apple = pygame.image.load(os.path.join(CURRENT_PATH + 'res/apple.png')).convert_alpha()
game_font = pygame.font.Font(CURRENT_PATH + 'font/PoetsenOne-Regular.ttf', 25)
menu_main_font = pygame.font.Font(CURRENT_PATH + 'font/PoetsenOne-Regular.ttf', 75)
play_font = pygame.font.Font(CURRENT_PATH + 'font/PoetsenOne-Regular.ttf', 30)
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

class Manager:
     def __init__(self): 
        self.game_state = "Menu"
        self.game_mode = ""
        self.highscore = 0
class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False
        self.manager = Manager()

        self.head_up = pygame.image.load(CURRENT_PATH + 'res/head_up.png').convert_alpha()
        self.head_down = pygame.image.load(CURRENT_PATH + 'res/head_down.png').convert_alpha()        
        self.head_right = pygame.image.load(CURRENT_PATH + 'res/head_right.png').convert_alpha()
        self.head_left = pygame.image.load(CURRENT_PATH + 'res/head_left.png').convert_alpha()
		
        self.tail_up = pygame.image.load(CURRENT_PATH + 'res/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load(CURRENT_PATH + 'res/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load(CURRENT_PATH + 'res/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load(CURRENT_PATH + 'res/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load(CURRENT_PATH + 'res/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load(CURRENT_PATH + 'res/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load(CURRENT_PATH + 'res/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load(CURRENT_PATH + 'res/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load(CURRENT_PATH + 'res/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load(CURRENT_PATH + 'res/body_bl.png').convert_alpha()
        self.crunch_sound = pygame.mixer.Sound(CURRENT_PATH + 'sound/crunch.wav')

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index,block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0: screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1: screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x: screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y: screen.blit(self.body_horizontal, block_rect)
                else: 
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1: screen.blit(self.body_tl, block_rect)
                    if previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1: screen.blit(self.body_bl, block_rect)
                    if previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1: screen.blit(self.body_tr, block_rect)
                    if previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1: screen.blit(self.body_br, block_rect)
    
    def update_head_graphics(self):
       head_rotation = self.body[1] - self.body[0]
       if head_rotation == Vector2(1, 0): self.head = self.head_left
       elif head_rotation == Vector2(-1, 0): self.head = self.head_right
       elif head_rotation == Vector2(0, 1): self.head = self.head_up
       elif head_rotation == Vector2(0, -1): self.head = self.head_down

    def update_tail_graphics(self):
       tail_relation = self.body[-2] - self.body[-1]
       if tail_relation == Vector2(1, 0): self.tail = self.tail_left
       elif tail_relation == Vector2(-1, 0): self.tail = self.tail_right
       elif tail_relation == Vector2(0, 1): self.tail = self.tail_up
       elif tail_relation == Vector2(0, -1): self.tail = self.tail_down

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        elif not 0 <= self.body[0].x < cell_number or not 0 <= self.body[0].y < cell_number: 
            if manager.game_mode == "NoWall":
                body_copy = self.body[:-1]
                body_copy.insert(0, body_copy[0] + self.direction * -cell_number)
                self.body = body_copy[:]
            elif manager.game_mode == "Regular":
                manager.game_state = "GameOver"
                manager.game_mode = ""

        else: 
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def play_cruch_sound(self):
        self.crunch_sound.play()

class Fruit:
    def __init__(self):
        self.randomize()

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rect)

class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.score = 0
        
    def update(self):
        if event.type == SCREEN_UPDATE: self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]: 
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_cruch_sound()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos: self.fruit.randomize()
 
    def check_fail(self):        
        for block in self.snake.body[1:]: 
            if block == self.snake.body[0]: 
                manager.game_state = "GameOver"
                manager.game_mode = ""


    def draw_grass(self):
        grass_color = (167, 209, 61)

        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        self.score = str(len(self.snake.body) - 3)
        score_surface = game_font.render(self.score, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 6, apple_rect.height)

        pygame.draw.rect(screen, (167, 209, 61), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)
        pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)

class Menu:
    def __init__(self): 
        self.main = Main()
        self.manager = Manager()

    def draw_elements(self):
        self.main.draw_grass()
        self.draw_welcome()

    def draw_welcome(self):
        title_text, regular_mode_text, no_wall_mode_text = "Snake", "Press 1 To Play Regular Mode", "Press 2 To Play Wallless Mode" 

        title_surface = menu_main_font.render(title_text, True, (56, 74, 12))
        regular_mode_surface = play_font.render(regular_mode_text, True, (56, 74, 12))
        no_wall_surface = play_font.render(no_wall_mode_text, True, (56, 74, 12))
        
        title_rect = title_surface.get_rect(center = ((400, 150)))
        regular_mode_rect = regular_mode_surface.get_rect(center = ((400, 225)))
        no_wall_mode_rect = no_wall_surface.get_rect(center = ((400, 275)))

        screen.blit(title_surface, title_rect)
        screen.blit(regular_mode_surface, regular_mode_rect)
        screen.blit(no_wall_surface, no_wall_mode_rect)

class GameOver:
    def __init__(self):
        self.main = Main()
        self.manager = Manager()
        if int(self.main.score) > int(self.manager.highscore): self.manager.highscore = self.main.score

    def draw_elements(self):
        self.main.draw_grass()
        self.draw_game_over()

    def draw_game_over(self):
        title_text, regular_mode_text, no_wall_mode_text = "Game Over", "Press 1 To Play Regular Mode", "Press 2 To Play Wallless Mode" 
        highscore_text = "High Score:", str(self.manager.highscore)

        title_surface = menu_main_font.render(title_text, True, (56, 74, 12))
        regular_mode_surface = play_font.render(regular_mode_text, True, (56, 74, 12))
        no_wall_surface = play_font.render(no_wall_mode_text, True, (56, 74, 12))
        highscore_surface = play_font.render(str(highscore_text), True, (56, 74, 12))
        
        title_rect = title_surface.get_rect(center = ((400, 150)))
        regular_mode_rect = regular_mode_surface.get_rect(center = ((400, 225)))
        no_wall_mode_rect = no_wall_surface.get_rect(center = ((400, 275)))
        highscore_rect = highscore_surface.get_rect(center = ((400, 350)))

        screen.blit(title_surface, title_rect)
        screen.blit(regular_mode_surface, regular_mode_rect)
        screen.blit(no_wall_surface, no_wall_mode_rect)
        screen.blit(highscore_surface, highscore_rect)

menu, main_game, manager, game_over= Menu(), Main(), Manager(), GameOver()

while True:
    for event in pygame.event.get():
        if manager.game_state == "Game":
                if event.type == SCREEN_UPDATE: main_game.update()
                if event.type == pygame.KEYDOWN: movement()
        if event.type == pygame.KEYDOWN:
            if manager.game_state == "Menu" or manager.game_state == "GameOver":
                if event.key == pygame.K_1: 
                    manager.game_mode = "Regular"
                    manager.game_state = "Game"
                if event.key == pygame.K_2: 
                    manager.game_mode = "NoWall"
                    manager.game_state = "Game"    
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit() 

    screen.fill((175, 215, 70))

    if manager.game_state == "Menu": menu.draw_elements()
    elif manager.game_state == "Game": main_game.draw_elements()
    elif manager.game_state == "GameOver": game_over.draw_elements() 

    pygame.display.update()
    clock.tick(framerate)

    def movement():
        if event.key == pygame.K_UP: 
            if main_game.snake.direction.y != 1: main_game.snake.direction = Vector2(0, -1)
        if event.key == pygame.K_RIGHT: 
            if main_game.snake.direction.x != -1: main_game.snake.direction = Vector2(1, 0)
        if event.key == pygame.K_DOWN:
            if main_game.snake.direction.y != -1: main_game.snake.direction = Vector2(0, 1)
        if event.key == pygame.K_LEFT: 
            if main_game.snake.direction.x != 1: main_game.snake.direction = Vector2(-1, 0)