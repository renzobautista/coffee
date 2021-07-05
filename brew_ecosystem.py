from compound import CompoundSnapshot
from event import ExtractEvent
from brew_method import Percolation, Immersion

class BrewEcosystem:
    def __init__(self, compounds, config, simulation_config):
        self.is_plugged = False
        self.compounds = compounds
        self.config = config
        self.simulation_config = simulation_config
        self.time = 0 # unit depends on simulation_config.events_per_second
        self.chamber_water = 0 # mL
        self.dripped_water = 0 # mL
        action_events_map = {}
        for action in config.actions:
            events = action.to_events(simulation_config.events_per_second)
            for time in events.keys():
                if time not in action_events_map:
                    action_events_map[time] = []
                action_events_map[time].append(events[time])
        self.action_events_map = action_events_map
        self.last_pour_ms = max(action_events_map.keys())

    def is_complete(self):
        return self.config.brew_method.is_complete(self)

    def step(self):
        if self.time in self.action_events_map.keys():
            for event in self.action_events_map[self.time]:
                event.trigger(self)
        ExtractEvent().trigger(self)
        for event in self.config.brew_method.create_events(self.simulation_config.events_per_second):
            event.trigger(self)
        self.time += 1

    def run(self):
        snapshots = []
        while not self.is_complete():
            self.step()
            snapshot = BrewEcosystemSnapshot(self)
            if (self.time % self.simulation_config.events_per_second == 0):
                print(self.time / self.simulation_config.events_per_second)
            snapshots.append(snapshot)
        return snapshots

class BrewEcosystemSnapshot:
    def __init__(self, ecosystem):
        self.compounds = list(map(lambda x: CompoundSnapshot(x), ecosystem.compounds))
        self.time = ecosystem.time
        self.chamber_water = ecosystem.chamber_water
        self.dripped_water = ecosystem.dripped_water

    def extracted_coffee_mass(self, brew_method):
        extracted_mass_fn = lambda x: 0
        if type(brew_method) is Percolation:
            extracted_mass_fn = lambda x: x.dripped_mass
        elif type(brew_method) is Immersion:
            extracted_mass_fn = lambda x: x.chamber_mass
        else:
            raise Exception("Invalid brew method.")
        return sum(map(extracted_mass_fn, self.compounds))