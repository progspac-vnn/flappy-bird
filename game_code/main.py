# Flappy Bird --> progspacvnn
import pygame
import sys
import random

# Draw floor 
def draw_floor():
    win.blit(fl,(fl_x,550))
    win.blit(fl,(fl_x + 450, 550))  # adding 2 blocks
# Pipe fn
def create_pipe():
    random_pipe_pos = random.choice(pipe_h)
    new_bottom = pipe_s.get_rect(midtop = (450,random_pipe_pos))
    new_top = pipe_s.get_rect(midbottom = (450,random_pipe_pos - 300))
    return new_top,new_bottom

# move pipes
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 2
    return pipes 

# draw pipes
def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 600:
            win.blit(pipe_s,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_s,False,True)
            win.blit(flip_pipe,pipe)
# collisions
def collisions(pipes):
    for pipe in pipes:
        if bird_r.colliderect(pipe):
            hit_sound.play()
            die_sound.play()
            return False
    if bird_r.top <= 5 or bird_r.bottom >= 555:
        hit_sound.play()
        die_sound.play()
        return False
    
    return True

def score_display(game_state):
    if game_state == 'game_main':
        score_surface = game_font.render(f'survival_time: {int(survival_time)}','True',(0,0,0))
        score_r = score_surface.get_rect(center=(215,50))
        win.blit(score_surface,score_r)
    if game_state == 'game_over':
        score_surface = game_font.render(f'survival_time: {int(survival_time)}','True',(0,0,0))
        score_r = score_surface.get_rect(center=(215,50))
        win.blit(score_surface,score_r)

        high_score_surface = game_font.render(f'highest_survival_time: {int(highest_survival_time)}','True',(0,0,0))
        high_score_r = high_score_surface.get_rect(center=(215,450))
        win.blit(high_score_surface,high_score_r)

def score_update(survival_time, highest_survival_time):
    if  survival_time >= highest_survival_time:
        highest_survival_time = survival_time
    return highest_survival_time

pygame.init()
win = pygame.display.set_mode((450,650))
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19__.TTF',30)

# Game Variables
g = 0.25
bird_move = 0
survival_time = 0
highest_survival_time = 0
game_on = True
# bg image 
bg = pygame.image.load('background-day.png').convert()
bg = pygame.transform.scale2x(bg)

# floor image
fl = pygame.image.load('base.png').convert()
fl = pygame.transform.scale2x(fl)
fl_x = 0 

# bird 
bird = pygame.image.load('redbird-midflap.png')
bird_r = bird.get_rect(center = (100,325))

# pipes
pipe_s = pygame.image.load('pipe-red.png')
pipe_l = []
pipe_h = [350,400,450,500]

P = pygame.USEREVENT
pygame.time.set_timer(P,1000)
running = True

game_over_surface = pygame.image.load('gameover.png').convert_alpha()
game_over_surface = pygame.transform.scale2x(game_over_surface)
game_over_r = game_over_surface.get_rect(center = (215,300))

# Sound
flap_sound = pygame.mixer.Sound('sfx_wing.wav')
hit_sound = pygame.mixer.Sound('sfx_hit.wav')
die_sound = pygame.mixer.Sound('sfx_die.wav')

#  Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_move = 0
                bird_move -= 8
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_on == False:
                game_on = True
                pipe_l.clear()
                bird_r.center = (100,300)
                bird_move = 0
                survival_time = 0
        if event.type == P:
            pipe_l.extend(create_pipe())
                
    # bg
    win.blit(bg,(0,-350))

    if game_on:
        bird_move += g 
        bird_r.centery += bird_move 
        # bird
        win.blit(bird,bird_r)
        # collision
        game_on = collisions(pipe_l)

        # score 
        survival_time += 0.01
        score_display('game_main')

        # pipes
        pipe_l = move_pipe(pipe_l)
        draw_pipes(pipe_l)
    else:
        win.blit(game_over_surface,game_over_r)
        highest_survival_time = score_update(survival_time, highest_survival_time)
        score_display('game_over')
    # floor
    fl_x -= 1
    draw_floor()

    if fl_x <= -450:
        fl_x = 0
    
    pygame.display.update()
    clock.tick(150)

