import pygame
import os

Width, Height = 760, 760
rows, cols = 8, 8
Square = Width // rows

brown = (87, 16, 16)
white = (225, 225, 225)

# import piece
Path = 'chess_images/'

# Black Pieces

black_knight = pygame.transform.scale(pygame.image.load(os.path.join(Path, "bKN.png")), (Square, Square))
black_queens = pygame.transform.scale(pygame.image.load(os.path.join(Path, "bQ.png")), (Square, Square))
black_bishop = pygame.transform.scale(pygame.image.load(os.path.join(Path, "bB.png")), (Square, Square))
black_king = pygame.transform.scale(pygame.image.load(os.path.join(Path, "bK.png")), (Square, Square))
black_rock = pygame.transform.scale(pygame.image.load(os.path.join(Path, "bR.png")), (Square, Square))
black_pion = pygame.transform.scale(pygame.image.load(os.path.join(Path, "bP.png")), (Square, Square))

# White Pieces

white_knight = pygame.transform.scale(pygame.image.load(os.path.join(Path, "wKN.png")), (Square, Square))
white_queens = pygame.transform.scale(pygame.image.load(os.path.join(Path, "wQ.png")), (Square, Square))
white_bishop = pygame.transform.scale(pygame.image.load(os.path.join(Path, "wB.png")), (Square, Square))
white_king = pygame.transform.scale(pygame.image.load(os.path.join(Path, "wK.png")), (Square, Square))
white_rock = pygame.transform.scale(pygame.image.load(os.path.join(Path, "wR.png")), (Square, Square))
white_pion = pygame.transform.scale(pygame.image.load(os.path.join(Path, "wP.png")), (Square, Square))
