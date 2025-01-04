import pygame
from constants import * 

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #pygame.Surface.fill(color, rect=None, special_flags=0)
        pygame.display.flip()
        
    
    



if __name__ == "__main__":
    main()