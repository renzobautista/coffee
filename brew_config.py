from action import Action
class BrewConfig:
    def __init__(self, grind_profile, brew_method, actions, target_extracted_mass):
        self.grind_profile = grind_profile
        self.brew_method = brew_method
        self.actions = actions
        self.target_extracted_mass = target_extracted_mass

