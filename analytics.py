import matplotlib.pyplot as plt

def analyze(ecosystem, snapshots):
    basic_analytics(ecosystem, snapshots)
    plot_total_extraction_over_time(ecosystem, snapshots)
    plot_diffusion_vs_initial_and_final_mass_ratios(ecosystem, snapshots)
    plot_diffusion_vs_mass_ratio_difference(ecosystem, snapshots)
    plot_initial_vs_final_mass_ratios(ecosystem, snapshots)

def basic_analytics(ecosystem, snapshots):
    # Brew time
    time_in_s = ecosystem.time // ecosystem.simulation_config.events_per_second
    minutes = time_in_s // 60
    seconds = time_in_s % 60
    print("total time: {m:d}:{s:d}".format(m=minutes, s=seconds))

    # Total extraction
    extracted_coffee_mass = snapshots[-1].extracted_coffee_mass(ecosystem.config.brew_method)
    print("target extracted mass: {tem:.2f}".format(tem=ecosystem.config.target_extracted_mass))
    print("total extracted mass: {tem:.2f}".format(tem=extracted_coffee_mass)) 
    print("accuracy: {diff:.2f}%".format(
        diff=(extracted_coffee_mass - ecosystem.config.target_extracted_mass) 
            / ecosystem.config.target_extracted_mass
            * 100
        )
    ) 
    print("total extracted mass %: {tem:.2f}%".format(tem=extracted_coffee_mass / ecosystem.config.grind_profile.coffee_mass * 100)) 

def plot_total_extraction_over_time(ecosystem, snapshots):
    x = list(map(lambda x: x.time / ecosystem.simulation_config.events_per_second, snapshots))
    y = list(map(lambda x: x.extracted_coffee_mass(ecosystem.config.brew_method), snapshots))
    plt.scatter(x, y)
    plt.show()

def plot_diffusion_vs_initial_and_final_mass_ratios(ecosystem, snapshots):
    sorted_compounds = sorted(snapshots[-1].compounds, key=lambda x: x.diffusion_coefficient)
    # x-values converted to str for nice vis.
    x = list(map(lambda x: str(x.diffusion_coefficient), sorted_compounds))
    total_initial_mass = sum(map(lambda x: x.initial_mass, sorted_compounds))
    total_extracted_mass = snapshots[-1].extracted_coffee_mass(ecosystem.config.brew_method)
    initial_mass_ratios = list(map(lambda x: x.initial_mass / total_initial_mass, sorted_compounds))
    final_mass_ratios = list(map(lambda x: x.extracted_mass(ecosystem.config.brew_method) / total_extracted_mass, sorted_compounds))
    fig, ax = plt.subplots()
    width = 1
    ax.bar(x, initial_mass_ratios, width, label="Initial mass ratio", fill=False, edgecolor="red")
    ax.bar(x, final_mass_ratios, width, label="Final mass ratio", fill=False, edgecolor="green")
    ax.legend()
    plt.show()

def plot_diffusion_vs_mass_ratio_difference(ecosystem, snapshots):
    sorted_compounds = sorted(snapshots[-1].compounds, key=lambda x: x.diffusion_coefficient)
    # x-values converted to str for nice vis.
    x = list(map(lambda x: str(x.diffusion_coefficient), sorted_compounds))
    total_initial_mass = sum(map(lambda x: x.initial_mass, sorted_compounds))
    total_extracted_mass = snapshots[-1].extracted_coffee_mass(ecosystem.config.brew_method)
    mass_ratio_difference = list(
        map(
            lambda x:
                x.extracted_mass(ecosystem.config.brew_method)/ total_extracted_mass
                    - x.initial_mass / total_initial_mass,
            sorted_compounds
        )
    )
    plt.scatter(x, mass_ratio_difference)
    plt.show()

def plot_initial_vs_final_mass_ratios(ecosystem, snapshots):
    total_initial_mass = sum(map(lambda x: x.initial_mass, snapshots[-1].compounds))
    total_extracted_mass = snapshots[-1].extracted_coffee_mass(ecosystem.config.brew_method)
    initial_mass_ratios = list(map(lambda x: x.initial_mass / total_initial_mass, snapshots[-1].compounds))
    final_mass_ratios = list(map(lambda x: x.extracted_mass(ecosystem.config.brew_method) / total_extracted_mass, snapshots[-1].compounds))
    plt.scatter(initial_mass_ratios, final_mass_ratios)
    plt.show()
