#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import numpy as np
from typing import List
from Particle import Particle
pygame.init()

################################################################################

# Define constants

# Define game window
WIDTH = 600
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

# Particle constants
PARTICLE_RADIUS = 10
NUM_PARTICLES = 10

FPS = 60

################################################################################

# Functions
def draw_window(particles):
    # create white background
    WINDOW.fill((255, 255, 255))

    # create particle container
    pygame.draw.rect(WINDOW,
                    (0, 0, 0),
                     pygame.Rect((0.25 * WIDTH) // 2,
                                 (0.25 * HEIGHT) // 2, 0.75 * WIDTH, 0.75 * HEIGHT),
                     2)

    draw_particles(particles)  # update all onscreen particles
    pygame.display.update()  # refresh the display


def simulate_n_particles(n: int) -> list:
    """Simulate n particles of uniform size and mass, with random initial
    velocities and starting positions.
    """
    particles = []
    for i in range(n):
        rand_vel = np.random.uniform(low = 2, high = 2, size = (2,))
        rand_pos = np.random.uniform(low = 75 + 20, high = 525 - 20, size = (2,))
        particles.append(Particle(rand_vel, rand_pos))

    return particles


def draw_particles(particles) -> None:
    # update all particle velocities and positions
    for p in particles:
        p.update_position()
        pygame.draw.circle(WINDOW, (0, 0, 255), p.get_position(), PARTICLE_RADIUS)

def main():
    run = True
    clock = pygame.time.Clock()

    particles = simulate_n_particles(NUM_PARTICLES)
    
    while run:
        clock.tick(FPS)  # run while loop 60x per second consistently

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        draw_window(particles)

    main()  # recursively re-run the game loop

################################################################################

if __name__ == '__main__':
    main()
