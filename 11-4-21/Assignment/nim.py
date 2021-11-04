import pygame, sys, random, os

pygame.mixer.pre_init(44100, -16, 2, 512)   
pygame.init()
CURRENT_PATH = "c:/Code/APCompSciPrin/11-4-21/Assignment/"
width = 1280
height = 853
screen = pygame.display.set_mode((width, height))
clock, framerate = pygame.time.Clock(), 480
marble = pygame.image.load(os.path.join(CURRENT_PATH + 'res/marble.png')).convert_alpha()
game_font = pygame.font.Font(CURRENT_PATH + 'font/PoetsenOne-Regular.ttf', 25)
menu_main_font = pygame.font.Font(CURRENT_PATH + 'font/PoetsenOne-Regular.ttf', 75)
play_font = pygame.font.Font(CURRENT_PATH + 'font/PoetsenOne-Regular.ttf', 30)
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

class Manager:
     def __init__(self): 
        self.game_state = "Menu"
    
class Marble:
    def __init__(self):
        self.numMar = random.randint(10, 100)

    def draw_marble(self):
        if self.numMar >= 10: 
            for i in range(self.numMar // 10): 
                for j in range(10):
                    screen.blit(marble, (j * 75, i * 65, 70, 56))

class Main:
    def __init__(self):
        self.marble = Marble()
        self.table = pygame.image.load(os.path.join(CURRENT_PATH + 'res/table.jfif')).convert_alpha()
        self.score = 0

    def draw_elements(self):
        self.draw_table()
        self.marble.draw_marble()
        self.draw_player()
        self.draw_computer()

    def draw_table(self):
        table_rect = pygame.Rect(0, 0, 1280, 853)
        screen.blit(self.table, table_rect)

    def draw_computer(self):
        print()

    def draw_player(self):
        print()

class Menu:
    def __init__(self): 
        self.main = Main()
        self.manager = Manager()

    def draw_elements(self):
        self.main.draw_table()
        self.draw_welcome()

    def draw_welcome(self):
        title_text, regular_mode_text = "Nim", "Press 1 To Play"

        title_surface = menu_main_font.render(title_text, True, (56, 74, 12))
        regular_mode_surface = play_font.render(regular_mode_text, True, (56, 74, 12))

        title_rect = title_surface.get_rect(center = ((1280 / 2, 300)))
        regular_mode_rect = regular_mode_surface.get_rect(center = ((1280 / 2, 500)))

        screen.blit(title_surface, title_rect)
        screen.blit(regular_mode_surface, regular_mode_rect)

class GameOver:
    def __init__(self):
        self.main = Main()
        self.manager = Manager()

    def draw_elements(self):
        self.main.draw_table()
        self.draw_game_over()

    def draw_game_over(self):
        title_text, regular_mode_text = "Game Over", "Press 1 To Play"

        title_surface = menu_main_font.render(title_text, True, (56, 74, 12))
        regular_mode_surface = play_font.render(regular_mode_text, True, (56, 74, 12))

        title_rect = title_surface.get_rect(center = ((1280 / 2, 300)))
        regular_mode_rect = regular_mode_surface.get_rect(center = ((1280 / 2, 500)))

        screen.blit(title_surface, title_rect)
        screen.blit(regular_mode_surface, regular_mode_rect)

menu, main_game, manager, game_over= Menu(), Main(), Manager(), GameOver()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if manager.game_state == "Menu" or manager.game_state == "GameOver":
                if event.key == pygame.K_1: 
                    manager.game_state = "Game"  
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit() 

    screen.fill((175, 215, 70))

    if manager.game_state == "Menu": menu.draw_elements()
    elif manager.game_state == "Game": 
        main_game.draw_elements()
    elif manager.game_state == "GameOver": 
        game_over.draw_elements() 

    pygame.display.update()
    clock.tick(framerate)