import pygame
import sys
import math

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            fillGrid(pos)
        pygame.display.update()

def fillGrid(click):
    blockSize = 20
    xStart = math.floor(click[0] / 20) * 20
    yStart = math.floor(click[1] / 20) * 20
    rect = pygame.Rect(xStart * blockSize, yStart * blockSize,
                       blockSize, blockSize)
    pygame.draw.rect(SCREEN, WHITE, rect, 1)
    print (click)
    print (xStart, yStart)


def drawGrid():
    blockSize = 20 #Set the size of the grid block
    for x in range(WINDOW_WIDTH):
        for y in range(WINDOW_HEIGHT):
            print (x, y)
            rect = pygame.Rect(x*blockSize, y*blockSize,
                               blockSize, blockSize)
            pygame.draw.rect(SCREEN, BLACK, rect, 1)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
