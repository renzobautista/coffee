from analytics import analyze
from compound import generate_compounds
from brew_ecosystem import BrewEcosystem
from brew_configs import *
from simulation_config import SimulationConfig, SimulationGranularity

def main():
    config = hoffman_v60()
    simulation_config = SimulationConfig(SimulationGranularity.SECOND)
    compounds = generate_compounds(
        config.grind_profile.coffee_mass,
        simulation_config.diffusion_coefficient_multiplier,
        count=200
    )
    ecosystem = BrewEcosystem(compounds, config, simulation_config)
    snapshots = ecosystem.run()
    analyze(ecosystem, snapshots)

if __name__ == "__main__":
    main()