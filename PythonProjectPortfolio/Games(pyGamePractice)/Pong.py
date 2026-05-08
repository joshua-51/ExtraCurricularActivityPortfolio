import pygame
import sys
import random

# --- 1. SETUP ---
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong - Progressive Difficulty")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 40)

# --- 2. GAME OBJECTS ---
ball = pygame.Rect(WIDTH//2 - 12, HEIGHT//2 - 12, 24, 24)
player = pygame.Rect(10, HEIGHT//2 - 70, 15, 140)
opponent = pygame.Rect(WIDTH - 25, HEIGHT//2 - 70, 15, 140)

# --- 3. DYNAMIC PHYSICS ---
INITIAL_BALL_SPEED = 6
ball_speed_x = INITIAL_BALL_SPEED * random.choice((1, -1))
ball_speed_y = INITIAL_BALL_SPEED * random.choice((1, -1))
speed_multiplier = 1.05 # Increases speed by 5% each hit

player_speed = 0
# AI speed starts slightly lower than initial ball speed to allow for misses
opponent_base_speed = 5.5 

player_score = 0
opponent_score = 0

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH//2, HEIGHT//2)
    # Reset to base speed so the game doesn't start too fast after a point
    ball_speed_x = INITIAL_BALL_SPEED * random.choice((1, -1))
    ball_speed_y = INITIAL_BALL_SPEED * random.choice((1, -1))

# --- 4. MAIN LOOP ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: player_speed -= 7
            if event.key == pygame.K_DOWN: player_speed += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP: player_speed += 7
            if event.key == pygame.K_DOWN: player_speed -= 7

    # Ball Movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Wall Bounces
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Scoring
    if ball.left <= 0:
        opponent_score += 1
        ball_restart()
    if ball.right >= WIDTH:
        player_score += 1
        ball_restart()

    # --- PADDLE COLLISIONS WITH SPEED UP ---
    if ball.colliderect(player) and ball_speed_x < 0:
        ball_speed_x *= -speed_multiplier # Reverse and Speed Up!
        ball_speed_y *= speed_multiplier
        ball.left = player.right

    if ball.colliderect(opponent) and ball_speed_x > 0:
        ball_speed_x *= -speed_multiplier # Reverse and Speed Up!
        ball_speed_y *= speed_multiplier
        ball.right = opponent.left

    # Player Movement
    player.y += player_speed
    player.clamp_ip(screen.get_rect()) # Keeps paddle on screen

    # --- IMPERFECT AI LOGIC ---
    # The AI targets the ball's center but moves at a limited speed
    if opponent.centery < ball.centery:
        opponent.y += opponent_base_speed
    if opponent.centery > ball.centery:
        opponent.y -= opponent_base_speed
    opponent.clamp_ip(screen.get_rect())

    # --- DRAWING ---
    screen.fill((20, 20, 20))
    pygame.draw.rect(screen, (255, 255, 255), player)
    pygame.draw.rect(screen, (255, 255, 255), opponent)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    pygame.draw.aaline(screen, (100, 100, 100), (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    p_text = font.render(str(player_score), True, (255, 255, 255))
    o_text = font.render(str(opponent_score), True, (255, 255, 255))
    screen.blit(p_text, (WIDTH//2 - 60, 20))
    screen.blit(o_text, (WIDTH//2 + 30, 20))

    pygame.display.flip()
    clock.tick(60)