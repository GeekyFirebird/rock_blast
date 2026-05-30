import pygame
from logger import log_state
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    # Restrict our game to draw a maximum of 60 times per second, or 60 FPS
    clock = pygame.time.Clock()
    dt = 0.0


    while True:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Sets the screen size
        log_state() # 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Makes the windows close button work. 
                return
        screen.fill("black")
        pygame.display.flip() #Refresh the screen
        dt = clock.tick(60) / 1000 # limit the framerate to 60 FPS

        # Restrict our game to draw a maximum of 60 times per second, or 60 FPS




if __name__ == "__main__":
    main()
