import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

pygame.init()

pygame.display.set_caption("Platformer")

BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 1000, 800  # Medidas de la pantalla
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))


def get_background(name):
    image = pygame.image.load("assets", "Background", name)
    x, y, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height):
            pos = [i * with, j * height]
            tiles.append(pos)

    return tiles, image 



def main(window):
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break



if __name__ == "__main__":
    main(window)