#! /usr/bin/env python3

import sys
import pygame
from SrcGame.constants import *

pygame.init()
clock = pygame.time.Clock()
Win = pygame.display.set_mode((Width, Height))

def main():
	FPS = 60
	run = True
	while run:
		clock.tick(FPS)
		Win.blit(white_bishop, (50,50))
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				quit()
	sys.exit(0)

if __name__ == "__main__":
    main()
    