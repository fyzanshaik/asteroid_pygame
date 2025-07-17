import pygame
from constants import ASTEROID_MIN_RADIUS,SCREEN_WIDTH,ASTEROID_KINDS,ASTEROID_SPAWN_RATE,ASTEROID_MAX_RADIUS,SCREEN_HEIGHT

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    timeClock = pygame.time.Clock()
    dt = 0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Thanks for playing this game!")
                return
        screen.fill("black")
        pygame.display.update()
        timeSinceLastFrameDrawn = timeClock.tick(60)
        dt = timeSinceLastFrameDrawn / 1000
if __name__ == "__main__":
    main()
