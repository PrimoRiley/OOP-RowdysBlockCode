import pygame
import os
from rowdy import Rowdy
from food import Food

img = pygame.image.load(os.path.join('Assets', 'MiniRowdy.png'))
screen = pygame.image.load(os.path.join('Assets', 'GameDisplay.png'))

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def drawgrid(w, rows, surface):
    sizebtwn = w // rows
    for i in range(0, w, sizebtwn):
        x, y = i, i
        pygame.draw.line(surface, ('white'), (x, 0), (x, w))
        pygame.draw.line(surface, ('white'), (0, y), (w, y))



'''
v1 = [245, 175]
v2 = [205, 155]
v3 = [205, 195]

v1_2 = [125, 145]
v2_2 = [105, 105]
v3_2 = [145, 105]

v1_3 = [655, 225]
v2_3 = [695, 205]
v3_3 = [695, 245]

rowdy = [v1, v2, v3]
rowdy2 = [v1_2, v2_2, v3_2]
rowdy3 = [v1_3, v2_3, v3_3]
'''

rowdy_class_coords = [150, 50]
rowdy_class = Rowdy(rowdy_class_coords)

def main():

    run = True
    object1 = pygame.Rect((20, 50), (50, 50))
    object2 = pygame.Rect((20, 50), (50, 50))
    circle_hitbox = pygame.Rect((300, 150), (50, 50))
    circle_color = (0, 255, 0)

    yeet = pygame.transform.rotate(img, 0)

    wall1 = pygame.Rect((550, 100), (50, 50))
    wall2 = pygame.Rect((500, 100), (50, 50))
    wall3 = pygame.Rect((550, 150), (50, 50))
    wall4 = pygame.Rect((550, 250), (50, 50))
    wall5 = pygame.Rect((550, 300), (50, 50))
    wall6 = pygame.Rect((600, 300), (50, 50))
    wall7 = pygame.Rect((700, 300), (50, 50))

    wall8 = pygame.Rect((0, 0), (900, 50))
    wall9 = pygame.Rect((0, 0), (150, 500))
    wall10 = pygame.Rect((750, 0), (750, 500))
    wall11 = pygame.Rect((0, 350), (900, 150))
    walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11]

    food1 = Food([550, 200])
    food2 = Food([300, 150])
    food3 = Food([650, 300])


    Foods = [food1, food2, food3]

    blocks = []


    while run:
        WIN.fill("sky blue")

        drawgrid(WIN.get_width(), 18, WIN)

        for wall in walls:
            pygame.draw.rect(WIN, 'gray', wall)

        for food in Foods:
            WIN.blit(food._image, food._coords)

        pygame.draw.rect(WIN, 'white', pygame.Rect(250, 400, 400, 50))

        for block in blocks:
            pygame.draw.rect(WIN, "light green", block)

        WIN.blit(rowdy_class._image, rowdy_class._coords)
        WIN.blit(screen, (0,0))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    cur = pygame.mouse.get_pos()
                    blocks.append(pygame.Rect(cur, (40, 40)))
                    print(cur)

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
                    x, y = 200, 400
                    test_rect = pygame.Rect((x, y), (25, 25))
                    for i in range(5):
                        if test_rect.collidelist(blocks) != -1:
                            rowdy_class.foodCollide(Foods)
                            if rowdy_class.wallCollide(walls):
                                rowdy_class.move()
                            print("hit")
                        x += 50
                        test_rect = pygame.Rect((x, y), (25, 25))

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
