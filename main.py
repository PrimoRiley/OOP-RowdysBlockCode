import pygame, sys
from button import Button
import os
from rowdy import Rowdy
from food import Food
from block import Block
from processBlocks import ProcessBlocks

img = pygame.image.load(os.path.join('Assets', 'MiniRowdy.png'))
left_arrow = pygame.image.load(os.path.join('Assets', 'left_arrow.png'))
right_arrow = pygame.image.load(os.path.join('Assets', 'right_arrow.png'))
currentColor = pygame.image.load(os.path.join('Assets', 'CurrentColor.png'))
startButton = pygame.image.load(os.path.join('Assets', 'StartButton.png'))
light_green = pygame.image.load(os.path.join('Assets', 'block_arrow.png'))
light_blue = pygame.image.load(os.path.join('Assets', 'turnRight.png'))
plum = pygame.image.load(os.path.join('Assets', 'turnLeft.png'))

def drawgrid(w, rows, surface):
    """TESTING

    Args:
        w (_type_): _description_
        rows (_type_): _description_
        surface (_type_): _description_
    """    
    sizebtwn = w // rows
    for i in range(0, w, sizebtwn):
        x, y = i, i
        pygame.draw.line(surface, ('white'), (x, 0), (x, w))
        pygame.draw.line(surface, ('white'), (0, y), (w, y))

def allFoodEaten(Foods):
    for food in Foods:
        if not food.isEaten:
            return False
    return True

pygame.init()

SCREEN = pygame.display.set_mode((900, 500))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/MainScreenEmptyButtons.png")
LEVELS_BG = pygame.image.load("assets/LevelsBGEmptyButtons.png")
PLAY_BG = pygame.image.load("assets/PlayBG.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():

    rowdy_class_coords = [150, 50]
    rowdy_class = Rowdy(rowdy_class_coords)

    top_border = pygame.Rect((0, 0), (900, 50))
    left_border = pygame.Rect((0, 0), (150, 500))
    right_border = pygame.Rect((750, 0), (750, 500))
    bottom_border_top = pygame.Rect((0, 350), (900, 50))
    bottom_border_bottom = pygame.Rect((0, 450), (900, 50))
    side_bar_left = pygame.Rect((150, 400), (100, 100))
    side_bar_right = pygame.Rect((650, 400), (100, 100))
    walls = [top_border, left_border, right_border, bottom_border_top, bottom_border_bottom, side_bar_left, side_bar_right]

    food1 = Food([550, 200])
    food2 = Food([300, 150])
    food3 = Food([650, 300])
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

        drawgrid(SCREEN.get_width(), 18, SCREEN)

        

        for food in Foods:
            SCREEN.blit(food._image, food._coords)
        
        # White code bar
        pygame.draw.rect(SCREEN, 'white', pygame.Rect(250, 400, 400, 50))

        for block in blocks:
            pygame.draw.rect(SCREEN, block.color, block)
            SCREEN.blit(block.img, block.coords)

        for wall in walls:
            pygame.draw.rect(SCREEN, 'gray', wall)

        SCREEN.blit(PLAY_BG, (0,0))
            

        # Color pallet
        pygame.draw.rect(SCREEN, 'light green', pygame.Rect(805, 105, 40, 40))
        SCREEN.blit(light_green, (805,105))
        pygame.draw.rect(SCREEN, 'light blue', pygame.Rect(805, 155, 40, 40))
        SCREEN.blit(light_blue, (805,155))
        pygame.draw.rect(SCREEN, 'plum', pygame.Rect(805, 205, 40, 40))
        SCREEN.blit(plum, (805,205))
        pygame.draw.rect(SCREEN, 'orange', pygame.Rect(805, 255, 40, 40))

        SCREEN.blit(rowdy_class._image, rowdy_class._coords)
        SCREEN.blit(left_arrow, (405,455))
        SCREEN.blit(right_arrow, (455,455))
        SCREEN.blit(currentColor, (250,355))
        SCREEN.blit(startButton, (130,405))

        # Block color: 
        pygame.draw.rect(SCREEN, block_color, pygame.Rect(455, 355, 40, 40))
        SCREEN.blit(block_image, (455,355))

        #SCREEN.blit(screen, (0,0))

        PLAY_BACK = Button(image=None, pos=(30, 26), 
                            text_input="BACK", font=get_font(10), base_color="Black", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if mouse_presses[0]:
                    cur = pygame.mouse.get_pos()
                    copy_cur = (cur[0],cur[1])
                    yeet = [((cur[0]//50)*50)+5,((cur[1]//50)*50)+5]
                    is_block = False
                    # Check if there is already a block placed if so remove it
                    for block in blocks:
                        if block.colliderect(pygame.Rect(yeet, (40, 40))):
                            blocks.remove(block)
                            is_block = True

                    # Check if click color pallet
                    if pygame.Rect(yeet, (40, 40)).colliderect(pygame.Rect(805, 105, 40, 40)):
                        print("green color")
                        block_color = "light green"
                        block_image = light_green
                    if pygame.Rect(yeet, (40, 40)).colliderect(pygame.Rect(805, 155, 40, 40)):
                        print("blue color")
                        block_color = "light blue"
                        block_image = light_blue
                    if pygame.Rect(yeet, (40, 40)).colliderect(pygame.Rect(805, 205, 40, 40)):
                        print("plum color")
                        block_color = "plum"
                        block_image = plum

                    # Check if Block is placed within white bar
                    if not is_block and yeet[1] > 400 and yeet[1] < 450 and yeet[0] > 250: 
                        temp_block = Block(coords=yeet, color=block_color, left=yeet[0],top=yeet[1], width=40, height=40)
                        blocks.append(temp_block)

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

                    # Check if start button is clicked
                    if pygame.Rect(copy_cur, (1, 1)).colliderect(pygame.Rect(105, 405, 130, 40)):
                        print("start")
                        process_block_class = ProcessBlocks(blocks)
                        block_index = 0
                        process_blocks = True
                        block_string = process_block_class.getInstructionString()
                        
                    print(cur, yeet)
                    print(block_string)
                    #wall_Coords_list.append(rounded_cords)
                    #walls.append(pygame.Rect(rounded_cords, (50,50)))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    cur = pygame.mouse.get_pos()
                    rounded_cords = ((cur[0]//50)*50,(cur[1]//50)*50)
                    if pygame.Rect(rounded_cords, (50,50)) in walls:
                        print("already a wall there")
                        walls.remove(pygame.Rect(rounded_cords, (50,50)))
                    else:
                        walls.append(pygame.Rect(rounded_cords, (50,50)))
                    print(f"Number of walls: {len(walls)}. Wall placed at {rounded_cords}")

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    cur = pygame.mouse.get_pos()
                    rounded_cords = ((cur[0]//50)*50,(cur[1]//50)*50)
                    print(rounded_cords)
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
                pygame.draw.rect(SCREEN, "black", pygame.Rect((255 + (block_index-1)*50), 450, 40, 10)) 
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

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=pygame.image.load("assets/ButtonBase.png"), pos=(450, 285), 
                            text_input="Start", font=get_font(20), base_color="black", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/ButtonBase.png"), pos=(450, 350), 
                            text_input="Levels", font=get_font(20), base_color="black", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/ButtonBase.png"), pos=(450, 415), 
                            text_input="Settings", font=get_font(20), base_color="black", hovering_color="White")

        #SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
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
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()