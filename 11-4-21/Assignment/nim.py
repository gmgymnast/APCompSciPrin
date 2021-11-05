import pygame, sys, random, os, math

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
        self.player_turn = 2  # 0 = player, 1 = computer
        self.player_score = 0
        self.computer_score = 0
        self.mode = random.randint(0, 1)
        self.computer_mode = "smart"
        self.lose = "None"
        # "dumb" if self.mode == 0 else "smart"
        self.title_text, self.number_marbles_text = "Enter the Number of Marbles you Want to Take: ", 0

class Marble:
    def __init__(self):
        self.manager = Manager()
        self.num_rows = 10
        self.num_columns = 10
        self.marble_width = 70
        self.marble_height = 56
        self.mmx = 75
        self.mmy = 65

    def draw_marble(self, numMar):
        title_text = "Marbles Left: " + str(numMar)
        title_surface = play_font.render(title_text, True, (56, 74, 12))
        title_rect = title_surface.get_rect(center = ((1280 / 2, 125)))
        screen.blit(title_surface, title_rect)

        for i in range((numMar // self.num_rows) + 1): 
            if i != (numMar // self.num_rows):
                for j in range(self.num_rows):
                    screen.blit(marble, (((width / 2) + (j * self.mmx) - ((self.mmx * self.num_rows) / 2)), ((height / 1.8) + (i * self.mmy) - ((self.mmy * self.num_columns) / 2)), self.marble_width, self.marble_height))
            else:
                for j in range(numMar % self.num_rows):
                    screen.blit(marble, (((width / 2) + (j * self.mmx) - ((self.mmx * self.num_rows) / 2)), ((height / 1.8) + (i * self.mmy) - ((self.mmy * self.num_columns) / 2)), self.marble_width, self.marble_height))
                    
class Main:
    def __init__(self):
        self.marble = Marble()
        self.manager = Manager()
        self.table = pygame.image.load(os.path.join(CURRENT_PATH + 'res/table.jfif')).convert_alpha()
        self.key_pressed = 0
        self.marbles_taken_by_computer = 0

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
        marble_small = pygame.image.load(os.path.join(CURRENT_PATH + 'res/marble_small.png')).convert_alpha()
        marbles_small_rect = pygame.Rect((1280 / 1.125) - 60, 330, 46, 37)
        screen.blit(marble_small, marbles_small_rect)

        title_text, number_marbles_text = "Computer", str(self.manager.computer_score)

        title_surface = play_font.render(title_text, True, (56, 74, 12))
        number_marbles_surface = play_font.render(number_marbles_text, True, (56, 74, 12))

        title_rect = title_surface.get_rect(center = ((1280 / 1.125, 300)))
        number_marbles_rect = number_marbles_surface.get_rect(center = ((1280 / 1.125, 350)))

        screen.blit(title_surface, title_rect)
        screen.blit(number_marbles_surface, number_marbles_rect)

    def draw_player(self):
        marble_small = pygame.image.load(os.path.join(CURRENT_PATH + 'res/marble_small.png')).convert_alpha()
        marbles_small_rect = pygame.Rect((1280 / 10) - 60, 330, 46, 37)
        screen.blit(marble_small, marbles_small_rect)

        title_text, number_marbles_text, number_marbles_taken_by_computer_text = "Player", str(self.manager.player_score), "The Computer Just Took " + str(self.marbles_taken_by_computer) + " Marbles"

        title_surface = play_font.render(title_text, True, (56, 74, 12))
        number_marbles_surface = play_font.render(number_marbles_text, True, (56, 74, 12))
        number_marbles_taken_by_computer_surface = play_font.render(number_marbles_taken_by_computer_text, True, (56, 74, 12))

        title_rect = title_surface.get_rect(center = ((1280 / 10, 300)))
        number_marbles_rect = number_marbles_surface.get_rect(center = ((1280 / 10, 350)))
        number_marbles_taken_by_computer_rect = number_marbles_taken_by_computer_surface.get_rect(center = ((1280 / 2, 830)))

        screen.blit(title_surface, title_rect)
        screen.blit(number_marbles_surface, number_marbles_rect)
        screen.blit(number_marbles_taken_by_computer_surface, number_marbles_taken_by_computer_rect)

    def computer_move(self):
        if self.manager.player_turn == 1:
            if self.manager.computer_mode == "dumb": marbles_taken = random.randint(1, self.manager.numMar / 2)
            elif self.manager.computer_mode == "smart":
                if self.manager.numMar < 2:  self.lose()
                else: marbles_taken = self.manager.numMar - (2 ** int(math.log(self.manager.numMar, 2)) - 1)
            self.manager.numMar -= marbles_taken
            self.manager.computer_score += marbles_taken
            self.marbles_taken_by_computer = marbles_taken
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
                    if self.manager.number_marbles_text != 0:
                        if self.manager.number_marbles_text == 1: self.lose()
                        if self.manager.number_marbles_text >= self.manager.numMar / 2: self.manager.number_marbles_text = 0
                        else:
                            self.manager.numMar -= self.manager.number_marbles_text
                            self.manager.player_score += self.manager.number_marbles_text
                            if self.manager.numMar == 0: self.lose()
                            else: self.manager.player_turn = 1

    def lose(self):
        self.manager.player_turn = 2
        self.manager.game_state = "Menu"
        print(self.manager.game_state)

class Menu:
    def __init__(self): 
        self.main = Main()
        self.manager = Manager()

    def draw_elements(self):
        self.main.draw_table()
        self.draw_menu()

    def draw_menu(self):
        if self.manager.lose == "Player": title_text = "You Lose!"
        elif self.manager.lose == "Computer": title_text = "You Win!"
        elif self.manager.lose == "None": title_text = "Nim"
        else: title_text = "Nim!"
        
        regular_mode_text = "Press 1 To Play"

        title_surface = menu_main_font.render(title_text, True, (56, 74, 12))
        regular_mode_surface = play_font.render(regular_mode_text, True, (56, 74, 12))  

        title_rect = title_surface.get_rect(center = ((1280 / 2, 300)))
        regular_mode_rect = regular_mode_surface.get_rect(center = ((1280 / 2, 500)))

        screen.blit(title_surface, title_rect)
        screen.blit(regular_mode_surface, regular_mode_rect)

class StateChange():
    def __init__(self):
        self.manager = Manager()
        self.menu = Menu()
        self.main = Main()

    def change_state(self):
        if self.manager.player_turn == 2: self.menu.draw_elements()
        if self.manager.game_state == "Game": self.main.draw_elements()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if self.manager.game_state == "Menu":
                    if event.key == pygame.K_1:
                        self.manager.game_state = "Game"           
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit() 
                exit()

manager, state = Manager(), StateChange()

while True:
    state.event_handler()
    state.change_state()

    pygame.display.update()
    clock.tick(framerate)
    