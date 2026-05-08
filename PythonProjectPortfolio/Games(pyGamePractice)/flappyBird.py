import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
GRAVITY = 0.25
BIRD_JUMP = -6
PIPE_GAP = 150
PIPE_FREQUENCY = 1500 

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
game_font = pygame.font.SysFont('Arial', 32)

# Game Variables
bird_rect = pygame.Rect(50, 300, 30, 30)
bird_movement = 0
pipes = []
last_pipe = pygame.time.get_ticks()
game_active = True

# Score Variables
score = 0
high_score = 0
can_score = True # Prevents a single pipe from giving multiple points

def create_pipe():
    random_pipe_pos = random.randint(150, 450)
    bottom_pipe = pygame.Rect(SCREEN_WIDTH, random_pipe_pos, 50, 600)
    top_pipe = pygame.Rect(SCREEN_WIDTH, random_pipe_pos - PIPE_GAP - 600, 50, 600)
    return bottom_pipe, top_pipe

def move_pipes(pipes_list):
    for pipe in pipes_list:
        pipe.centerx -= 3
    return [pipe for pipe in pipes_list if pipe.right > 0]

def draw_pipes(pipes_list):
    for pipe in pipes_list:
        pygame.draw.rect(screen, (0, 200, 0), pipe)

def check_collision(pipes_list):
    for pipe in pipes_list:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= 0 or bird_rect.bottom >= SCREEN_HEIGHT:
        return False
    return True

def display_score(status):
    if status == 'playing':
        score_surface = game_font.render(f'Score: {int(score)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center = (200, 50))
        screen.blit(score_surface, score_rect)
    if status == 'game_over':
        score_surface = game_font.render(f'Score: {int(score)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center = (200, 50))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'High Score: {int(high_score)}', True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center = (200, 550))
        screen.blit(high_score_surface, high_score_rect)

def update_score(pipes_list, current_score):
    for pipe in pipes_list:
        # If bird passes the center of a pipe
        if 45 < pipe.centerx < 55:
            current_score += 0.5 # Two pipes (top/bottom) = 1 point
    return current_score

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement += BIRD_JUMP
            if event.key == pygame.K_SPACE and not game_active:
                game_active = True
                pipes.clear()
                bird_rect.center = (50, 300)
                bird_movement = 0
                score = 0

    screen.fill((135, 206, 235)) 

    if game_active:
        # Bird Physics
        bird_movement += GRAVITY
        bird_rect.centery += bird_movement
        pygame.draw.rect(screen, (255, 255, 0), bird_rect)

        # Pipes
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > PIPE_FREQUENCY:
            pipes.extend(create_pipe())
            last_pipe = time_now

        pipes = move_pipes(pipes)
        draw_pipes(pipes)

        # Collision & Scoring
        game_active = check_collision(pipes)
        score = update_score(pipes, score)
        display_score('playing')
    else:
        # Update High Score
        if score > high_score:
            high_score = score
        
        display_score('game_over')
        over_text = game_font.render("Press Space to Restart", True, (255, 255, 255))
        screen.blit(over_text, (65, 280))

    pygame.display.update()
    clock.tick(60)