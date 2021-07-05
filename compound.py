import random
from brew_method import Percolation, Immersion

class Compound:
    def __init__(self, diffusion_coefficient, availability_ratio):
        self.diffusion_coefficient = diffusion_coefficient # cm^2/s
        self.availability_ratio = availability_ratio

    def __str__(self):
        return "({d:.2f}, {a:.2f})".format(d=self.diffusion_coefficient, a=self.availability_ratio)

    def set_initial_mass(self, initial_mass):
        self.initial_mass = initial_mass # in g
        self.grind_mass = initial_mass # in g
        self.chamber_mass = 0 # in g
        self.dripped_mass = 0 # in g

    def drip(self, chamber_water, drip_amount):
        ''' Water amounts in mL '''
        compound_mass_in_drip = self.chamber_mass / chamber_water * drip_amount # concentration in chamber * drip volume
        self.chamber_mass -= compound_mass_in_drip
        self.dripped_mass += compound_mass_in_drip

    def extract(self, extracted_mass):
        self.chamber_mass += extracted_mass
        self.grind_mass -= extracted_mass

class CompoundSnapshot:
    def __init__(self, compound):
        self.initial_mass = compound.initial_mass
        self.diffusion_coefficient = compound.diffusion_coefficient
        self.grind_mass = compound.grind_mass
        self.chamber_mass = compound.chamber_mass
        self.dripped_mass = compound.dripped_mass

    def extracted_mass(self, brew_method):
        if type(brew_method) is Percolation:
            return self.dripped_mass
        elif type(brew_method) is Immersion:
            return self.chamber_mass
        else:
            raise Exception("Invalid brew method.")

def generate_compounds(coffee_mass, diffusion_coefficient_multiplier, count=30):
    compounds = []
    for i in range(count):
        compounds.append(Compound(random.random() * diffusion_coefficient_multiplier, random.random()))
    total_extractable_mass = coffee_mass * 0.28 # TEM is computed as 28% of coffee mass
    total_availabilities = sum(map(lambda x: x.availability_ratio, compounds))
    for compound in compounds:
        compound.set_initial_mass(total_extractable_mass * compound.availability_ratio / total_availabilities)
    return compounds
