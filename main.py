import pygame
from logger import log_state
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_RADIUS
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Sets the screen size

    # Restrict our game to draw a maximum of 60 times per second, or 60 FPS
    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state() # 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Makes the windows close button work. 
                return
            
        updatable.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip() #Refresh the screen
        dt = clock.tick(60) / 1000 # limit the framerate to 60 FPS
        # Restrict our game to draw a maximum of 60 times per second, or 60 FPS




if __name__ == "__main__":
    main()
