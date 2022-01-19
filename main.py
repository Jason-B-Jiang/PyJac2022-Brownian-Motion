#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
pygame.init()

################################################################################

# Define constants

# Define game window
WIDTH = 600
HEIGHT = 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))  # set main window
pygame.display.set_caption("Brownian motion simulator!")  # set window name

# Particle container
CONTAINER_WIDTH = 450
CONTAINER_HEIGHT = 450
CONTAINER_BORDERS = {
    'LEFT': (0.25 * WIDTH) // 2,
    'RIGHT': WIDTH - ((0.25 * WIDTH) // 2),
    'UP': (0.25 * HEIGHT) // 2,
    'DOWN': HEIGHT - ((0.25 * HEIGHT) // 2)
}

# Particle size
PARTICLE_RADIUS = 10

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

    # put all particles onto screen
    draw_particles(particles)
    pygame.draw.circle(WINDOW, (0, 0, 255), (100, 100), PARTICLE_RADIUS)
    
    pygame.display.update()

def draw_particles(particles):
    [p.detect_collisions() for p in particles]  # detect collisions and update velocities
    for particle in particles:
        # update position using velocity
        # use position to draw new circle for each particle
        pass

def main():
    run = True
    clock = pygame.time.Clock()

    particles = []
    
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
