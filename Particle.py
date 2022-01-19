#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import annotations
import numpy as np
from typing import Tuple

MASS = 1
RADIUS = 10
COLOR = (0, 0, 255)  # default color of blue for particles
X_LIMITS = [75, 525]
Y_LIMITS = [75, 525]

class Particle:
    def __init__(self, vel: np.array, position: np.array, r: int = RADIUS,
                 mass: int = MASS, color: Tuple[int] = COLOR):
        self.vel = vel
        self.pos = position  # centre of the particle
        self.r = r  # radius around the centre
        self.mass = mass
        self.color = color

    def _get_x(self) -> float:
        return self.pos[0]

    def _get_y(self) -> float:
        return self.pos[1]

    def update_position(self) -> None:
        # will also check for collision w/ wall and update velocity accordingly
        self.check_wall_collision()

        # update position using updated velocity, and assuming time increment of
        # 1 unit
        self.pos = np.array(
            [self._get_x() + self.vel[0], self._get_y() + self.vel[1]]
        )

    def get_position(self) -> Tuple[float]:
        return self._get_x(), self._get_y()

    def check_wall_collision(self) -> bool:
        """Checks if the particle has collided with any of the container walls,
        and adjusts the particle's velocity to collide elastically if so.

        A collision counts as the particle being within 5 pixels of a wall,
        including the radius of the particle.
        """

        # check for collision with left/right container borders
        # count as collision if particle is 10 + radius units away from border
        dx_left = self._get_x() - (X_LIMITS[0] + 5 + self.r)
        dx_right = (X_LIMITS[1] - 5 - self.r) - self._get_x()
        dy_top = self._get_y() - (Y_LIMITS[0] + 5 + self.r)
        dy_bottom = (Y_LIMITS[1] - 5 - self.r) - self._get_y()
        
        # collided with left or right border
        if dx_left <=0 or dx_right <= 0:
            # particle's velocity is perpendicular to left/right border, so
            # reverse its velocity
            print('collided with side')
            if np.dot(self.vel, np.array([0, 1])) == 0:
                self.vel = -self.vel
                print('head-on collision with side')
            else:
                # otherwise, flip velocity vector and negate new y velocity,
                # to bounce off right angle from wall
                self.vel = np.array([self.vel[1], -self.vel[0]])
        
        elif dy_top <= 0 or dy_bottom <= 0:
            # particle velocity perpendicular to top/bottom border
            print('collided with top/bottom')
            if np.dot(self.vel, np.array([1, 0])) == 0:
                self.vel = -self.vel
                print('head-on collision with top/bottom')
            else:
                self.vel = np.array([self.vel[1], -self.vel[0]])
        
    def collided_with(self, other: Particle) -> bool:
        """Check if particle has collided with some other particle.
        If so, adjust the velocity of both particles accordingly, assuming
        a perfect elastic collision.
        """
        pass