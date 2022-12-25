import pygame


def timer_start():
    """Starts a timer.

    Returns:
        integer: Timer start time.
    """
    timer = pygame.time.get_ticks()
    return timer


def timer_stop(timer):
    """Calculates the time difference between 
    the timer start time and the current time.

    Args:
        timer: Timer start time.

    Returns:
        integer: Timer stop time (the time difference
        between the timer start time and the current time).
    """
    stop_time = pygame.time.get_ticks() - timer
    return stop_time
