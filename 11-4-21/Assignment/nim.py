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
        self.numMar = random.randint(10, 100)
        self.player_turn = 0  # 0 = player, 1 = computer
        self.player_score = 0
        self.computer_score = 0
        self.title_text, self.number_marbles_text = "Enter the Number of Marbles you Want to Take: ", 0

class Marble:
    def __init__(self):
        self.manager = Manager()
        self.num_rows = 10
        self.num_columns = self.manager.numMar // self.num_rows
        self.marble_width = 70
        self.marble_height = 56
        self.mmx = 75
        self.mmy = 65

    def draw_marble(self, numMar):
        print(numMar)
        for i in range((numMar // self.num_rows) + 1): 
            if i != (numMar // self.num_rows):
                for j in range(self.num_rows):
                    screen.blit(marble, (((width / 2) + (j * self.mmx) - ((self.mmx * self.num_rows) / 2)), ((height / 2) + (i * self.mmy) - ((self.mmy * self.num_columns) / 2)), self.marble_width, self.marble_height))
            else:
                for j in range(numMar % self.num_rows):
                    screen.blit(marble, (((width / 2) + (j * self.mmx) - ((self.mmx * self.num_rows) / 2), ((height / 2) + (i * self.mmy) - ((self.mmy * self.num_columns) / 2)), self.marble_width, self.marble_height)))
                    
class Main:
    def __init__(self):
        self.marble = Marble()
        self.manager = Manager()
        self.table = pygame.image.load(os.path.join(CURRENT_PATH + 'res/table.jfif')).convert_alpha()
        self.key_pressed = 0

    def draw_elements(self):
        self.draw_table()
        self.marble.draw_marble(self.manager.numMar)
        self.draw_player()
        self.draw_computer()
        self.computer_move()
        self.player_move()

    def draw_table(self):
        table_rect = pygame.Rect(0, 0, 1280, 853)
        screen.blit(self.table, table_rect)

    def draw_computer(self):
        title_text, number_marbles_text = "Computer", str(self.manager.computer_score)

        title_surface = play_font.render(title_text, True, (56, 74, 12))
        number_marbles_surface = play_font.render(number_marbles_text, True, (56, 74, 12))

        title_rect = title_surface.get_rect(center = ((1280 / 1.125, 300)))
        number_marbles_rect = number_marbles_surface.get_rect(center = ((1280 / 1.125, 350)))

        screen.blit(title_surface, title_rect)
        screen.blit(number_marbles_surface, number_marbles_rect)

    def draw_player(self):
        title_text, number_marbles_text = "Player", str(self.manager.player_score)

        title_surface = play_font.render(title_text, True, (56, 74, 12))
        number_marbles_surface = play_font.render(number_marbles_text, True, (56, 74, 12))

        title_rect = title_surface.get_rect(center = ((1280 / 10, 300)))
        number_marbles_rect = number_marbles_surface.get_rect(center = ((1280 / 10, 350)))

        screen.blit(title_surface, title_rect)
        screen.blit(number_marbles_surface, number_marbles_rect)

    def computer_move(self):
        if self.manager.player_turn == 1:
            # Computer Logic
            self.manager.numMar -= int(random.randint(1, 10))
            self.manager.computer_score += self.manager.number_marbles_text
            self.manager.number_marbles_text = 0
            self.manager.player_turn = 0

    def player_move(self):
        if self.manager.player_turn == 0:
            title_surface = play_font.render(self.manager.title_text, True, (56, 74, 12))
            number_marbles_surface = play_font.render(str(self.manager.number_marbles_text), True, (56, 74, 12))

            title_rect = title_surface.get_rect(center = ((1280 / 2, 75)))
            number_marbles_rect = number_marbles_surface.get_rect(center = (((1280 / 2) + 400, 75)))

            screen.blit(title_surface, title_rect)
            screen.blit(number_marbles_surface, number_marbles_rect)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN: 
                    if pygame.key.name(event.key) in "123456789":
                        self.manager.number_marbles_text = (self.manager.number_marbles_text  * 10) + int(pygame.key.name(event.key))
                if event.type == pygame.KEYDOWN and pygame.key.name(event.key) == "return":
                    self.manager.numMar -= self.manager.number_marbles_text
                    self.manager.player_score += self.manager.number_marbles_text
                    self.manager.player_turn = 1

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
            exit()

    if manager.game_state == "Menu": menu.draw_elements()
    elif manager.game_state == "Game": main_game.draw_elements()
    elif manager.game_state == "GameOver": game_over.draw_elements() 

    pygame.display.update()
    clock.tick(framerate)