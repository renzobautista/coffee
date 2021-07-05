from event import DripEvent

class BrewMethod:
    def is_complete(self, ecosystem):
        return True
    def create_events(self, events_per_second):
        return []

class Percolation(BrewMethod):
    def __init__(self, drip_rate):
        self.drip_rate = drip_rate
    def is_complete(self, ecosystem):
        return (ecosystem.time > ecosystem.last_pour_ms
            and ecosystem.chamber_water <= ecosystem.config.grind_profile.coffee_mass * 2)
    def create_events(self, events_per_second):
        event_drip_amount = self.drip_rate / events_per_second
        return [DripEvent(event_drip_amount)]

class Immersion(BrewMethod):
    def __init__(self, brew_time):
        self.brew_time = brew_time # in s
    def is_complete(self, ecosystem):
        return ecosystem.time >= self.brew_time * ecosystem.simulation_config.events_per_second
