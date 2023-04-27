import pygame, sys
from button import Button
import os
from rowdy import Rowdy
from wall import Wall
from food import Food
from block import Block
from processBlocks import ProcessBlocks

img = pygame.image.load(os.path.join('Assets', 'MiniRowdy_40.png'))
left_arrow = pygame.image.load(os.path.join('Assets', 'left_arrow.png'))
right_arrow = pygame.image.load(os.path.join('Assets', 'right_arrow.png'))
currentColor = pygame.image.load(os.path.join('Assets', 'CurrentColor.png'))
light_green = pygame.image.load(os.path.join('Assets', 'move_arrow.png'))
light_blue = pygame.image.load(os.path.join('Assets', 'turnRight2.png'))
plum = pygame.image.load(os.path.join('Assets', 'turnLeft2.png'))
blank = pygame.image.load(os.path.join('Assets', 'blank.png'))
wall_img = pygame.image.load(os.path.join('Assets', 'Wall.png'))

steve = pygame.image.load(os.path.join('Assets', 'StevePlayer.png'))
dora = pygame.image.load(os.path.join('Assets', 'DoraPlayer.png'))
tweety = pygame.image.load(os.path.join('Assets', 'TweetyPlayer.png'))

PLAYER_IMAGE = img
SELECTION = 4


def allFoodEaten(Foods):
    for food in Foods:
        if not food.isEaten:
            return False
    return True

pygame.init()

SCREEN = pygame.display.set_mode((900, 500))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/MainScreenEmptyButtons.png")
HELP_SCREEN = pygame.image.load("assets/help_screen.png")
LEVELS_BG = pygame.image.load("assets/LevelsBGEmptyButtons.png")
PLAY_BG_2 = pygame.image.load("assets/PlayBG_2.png")
SETTINGS_BG = pygame.image.load("assets/SettingsBG.png")

SELECTED_ARROW = pygame.image.load("assets/SelectedArrow.png")
SELECTED_COLOR = pygame.image.load("assets/SelectedColor.png")
DORA_SELECTED = pygame.image.load("assets/Dora.png")
STEVE_SELECTED = pygame.image.load("assets/Steve.png")
TWEETY_SELECTED = pygame.image.load("assets/Tweety.png")
ROWDY_SELECTED = pygame.image.load("assets/RowdySelected.png")

HIGHLIGHT = pygame.image.load("assets/Highlight_40%.png")


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def get_Roboto(size):
    return pygame.font.Font("assets/Roboto-Thin.ttf", size)

def play():

    rowdy_class_coords = [195, 55]
    rowdy_class = Rowdy(rowdy_class_coords)
    rowdy_class._image = PLAYER_IMAGE

    top_border = Wall([0,0], size = (900,50), img=blank)
    left_border = Wall([0,0], size = (150,500), img=blank)
    right_border = Wall([713,0], size = (750,500), img=blank)
    bottom_border_top = Wall([0,350], size = (900,50), img=blank)
    bottom_border_bottom = Wall([0,340], size = (900,50), img=blank)
    side_bar_left = Wall([150,400], size = (100,100), img=blank)
    side_bar_right = Wall([650,400], size = (100,100), img=blank)
    #test = Wall([427,227])
    walls = [top_border, left_border, right_border, bottom_border_top, bottom_border_bottom, side_bar_left, side_bar_right]

    food1 = Food([255, 55])
    food2 = Food([314, 114])
    food3 = Food([666, 55])
    Foods = [food1, food2, food3]

    blocks = []
    block_color = "light green"
    block_image = light_green

    process_blocks = False
    block_index = 0
    block_string = ""

    color_pallet = []

    solve_maze = False


    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("sky blue")

        SCREEN.blit(PLAY_BG_2, (0,0))

        for wall in walls:
            SCREEN.blit(wall._image,wall._coords)

        for block in blocks:
            #pygame.draw.rect(SCREEN, block.color, block)
            SCREEN.blit(block.img, block.coords)

        for food in Foods:
            SCREEN.blit(food._image, food._coords)
            

        # Color pallet
        #pygame.draw.rect(SCREEN, 'light green', pygame.Rect(805, 105, 40, 40))
        SCREEN.blit(light_green, (765,63))
        #pygame.draw.rect(SCREEN, 'light blue', pygame.Rect(805, 155, 40, 40))
        SCREEN.blit(light_blue, (765,160))
        #pygame.draw.rect(SCREEN, 'plum', pygame.Rect(805, 205, 40, 40))
        SCREEN.blit(plum, (765,253))
        #pygame.draw.rect(SCREEN, 'orange', pygame.Rect(805, 255, 40, 40))

        SCREEN.blit(rowdy_class._image, rowdy_class._coords)
        #CREEN.blit(left_arrow, (405,455))
        #SCREEN.blit(right_arrow, (455,455))
        #SCREEN.blit(currentColor, (250,355))
        #SCREEN.blit(startButton, (130,405))

        # Block color: 
        #pygame.draw.rect(SCREEN, block_color, pygame.Rect(455, 355, 40, 40))
        SCREEN.blit(block_image, (600,420))

        #SCREEN.blit(screen, (0,0))

        PLAY_BACK = Button(image=None, pos=(50, 38), 
                            text_input="BACK", font=get_font(15), base_color="Black", hovering_color="Green")
        
        HELP = Button(image=None, pos=(26, 479), 
                            text_input="?", font=get_font(30), base_color="Black", hovering_color="Green")

        RUN = Button(image=None, pos=(450, 461), 
                            text_input="RUN▶", font=get_font(30), base_color="White", hovering_color="Green")
        
        for button in [PLAY_BACK, HELP, RUN]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if HELP.checkForInput(PLAY_MOUSE_POS):
                    help()
                #Check if start button is pressed
                if RUN.checkForInput(PLAY_MOUSE_POS):
                    print("start")
                    process_block_class = ProcessBlocks(blocks)
                    block_index = 0
                    process_blocks = True
                    block_string = process_block_class.getInstructionString()
                if mouse_presses[0]:
                    cur = pygame.mouse.get_pos()
                    copy_cur = (cur[0],cur[1])
                    yeet = [((cur[0]//50)*50)+5,((cur[1]//50)*50)+5]
                    is_block = False
                    # Check if there is already a block placed if so remove it
                    for block in blocks:
                        if block.colliderect(pygame.Rect(cur, (70, 70))):
                            blocks.remove(block)
                            is_block = True

                    # Check if click color pallet
                    if pygame.Rect(yeet, (40, 40)).colliderect(pygame.Rect(764, 62, 70, 70)):
                        print("green color")
                        block_color = "light green"
                        block_image = light_green
                    if pygame.Rect(yeet, (40, 40)).colliderect(pygame.Rect(766, 161, 70, 70)):
                        print("blue color")
                        block_color = "light blue"
                        block_image = light_blue
                    if pygame.Rect(yeet, (40, 40)).colliderect(pygame.Rect(765, 253, 70, 70)):
                        print("plum color")
                        block_color = "plum"
                        block_image = plum

                    # Check if Block is placed within white bar
                    #if not is_block and yeet[1] > 400 and yeet[1] < 450 and yeet[0] > 250: 
                    if not is_block and yeet[1] > 300 and yeet[1] < 410 and yeet[0] > 150: 
                        block_x = 0 
                        if copy_cur[0] > 185:
                            base = copy_cur[0] - 185
                            how_many_Forward = base//80
                            block_x = 185 + (how_many_Forward*80)
                            print(f"Base: {base}, Forward: {how_many_Forward}, Block_x: {block_x}")
                        block_cords = (block_x, 343)
                        temp_block = Block(coords=block_cords, color=block_color, left=yeet[0],top=yeet[1], width=70, height=70)
                        blocks.append(temp_block)

                    '''
                    # If left arrow clicked shift blocks to the left
                    if pygame.Rect(yeet, (40, 40)).colliderect(pygame.Rect(405, 455, 25, 40)):
                        for block in blocks:
                            block.move_ip(-50,0)
                            block.coords[0] -= 50
                            print(block)

                    # If right arrow clicked shift blocks to the right
                    if pygame.Rect(yeet, (40, 40)).colliderect(pygame.Rect(455, 455, 25, 40)):
                        for block in blocks:
                            block.move_ip(50,0)
                            block.coords[0] += 50
                            print(block)
                    '''
   
                    print(cur, yeet)
                    print(block_string)
                    #wall_Coords_list.append(rounded_cords)
                    #walls.append(pygame.Rect(rounded_cords, (50,50)))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    cur = pygame.mouse.get_pos()
                    x = 192 + (int((cur[0] - 195)/58.75)*58.75)
                    y = 51 + (int((cur[1] - 55)/58.75)*58.75)
                    rounded_cords = [x,y]
                    print(rounded_cords)
                    is_wall = False
                    for wall in walls:
                        if wall.hitbox.colliderect(pygame.Rect(rounded_cords, (50, 50))):
                            walls.remove(wall)
                            is_wall = True
                    if not is_wall:
                        walls.append(Wall(rounded_cords))
                    print(f"Number of walls: {len(walls)}. Wall placed at {rounded_cords}")

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    cur = pygame.mouse.get_pos()
                    x = 196 + (int((cur[0] - 195)/58.75)*58.75)
                    y = 56 + (int((cur[1] - 55)/58.75)*58.75)
                    rounded_cords = (x,y)
                    print(rounded_cords)
                    is_food = False
                    for food in Foods:
                        if food.hitbox.colliderect(pygame.Rect(rounded_cords, (50, 50))):
                            Foods.remove(food)
                            is_food = True
                    if not is_food:
                        temp_food = Food(rounded_cords)
                        Foods.append(temp_food)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    rowdy_class.foodCollide(Foods)
                    if rowdy_class.wallCollide(walls):
                        rowdy_class.move()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    rowdy_class.turn_right()
                    # print(rowdy_class._facing)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    rowdy_class.turn_left()
                    # print(rowdy_class._facing)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    print("start")
                    block_index = 0
                    process_block_class = ProcessBlocks(blocks)
                    process_blocks = True
                    block_string = process_block_class.getInstructionString()
                    print(cur, yeet, block_string)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    if rowdy_class.wallOnRight(walls):
                        print("wall on right")
                    else:
                        print("no wall")

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    solve_maze = not solve_maze
        if process_blocks:
            if block_index != 0:
                #pygame.draw.rect(SCREEN, "black", pygame.Rect((255 + (block_index-1)*50), 450, 40, 10)) 
                SCREEN.blit(HIGHLIGHT, ((185 + (block_index-1)*80),344))
            if block_index >= len(blocks):
                process_blocks = False
            elif block_string[block_index] == "m":
                rowdy_class.foodCollide(Foods)
                if rowdy_class.wallCollide(walls):
                    rowdy_class.move()
            elif block_string[block_index] == "r":
                rowdy_class.turn_right()
            elif block_string[block_index] == "l":
                rowdy_class.turn_left()
            block_index += 1   
            pygame.time.delay(750)
            

        
        if solve_maze and not allFoodEaten(Foods):   
            # Maze solving code
            if rowdy_class.wallOnRight(walls):
                if rowdy_class.wallCollide(walls):
                    rowdy_class.foodCollide(Foods)
                    rowdy_class.move()
                else:
                    rowdy_class.turn_left()
            else:
                rowdy_class.turn_right()
                rowdy_class.foodCollide(Foods)
                rowdy_class.move()
            pygame.time.delay(100)
        
        pygame.display.update()

    
def options():
    while True:
        SCREEN.blit(LEVELS_BG, (0, 0))
        
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        OPTIONS_BACK = Button(image=None, pos=(30, 26), 
                            text_input="BACK", font=get_font(10), base_color="Black", hovering_color="Green")
        LEVELONE_BUTTON = Button(image=pygame.image.load("assets/LevelButtonBase.png"), pos=(450, 190), 
                            text_input="Level 1", font=get_font(15), base_color="black", hovering_color="White")
        LEVELTWO_BUTTON = Button(image=pygame.image.load("assets/LevelButtonBase.png"), pos=(450, 248), 
                            text_input="Level 2", font=get_font(15), base_color="black", hovering_color="White")
        LEVELTHREE_BUTTON = Button(image=pygame.image.load("assets/LevelButtonBase.png"), pos=(450, 305), 
                            text_input="Level 3", font=get_font(15), base_color="black", hovering_color="White")

        for button in [OPTIONS_BACK, LEVELONE_BUTTON, LEVELTWO_BUTTON, LEVELTHREE_BUTTON]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if LEVELONE_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    play()

        pygame.display.update()

def help():
    while True:
        SCREEN.blit(HELP_SCREEN, (0, 0))

        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        HELP_BACK = Button(image=None, pos=(30, 26), 
                            text_input="BACK", font=get_font(10), base_color="Black", hovering_color="Green")

        for button in [HELP_BACK]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if HELP_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    play()

        pygame.display.update()

def settings():
    global SELECTION
    global PLAYER_IMAGE 
    while True:
        SCREEN.blit(SETTINGS_BG, (0, 0))
        SCREEN.blit(TWEETY_SELECTED, (465, 140))
        SCREEN.blit(ROWDY_SELECTED, (575, 146))


        if SELECTION == 1:
            #SCREEN.blit(SELECTED_ARROW, (285, 225))
            SCREEN.blit(SELECTED_COLOR, (278, 145))
            SCREEN.blit(DORA_SELECTED, (283, 144))
            PLAYER_IMAGE = dora
        
        if SELECTION == 2:
            #SCREEN.blit(SELECTED_ARROW, (375, 225))
            SCREEN.blit(SELECTED_COLOR, (370, 145))
            SCREEN.blit(STEVE_SELECTED, (378, 139))
            PLAYER_IMAGE = steve
        
        if SELECTION == 3:
            SCREEN.blit(SELECTED_COLOR, (463, 145))
            SCREEN.blit(TWEETY_SELECTED, (465, 140))
            PLAYER_IMAGE = tweety

        if SELECTION == 4:
            SCREEN.blit(SELECTED_COLOR, (568, 145))
            SCREEN.blit(ROWDY_SELECTED, (575, 146))
            PLAYER_IMAGE = img
        
        
        

        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        HELP_BACK = Button(image=None, pos=(30, 26), 
                            text_input="BACK", font=get_font(10), base_color="Black", hovering_color="Green")
        
        DORA = Button(image=None, pos=(302, 185),
                            text_input="   ", font=get_Roboto(70), base_color="Black", hovering_color="White", hovering_image=HIGHLIGHT)
        
        STEVE = Button(image=None, pos=(396, 190),
                            text_input="   ", font=get_Roboto(80), base_color="Black", hovering_color="White", hovering_image=HIGHLIGHT)
        
        TWEETY = Button(image=None, pos=(490, 190),
                            text_input="   ", font=get_Roboto(80), base_color="Black", hovering_color="White", hovering_image=HIGHLIGHT)
        
        ROWDY = Button(image=None, pos=(595, 190),
                            text_input="   ", font=get_Roboto(80), base_color="Black", hovering_color="White", hovering_image=HIGHLIGHT)
        
        

        for button in [HELP_BACK, DORA, STEVE, TWEETY, ROWDY]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                if HELP_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if DORA.checkForInput(OPTIONS_MOUSE_POS):
                    print("Dora")
                    SELECTION = 1
                if STEVE.checkForInput(OPTIONS_MOUSE_POS):
                    print("Steve")
                    SELECTION = 2
                if TWEETY.checkForInput(OPTIONS_MOUSE_POS):
                    print("Tweety")
                    SELECTION = 3
                if ROWDY.checkForInput(OPTIONS_MOUSE_POS):
                    print("Rowdy")
                    SELECTION = 4
                
                

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=pygame.image.load("assets/ButtonBase.png"), pos=(450, 285), 
                            text_input="Start", font=get_font(20), base_color="black", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/ButtonBase.png"), pos=(450, 350), 
                            text_input="Levels", font=get_font(20), base_color="black", hovering_color="White")
        SETTINGS_BUTTON = Button(image=pygame.image.load("assets/ButtonBase.png"), pos=(450, 415), 
                            text_input="Settings", font=get_font(20), base_color="black", hovering_color="White")

        #SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, SETTINGS_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if SETTINGS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    settings()

        pygame.display.update()

main_menu()