#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import random
from ParticleManager import ParticleManager
pygame.init()

################################################################################

# Define constants

# Define game window
WIDTH = 800
HEIGHT = 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))  # set main window
pygame.display.set_caption("Many body interactions!")  # set window name

# Particle container
CONTAINER_WIDTH = 450
CONTAINER_HEIGHT = 450
CONTAINER_BORDERS = {
    'LEFT': (0.25 * WIDTH) // 2,
    'RIGHT': WIDTH - ((0.25 * WIDTH) // 2),
    'UP': (0.25 * HEIGHT) // 2,
    'DOWN': HEIGHT - ((0.25 * HEIGHT) // 2)
}

# Simulation constants
MAX_PARTICLES = 30
FPS = 60

################################################################################

# Functions
def draw_window(manager: ParticleManager):
    # create white background
    WINDOW.fill((255, 255, 255))

    # create particle container
    pygame.draw.rect(WINDOW,
                    (0, 0, 0),
                    (75, 75, 450, 450),
                     2)

    # update particle velocities and positions
    manager.update_particles()

    # update positions and colors of all onscreen particles
    new_particle_info = manager.get_updated_particle_info()
    [pygame.draw.circle(WINDOW, p[0], p[1], p[2]) for p in new_particle_info]

    # refresh the display
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    manager = ParticleManager()

    # Initially have n random particles simulated on the screen, from 1 to
    # MAX_PARTICLES
    manager.simulate_n_particles(random.randint(1, MAX_PARTICLES))
    
    while run:
        clock.tick(FPS)  # run while loop 60x per second consistently

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        draw_window(manager)

    main()  # recursively re-run the game loop

################################################################################

if __name__ == '__main__':
    main()
