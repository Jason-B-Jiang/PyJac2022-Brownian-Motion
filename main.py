#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import random
from ParticleManager import ParticleManager
from Button import *
from typing import Dict, List
pygame.init()

################################################################################

# Define constants

# Define game window
WIDTH = 925
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
def draw_window(manager: ParticleManager, buttons: List[Button],
                particle_values: Dict[str, int]) -> None:
    # create white background
    WINDOW.fill((255, 255, 255))

    # create particle container
    pygame.draw.rect(WINDOW,
                    (0, 0, 0),
                    (75, 75, 450, 450),
                     2)

    # draw labels for buttons adjusting particle speed/size/mass, and the buttons
    # themselves
    # reuse button to make labels, because I'm lazy
    speed_label = Button(575, 75, 100, 50, 'SPEED')
    speed_label.draw(WINDOW, (0, 0, 0))

    size_label = Button(575, 175, 100, 50, 'SIZE')
    size_label.draw(WINDOW, (0, 0, 0))

    mass_label = Button(575, 275, 100, 50, 'MASS')
    mass_label.draw(WINDOW, (0, 0, 0))

    # draw current values of particle speed/size/mass
    speed_value = Button(765, 75, 50, 50, str(particle_values['SPEED']),
                         color = (255, 255, 255), text_color= (0, 0, 0))
    size_value = Button(765, 175, 50, 50, str(particle_values['SIZE']),
                        color = (255, 255, 255), text_color = (0, 0, 0))
    mass_value = Button(765, 275, 50, 50, str(particle_values['MASS']),
                        color = (255, 255, 255), text_color = (0, 0, 0))
    speed_value.draw(WINDOW)
    size_value.draw(WINDOW)
    mass_value.draw(WINDOW)

    # draw buttons
    for button in buttons:
        button.draw(WINDOW, (0, 0, 0))

    # update particle velocities and positions
    manager.update_particles()

    # update positions and colors of all onscreen particles
    new_particle_info = manager.get_updated_particle_info()
    [pygame.draw.circle(WINDOW, p[0], p[1], p[2]) for p in new_particle_info]

    # refresh the display
    pygame.display.update()


def make_and_get_buttons() -> List[Button]:
    """Initialize buttons for the game and return a list of all the buttons.
    """
    clear_button = Button(575, 475, 140, 50, 'CLEAR', 'CLEAR')
    random_button = Button(750, 475, 140, 50, 'RANDOM', 'RANDOM')
    add_button = Button(575, 375, 140, 50, 'ADD', 'ADD')
    remove_button = Button(750, 375, 140, 50, 'REMOVE', 'REMOVE')
    speed_decr_button = Button(700, 75, 50, 50, '-', '-SPEED')
    speed_incr_button = Button(825, 75, 50, 50, '+', '+SPEED')
    size_decr_button = Button(700, 175, 50, 50, '-', '-SIZE')
    size_incr_button = Button(825, 175, 50, 50, '+', '+SIZE')
    mass_decr_button = Button(700, 275, 50, 50, '-', '-MASS')
    mass_incr_button = Button(825, 275, 50, 50, '+', '+MASS')

    return [clear_button, random_button, add_button, remove_button,
    speed_decr_button, speed_incr_button, size_decr_button, size_incr_button,
    mass_decr_button, mass_incr_button]


def clear(manager: ParticleManager) -> None:
    # Remove all particles on screen
    manager.clear()


def random_simulation(manager: ParticleManager, n: int) -> None:
    # Regenerate n random particles to simulate
    manager.clear()
    manager.simulate_n_particles(n)


def add_particle(manager: ParticleManager, particle_values: Dict[str, int]) -> None:
    """Add a new particle to the screen, with speed, size and mass specified
    by particle_values.

    Do nothing if MAX_PARTICLES is already on the screen
    """
    manager.add_particle(particle_values['SPEED'], particle_values['SIZE'],
                         particle_values['MASS'])


def remove_particle(manager: ParticleManager) -> None:
    """Remove the last added particle from the screen.
    Do nothing if there are no particles on the screen.
    """
    manager.remove_particle()


def adjust_particles(property: str, particle_values: Dict[str, int]) -> None:
    """Increase or decrease speed, mass or size of new particles added to screen
    by 1, by adjusting their values in the particle_values dictionary.

    Ensures that speed/mass/size values are between 1 and 5, inclusive.
    """
    operator = property[0]  # - or +
    value = property[1:]  # SPEED, MASS or SIZE

    if operator == '-':
        particle_values[value] = max(1, particle_values[value] - 1)
    else:
        particle_values[value] = min(5, particle_values[value] + 1)


def main():
    run = True
    clock = pygame.time.Clock()
    manager = ParticleManager()

    # keep track of scaling factors for the speed, mass and size of new
    # particles, with the factors being from 1 - 5
    particle_values = {'SPEED': 1, 'MASS': 1, 'SIZE': 1}
    buttons = make_and_get_buttons()

    # Initially have n random particles simulated on the screen, from 1 to
    # MAX_PARTICLES - 1
    manager.simulate_n_particles(random.randint(1, MAX_PARTICLES - 1))
    
    while run:
        clock.tick(FPS)  # run while loop 60x per second consistently

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.isOver(pygame.mouse.get_pos()):
                        action = button.action
                        print(f"{action} pressed")
                        if action == 'CLEAR':
                            clear(manager)
                        elif action == 'RANDOM':
                            n = random.randint(1, MAX_PARTICLES - 1)
                            random_simulation(manager, n)
                        elif action == 'ADD':
                            add_particle(manager, particle_values)
                        elif action == 'REMOVE':
                            remove_particle(manager)
                        elif '-' in action or '+' in action:
                            adjust_particles(button.action, particle_values)

        draw_window(manager, buttons, particle_values)

################################################################################

if __name__ == '__main__':
    main()
