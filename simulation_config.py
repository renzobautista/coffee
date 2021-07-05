from enum import IntEnum

class SimulationGranularity(IntEnum):
    SECOND = 1
    CENTISECOND = 100
    HALF_SECOND = 500
    MILLISECOND = 1000

class SimulationConfig:
    def __init__(self, events_per_second, diffusion_coefficient_multiplier=1/50000):
        self.events_per_second = events_per_second
        self.diffusion_coefficient_multiplier = diffusion_coefficient_multiplier
