#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import random
from Particle import Particle
from typing import List, Tuple

# Minimum and maximum speeds, masses and radii for simulated particles
MIN_SPEED = 2
MAX_SPEED = 10
MIN_MASS = 12
MAX_MASS = 20
MIN_RADIUS = 12
MAX_RADIUS = 20

# Minimum and maximum values for both x and y coordinates of a particle, defined
# by the square holding the particles
MIN_POS = 75 + 25
MAX_POS = 525 - 25

# default color of blue for particles
COLOR = (0, 0, 255)

# Maximum number of particles to simulate
MAX_PARTICLES = 30

################################################################################

class ParticleManager:
    """Stores simulated particles, and controls adding/removing particles from
    the screen.
    """
    def __init__(self):
        self.particles = []

    def simulate_n_particles(self, n: int) -> None:
        """Initialize n particles of random velocities, positions, sizes and
        mass, storing the particles in self.particles.
        """
        for _ in range(n):
            rand_vel = np.random.uniform(low = -MAX_SPEED, high = MAX_SPEED,
                                         size = (2,))
            rand_pos = np.random.uniform(low = MIN_POS, high = MAX_POS,
                                         size = (2,))
            rand_radius = random.randint(MIN_RADIUS, MAX_RADIUS)
            rand_mass = random.randint(MIN_MASS, MAX_MASS)

            rand_particle = Particle(rand_vel, rand_pos, rand_radius, rand_mass,
                                     COLOR)

            self.particles.append(rand_particle)

    def update_particles(self) -> None:
        """Update velocities and positions for all particles in self.particles
        in a single frame, based on particle velocities and collisions.
        """
        for p in self.particles:
            p.update_position([par for par in self.particles if par != p])

    def clear(self) -> None:
        """Removes all particles stored in the ParticleManager.
        """
        self.particles = []

    def get_num_particles(self) -> int:
        """Returns number of particles stored by ParticleManager.
        """
        return len(self.particles)

    def get_updated_particle_info(self) -> List[Tuple]:
        """Return a list of tuples, where each tuple contains the new color
        (scaled by the particle's speed), position and radius for a particle.
        """
        particle_tuples = []
        for p in self.particles:
            new_col = (np.clip(30 * np.linalg.norm(p.vel), 0, 255), 0, 255)
            new_pos = p.get_position()
            r = p.r

            particle_tuples.append((new_col, new_pos, r))

        return particle_tuples
    
    def remove_particle(self) -> None:
        """Remove a particle from self.particles, and do nothing if
        self.particles is already empty.
        """
        if len(self.particles) > 0:
            self.particles.pop()

    def add_particle(self, speed: int, radius: int,
                     mass: int) -> None:
        """Adds a new particle for simulation, with speed, radius and mass
        determining the magnitude of each of these properties for the new
        particle.
        
        Preconditions: speed, radius and mass are all between 1 to 5, inclusive.
        """
        if len(self.particles) == MAX_PARTICLES:
            return  # don't allow number of simulated particles to exceed max

        new_vel = np.array([MIN_SPEED + 2 * (speed - 1),
                            MIN_SPEED + 2 * (speed - 1)])
        new_pos = np.random.uniform(low=MIN_POS, high=MAX_POS,
                                     size=(2,))
        new_radius = MIN_RADIUS + 2 * (radius - 1)
        new_mass = MIN_MASS + 2 * (mass - 1)

        p = Particle(new_vel, new_pos, new_radius, new_mass, COLOR)

        self.particles.append(p)
