from brew_config import BrewConfig
from action import PourAction, PlugAction
from grind_profile import GrindProfile, GrindSize
from brew_method import Percolation, Immersion

def hoffman_v60():
    coffee_mass = 30
    bloom_pour = PourAction(0, 60, 15)
    first_pour = PourAction(45, 240, 30)
    final_pour = PourAction(75, 200, 30)
    pour_actions = [bloom_pour, first_pour, final_pour]
    return BrewConfig(
        GrindProfile(coffee_mass, GrindSize.MEDIUM_FINE),
        Percolation(2.31), # Approximated from Hoffman's 3:30 brew time, unit: mL/s
        pour_actions,
        coffee_mass * 0.2
    )

def two_min_immersion():
    coffee_mass = 11.0
    pour_actions = [PourAction(0, 200, 30)]
    return BrewConfig(
        GrindProfile(coffee_mass, GrindSize.MEDIUM_FINE),
        Immersion(120),
        pour_actions,
        coffee_mass * 0.2
    )

def eight_min_immersion():
    coffee_mass = 11.0
    pour_actions = [PourAction(0, 200, 30)]
    return BrewConfig(
        GrindProfile(coffee_mass, GrindSize.MEDIUM),
        Immersion(480),
        pour_actions,
        coffee_mass * 0.2
    )

def aeropress_champ_2019():
    coffee_mass = 30
    pour_actions = [PourAction(0, 100, 10)]
    return BrewConfig(
        GrindProfile(coffee_mass, GrindSize.COARSE),
        Immersion(50),
        pour_actions,
        13.3 * 0.2 # I guess copy the target from a normal aeropress cup?
    )

def phased_aeropress():
    coffee_mass = 13.3
    actions = [
        PourAction(0, 120, 15),
        PlugAction(15, True),
        PlugAction(60, False),
        PourAction(90, 80, 30),
        PlugAction(120, True),
        PlugAction(150, False),
    ]
    return BrewConfig(
        GrindProfile(coffee_mass, GrindSize.MEDIUM_FINE),
        Percolation(1),
        actions,
        13.3 * 0.2 # I guess copy the target from a normal aeropress cup?
    )
