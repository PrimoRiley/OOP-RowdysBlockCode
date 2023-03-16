import pygame
import os
from rowdy import Rowdy
from food import Food

img = pygame.image.load(os.path.join('Assets', 'MiniRowdy.png'))
left_arrow = pygame.image.load(os.path.join('Assets', 'left_arrow.png'))
right_arrow = pygame.image.load(os.path.join('Assets', 'right_arrow.png'))
currentColor = pygame.image.load(os.path.join('Assets', 'CurrentColor.png'))
startButton = pygame.image.load(os.path.join('Assets', 'StartButton.png'))


#screen = pygame.image.load(os.path.join('Assets', 'GameDisplay.png'))

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

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

# TODO fix run blocks
def runBlocks(blocks,block_index,block_string,process_blocks):
    '''
    while not blocks[0][1].colliderect(pygame.Rect(205, 405, 30, 30)):
    for block in blocks:
    block[1].move_ip(50,0)
                    '''
    x, y = 200, 400
    test_rect = pygame.Rect((x, y), (25, 25))
    block_index = 0
    block_string = ""
    for i in range(len(blocks)):
        if test_rect.colliderect(blocks[i][1]) != -1:
            process_blocks = True
            if blocks[i][0] == "light green":
                #rowdy_class.foodCollide(Foods)
                #if rowdy_class.wallCollide(walls):
                    #rowdy_class.move()
                block_string += "m"
            elif blocks[i][0] == "light blue":
                #rowdy_class.turn_right()
                block_string += "r"
            elif blocks[i][0] == "plum":
                #rowdy_class.turn_left()
                block_string += "l"
        print("hit")
        x += 50
        test_rect = pygame.Rect((x, y), (25, 25))


rowdy_class_coords = [150, 50]
rowdy_class = Rowdy(rowdy_class_coords)

def main():

    run = True

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

    process_blocks = False
    block_index = 0
    block_string = ""

    color_pallet = []

    solve_maze = False

    '''
    wall_Coords_list = [(200, 50), (200, 100), (150, 200), (200, 200), (250, 200), (300, 200)]

    for wall in wall_Coords_list:
        walls.append(pygame.Rect(wall, (50,50)))
    '''

    while run:
        WIN.fill("sky blue")

        drawgrid(WIN.get_width(), 18, WIN)

        for food in Foods:
            WIN.blit(food._image, food._coords)


        pygame.draw.rect(WIN, 'white', pygame.Rect(250, 400, 400, 50))

        for block in blocks:
            pygame.draw.rect(WIN, block[0], block[1])

        for wall in walls:
            pygame.draw.rect(WIN, 'gray', wall)

        pygame.draw.rect(WIN, 'light green', pygame.Rect(805, 105, 40, 40))
        pygame.draw.rect(WIN, 'light blue', pygame.Rect(805, 155, 40, 40))
        pygame.draw.rect(WIN, 'plum', pygame.Rect(805, 205, 40, 40))
        pygame.draw.rect(WIN, 'orange', pygame.Rect(805, 255, 40, 40))

        WIN.blit(rowdy_class._image, rowdy_class._coords)
        WIN.blit(left_arrow, (405,455))
        WIN.blit(right_arrow, (455,455))
        WIN.blit(currentColor, (250,355))
        WIN.blit(startButton, (130,405))
        

        pygame.draw.rect(WIN, block_color, pygame.Rect(455, 355, 40, 40))
        #WIN.blit(screen, (0,0))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    cur = pygame.mouse.get_pos()
                    copy_cur = (cur[0],cur[1])
                    yeet = (((cur[0]//50)*50)+5,((cur[1]//50)*50)+5)
                    is_block = False
                    for block in blocks:
                        if pygame.Rect(yeet, (40, 40)) == block[1]:
                            blocks.remove(block)
                            is_block = True
                    if pygame.Rect(yeet, (40, 40)).colliderect(pygame.Rect(805, 105, 40, 40)):
                        print("green color")
                        block_color = "light green"
                    if pygame.Rect(yeet, (40, 40)).colliderect(pygame.Rect(805, 155, 40, 40)):
                        print("blue color")
                        block_color = "light blue"
                    if pygame.Rect(yeet, (40, 40)).colliderect(pygame.Rect(805, 205, 40, 40)):
                        print("plum color")
                        block_color = "plum"
                    if not is_block and yeet[1] > 400 and yeet[1] < 450 and yeet[0] > 250: 
                        blocks.append([block_color,pygame.Rect(yeet, (40, 40))])
                    if pygame.Rect(yeet, (40, 40)).colliderect(pygame.Rect(405, 455, 25, 40)):
                        for block in blocks:
                            block[1].move_ip(-50,0)
                            print(block)
                    if pygame.Rect(yeet, (40, 40)).colliderect(pygame.Rect(455, 455, 25, 40)):
                        for block in blocks:
                            block[1].move_ip(50,0)
                            print(block)

                    if pygame.Rect(copy_cur, (1, 1)).colliderect(pygame.Rect(105, 405, 130, 40)):
                        print("start")
                        '''
                        while not blocks[0][1].colliderect(pygame.Rect(205, 405, 30, 30)):
                            for block in blocks:
                                block[1].move_ip(50,0)
                        '''
                        x, y = 200, 400
                        test_rect = pygame.Rect((x, y), (25, 25))
                        block_index = 0
                        block_string = ""
                        for i in range(len(blocks)):
                            if test_rect.colliderect(blocks[i][1]) != -1:
                                process_blocks = True
                                if blocks[i][0] == "light green":
                                    #rowdy_class.foodCollide(Foods)
                                    #if rowdy_class.wallCollide(walls):
                                        #rowdy_class.move()
                                    block_string += "m"
                                elif blocks[i][0] == "light blue":
                                    #rowdy_class.turn_right()
                                    block_string += "r"
                                elif blocks[i][0] == "plum":
                                    #rowdy_class.turn_left()
                                    block_string += "l"
                                print("hit")
                            x += 50
                            test_rect = pygame.Rect((x, y), (25, 25))

                    print(cur, yeet)
                    #wall_Coords_list.append(rounded_cords)
                    #walls.append(pygame.Rect(rounded_cords, (50,50)))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    cur = pygame.mouse.get_pos()
                    rounded_cords = ((cur[0]//50)*50,(cur[1]//50)*50)
                    print(rounded_cords)
                    if pygame.Rect(rounded_cords, (50,50)) in walls:
                        print("already a wall there")
                        walls.remove(pygame.Rect(rounded_cords, (50,50)))
                    else:
                        walls.append(pygame.Rect(rounded_cords, (50,50)))
                    print(len(walls))

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
                    '''
                    while not blocks[0][1].colliderect(pygame.Rect(205, 405, 30, 30)):
                        for block in blocks:
                            block[1].move_ip(50,0)
                    '''
                    x, y = 200, 400
                    test_rect = pygame.Rect((x, y), (25, 25))
                    block_index = 0
                    block_string = ""
                    for i in range(len(blocks)):
                        if test_rect.colliderect(blocks[i][1]) != -1:
                            process_blocks = True
                            if blocks[i][0] == "light green":
                                #rowdy_class.foodCollide(Foods)
                                #if rowdy_class.wallCollide(walls):
                                    #rowdy_class.move()
                                block_string += "m"
                            elif blocks[i][0] == "light blue":
                                #rowdy_class.turn_right()
                                block_string += "r"
                            elif blocks[i][0] == "plum":
                                #rowdy_class.turn_left()
                                block_string += "l"
                            print("hit")
                        x += 50
                        test_rect = pygame.Rect((x, y), (25, 25))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    if rowdy_class.wallOnRight(walls):
                        print("wall on right")
                    else:
                        print("no wall")

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    if solve_maze:
                        solve_maze = False
                    else:
                        solve_maze = True
        

        if process_blocks:
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
            pygame.time.delay(300)

        
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
    #print(wall_Coords_list)
    pygame.quit()


if __name__ == "__main__":
    main()
