import random as r
import pygame


#fin a away to detect scuares around it
#make art
#make text appear for lose screen and numbered squares





pygame.init()
pygame.display.set_caption("Mines-weeper")
pygame.font.init()

flags = (pygame.RESIZABLE)
HEIGHT = 400
WIDTH = 840
screen = pygame.display.set_mode((WIDTH, HEIGHT), flags)
screen.fill((255, 255, 0))
mouse_location = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()[0]
size = 20



class Buttons:
    def __init__(self, color, xpos, ypos, size,):
        self.color = color
        self.xpos = xpos
        self.ypos = ypos
        self.size = size

    def mine(self, screen):
        mine = pygame.draw.rect(
            screen, self.color, (self.xpos, self.ypos, self.size, self.size))
        return mine
'''
def numbered_square(color, screen, xpos, ypos, size):
    numbered_square_text = pygame.font.SysFont("infree", 12, True)
    numbered_square = pygame.draw.rect(
        screen, color, (xpos, ypos, size, size))
    numbered_square_text.render("0", False, (0, 0, 0))
    rect = numbered_square_text.get_rect(center=numbered_square.center)
    screen.blit(numbered_square_text, rect)
numbered_square((90, 255, 255), screen, 100, 100, size)
'''


        
        

    

#check for mines next to it:
#cell looks left & right for a intiger one in list
#cell looks at list above and directvly below
#cell looks left and right from previous positions

coords = []
pos = []
grid_list_size = HEIGHT//size
a_row_size = WIDTH//size
amount_of_mines = 300

def list_grid(a_row_size = a_row_size , grid_list_size = grid_list_size):
    for this in range(grid_list_size):
        a_row = []
        for this in range(a_row_size):
            a_row.append(0)
        coords.append(a_row)
    return coords


def randomizer():
    pos_list = []
    while len(pos_list) != amount_of_mines:
        coordinates = []
        grid_pos = r.randint(0, grid_list_size - 1)
        row_pos = r.randint(0, a_row_size - 1)
        coordinates.append(grid_pos)
        coordinates.append(row_pos)
        pos_list.append(coordinates)
        for list_of_coords in pos_list:
            if pos_list.count(list_of_coords) > 1:
                pos_list.remove(list_of_coords)
    return pos_list


def setting_value():
    pos = randomizer()
    grid = list_grid()
    for place in pos:
        grid[place[0]][place[1]] = "m"
    return grid
buttons = []

def game_grid(size, xpos = 0, ypos = 0):
    grid = setting_value()
    row = 0
    cell = 0
    for this in range(HEIGHT//size):
        for square in range(WIDTH // size):
            if grid[row][cell] == "m":
                color = (50, 50, 50)
                Buttons(color, xpos, ypos, size).mine(screen)
                buttons.append(Buttons(color, xpos, ypos, size).mine(screen))
            elif grid[row][cell] == 0:
                color = (50, 50, 50)
                pygame.draw.rect(
                screen, color, (xpos, ypos, size, size)
                )
            cell += 1
            xpos += size
        row += 1
        cell -= WIDTH//size
        ypos += size
        for square in range(WIDTH // size):
            xpos -= size
        
        
    return color

def game():

    game_grid(size)
    
              
    run = True
    while run:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            
            
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                for button in buttons:
                    if button.collidepoint(event.pos):
                        print("you lose!!!")
                        for button in buttons:
                            Buttons((250, 90, 90), button[0], button[1], button[2]).mine(screen)


        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    game()
