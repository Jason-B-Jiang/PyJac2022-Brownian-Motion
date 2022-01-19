#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

class Particle:
    def __init__(self, r: int, mass: int, vel: np.array):
        self.r = r
        self.mass = mass
        self.vel = vel

    def get_radius(self) -> int:
        return self.r
        
    def get_mass(self) -> int:
    	return self.mass

    def get_velocity(self) -> np.array:
        return self.vel
        
    def detect_collisions(self) -> None:
    	pass
