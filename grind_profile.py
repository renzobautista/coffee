import math
from enum import IntEnum

class GrindProfile:
    coffee_density = 0.43 # in g/mL
    def __init__(self, coffee_mass, grind_size):
        self.coffee_mass = coffee_mass # in g
        self.grind_size = grind_size # GrindSize, value in micrometers

        self.particle_radius = self.grind_size / 10000 / 2 # in cm
        particle_volume = 4 / 3 * math.pi * (self.particle_radius ** 3) # in cm^3, i.e. mL
        particle_surface_area = 4 * math.pi * (self.particle_radius ** 2) # in cm^2
        particle_mass = particle_volume * self.coffee_density # in g
        particle_count = self.coffee_mass / particle_mass
        self.surface_area = particle_count * particle_surface_area # in cm^2

        self.grind_volume = self.coffee_mass / self.coffee_density  # in mL

class GrindSize(IntEnum):
    SUPERFINE = 100 # diameter in micrometers
    FINE = 300
    MEDIUM_FINE = 500
    MEDIUM = 750
    COARSE = 1000
    EXTRA_COARSE = 1500
