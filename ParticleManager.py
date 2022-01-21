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
            rand_vel = np.random.uniform(low = MIN_SPEED, high = MAX_SPEED,
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

    def get_updated_particle_info(self) -> List[Tuple]:
        """Return a list of tuples, where each tuple contains the new color
        (scaled by the particle's speed), position and radius for a particle.
        """
        particle_tuples = []
        for p in self.particles:
            new_col = (np.clip(20 * np.linalg.norm(p.vel), 0, 255), 0, 255)
            new_pos = p.get_position()
            r = p.r

            particle_tuples.append((new_col, new_pos, r))

        return particle_tuples