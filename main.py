import pygame
import sys
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from Shot import *

def main():
    pygame.init()
    Clock = pygame.time.Clock()
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (drawable, updatable, shots)
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    komeetveld = AsteroidField()
    while 0 < 1 :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for everyasteroid in asteroids:
            if everyasteroid.check_for_collision(player):
                print ("Game over !")
                sys.exit()
        for everyasteroid in asteroids:
            for everybullet in shots:
                if everybullet.check_for_collision(everyasteroid):
                    everyasteroid.split()
        pygame.Surface.fill(screen,(0,0,0))  
        for drawablestuff in drawable:
            drawablestuff.draw(screen)
        pygame.display.flip()
        dt = Clock.tick(60)/1000         
    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()