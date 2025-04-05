# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import *
from shot import Shot

def game_over_screen(screen, my_font):
    screen.fill('black')
    game_over_text = my_font.render("GAME OVER", False, (255, 0, 0))
    game_over_text_note = my_font.render("(press 'ENTER' to close)", False, (255, 0, 0))
    screen.blit(game_over_text, (
        SCREEN_WIDTH // 2 - game_over_text.get_width() // 2,
        SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2
    ))
    screen.blit(game_over_text_note, (
        SCREEN_WIDTH // 2 - game_over_text_note.get_width() // 2,
        SCREEN_HEIGHT // 2 - (game_over_text_note.get_height() // 2) + game_over_text.get_height()
    ))
    pygame.display.flip()
    pygame.time.wait(3000)# Wait for 3 seconds before closing
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()

    pygame.font.init() # you have to call this at the start,
    # if you want to use this module.
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    hits = 0
    lives = 3
    running = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        updatable.update(dt)
        score_text = my_font.render(f"SCORE:{hits}", False, (255, 255, 255))
        lives_text = my_font.render(f"LIVES:{lives}", False, (255, 255, 255))
        screen.blit(score_text, (0, 0))
        screen.blit(lives_text, (0, 30))

        for asteroid in asteroids:
            if player.collision(asteroid) :
                if lives == 0:
                    print("Game over!")
                    game_over_screen(screen, my_font)
                    return
                else:
                    lives -= 1
                    asteroid.kill()
            for bullet in shots:
                if bullet.collision(asteroid):
                    if isinstance(asteroid, Asteroid):
                        hits += 1
                        bullet.kill()
                        asteroid.split()
                    break
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
