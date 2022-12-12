import pygame

def timer_start():
    timer = pygame.time.get_ticks()
    return timer

def timer_stop(timer):
    stop_time = pygame.time.get_ticks() - timer
    return stop_time