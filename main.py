import pygame
from constants import ASTEROID_MIN_RADIUS,SCREEN_WIDTH,ASTEROID_KINDS,ASTEROID_SPAWN_RATE,ASTEROID_MAX_RADIUS,SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    timeClock = pygame.time.Clock()
    dt = 0

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()

    Player.containers = (updatable_group,drawable_group)
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group,)
    
    player = Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)
    asteroidField = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Thanks for playing this game!")
                return
            
        timeSinceLastFrameDrawn = timeClock.tick(60)
        dt = timeSinceLastFrameDrawn / 1000
        updatable_group.update(dt)

        screen.fill("black")

        for obj in drawable_group:
            obj.draw(screen)        
        pygame.display.update()


if __name__ == "__main__":
    main()
