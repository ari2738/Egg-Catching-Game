import pygame
import random

pygame.init()

width = 500
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Egg Catching Game")

# Load Images
egg_img = pygame.image.load("egg.png")
basket_img = pygame.image.load("basket.png")

egg_img = pygame.transform.scale(egg_img, (40, 50))
basket_img = pygame.transform.scale(basket_img, (120, 60))

basket_x = width // 2
basket_y = height - 70
basket_speed = 8

egg_x = random.randint(50, width - 50)
egg_y = 0
egg_speed = 5

score = 0
lives = 3

font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 72)

clock = pygame.time.Clock()
running = True
game_over = False

while running:
    clock.tick(60)
    screen.fill((200, 230, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            basket_x -= basket_speed
        if keys[pygame.K_RIGHT]:
            basket_x += basket_speed

        if basket_x < 0:
            basket_x = 0
        if basket_x > width - 120:
            basket_x = width - 120

        egg_y += egg_speed

        # Collision
        if basket_y < egg_y + 50 and basket_x < egg_x < basket_x + 120:
            score += 1
            egg_y = 0
            egg_x = random.randint(50, width - 50)

        # Missed egg
        if egg_y > height:
            lives -= 1
            egg_y = 0
            egg_x = random.randint(50, width - 50)

        if lives == 0:
            game_over = True
            game_over_time = pygame.time.get_ticks()

        # Draw game
        screen.blit(basket_img, (basket_x, basket_y))
        screen.blit(egg_img, (egg_x, egg_y))

        score_text = font.render("Score: " + str(score), True, (0, 0, 0))
        lives_text = font.render("Lives: " + str(lives), True, (0, 0, 0))

        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (380, 10))

    else:
        # Show GAME OVER
        over_text = big_font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(over_text, (100, 250))

        # Wait 3 seconds then close
        if pygame.time.get_ticks() - game_over_time > 3000:
            running = False

    pygame.display.update()

pygame.quit()
