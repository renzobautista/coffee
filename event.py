class Event:
    def trigger(self, ecosystem):
        return

class PourEvent(Event):
    def __init__(self, water):
        self.water = water
    def trigger(self, ecosystem):
        ecosystem.chamber_water += self.water

class DripEvent(Event):
    def __init__(self, water):
        self.water = water
    def trigger(self, ecosystem):
        if ecosystem.chamber_water <= 0:
            return
        if ecosystem.is_plugged:
            return
        drip_amount = min(ecosystem.chamber_water, self.water)
        for compound in ecosystem.compounds:
            compound.drip(ecosystem.chamber_water, drip_amount)
        ecosystem.dripped_water += drip_amount
        ecosystem.chamber_water -= drip_amount

class ExtractEvent(Event):
    def trigger(self, ecosystem):
        if ecosystem.chamber_water <= 0:
            return
        thickness = 0.05  # thickness of the concentration gradient, approximated to 0.5mm, reduced by stirring, unit: cm
        for compound in ecosystem.compounds:
            grind_concentration = compound.grind_mass / ecosystem.config.grind_profile.grind_volume # g/mL
            chamber_concentration = compound.chamber_mass / ecosystem.chamber_water # g/mL
            # Noyes-Whitney approximation, unit: g/s
            extraction_rate = (ecosystem.config.grind_profile.surface_area # cm^2
                * compound.diffusion_coefficient # cm^2/s
                / thickness # cm
                * (grind_concentration - chamber_concentration)) # g/mL
            if extraction_rate <= 0:
                return

            extracted_mass = extraction_rate / ecosystem.simulation_config.events_per_second # g, extraction amount in one ms
            compound.extract(extracted_mass)

class PlugEvent(Event):
    def __init__(self, set_plugged):
        self.set_plugged = set_plugged

    def trigger(self, ecosystem):
        ecosystem.is_plugged = self.set_plugged
