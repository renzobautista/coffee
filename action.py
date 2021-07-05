from event import PourEvent, PlugEvent

class Action:
    def to_events(self, events_per_second):
        return {}

class PourAction(Action):
    def __init__(self, start_time, water_amount, duration):
        self.start_time = start_time # start time of action, in s
        self.water_amount = water_amount # amount of water poured, in mL
        self.duration = duration # duration of pour, in s

    def to_events(self, events_per_second):
        event_count = self.duration * events_per_second
        event_water_amount = self.water_amount / event_count
        event_map = {}
        start_event_index = self.start_time * events_per_second
        event_map = {}
        for i in range(event_count):
            event_time = start_event_index + i
            event_map[event_time] = PourEvent(event_water_amount)
        return event_map

class PlugAction(Action):
    def __init__(self, start_time, set_plugged):
        self.start_time = start_time
        self.set_plugged = set_plugged

    def to_events(self, events_per_second):
        start_event_index = self.start_time * events_per_second
        return { start_event_index: PlugEvent(self.set_plugged) }
