"""
© 2024 Emily Maxwell <maxwelea@rose-hulman.edu>
SPDX License: BSD-3-Clause

body_trial.py

Last Modified: 11/18/2024
"""

import simulate_body_nogui as sb
from genalgs import Microbial

import numpy as np
import pandas as pd

# Limit for amplitude
amp_lim = 2


def randomize_params():
    amps = np.random.uniform(-amp_lim, amp_lim, size=4)
    params = [amps[0], amps[1], amps[2], amps[3]]
    params.extend(np.random.uniform(-2*np.pi, 2*np.pi, size=4))

    return params


def randomize_drivers(num_drivers: int):
    all_drivers = []
    for i in range(num_drivers):
        all_drivers.append(randomize_params())

    return all_drivers


def driver_trial(num_drivers: int, body_num: int, generations: int, title: str, prob_reproduction = 0.8,
                 prob_mutation = 0.1, mutation_deviation = 0.05, encoding_type = 1, minimise = False):

    # Generate amplitudes and phase offsets
    drivers = randomize_drivers(num_drivers)
    body = f"body_{body_num}.urdf"

    # Find the fitness for each driver for the chosen body (final distance from starting point)
    fitness = []
    for i in range(len(drivers)):
        distance = sb.simulate_body(body, amplitude=drivers[i][0:4], phase_offset=drivers[i][4:8])
        fitness.append(distance[-1])

    ga = Microbial(drivers, fitness, prob_reproduction, prob_mutation, mutation_deviation, encoding_type, minimise)

    # Create pandas dataframe to info related to fitness
    columns = ('Generation', 'Fitness', 'amp_1', 'amp_2', 'amp_3', 'amp_4', 'phase_1', 'phase_2', 'phase_3', 'phase_4')

    error = (None, None)
    most_fit = ga.getMostFit()

    while most_fit == error:
        most_fit = ga.getMostFit()

    data = [0, most_fit[1]]
    data.extend(most_fit[0])

    df = pd.DataFrame(columns=columns)
    df.loc[0] = data

    # Generational loop for genetic algorithm
    for i in range(generations):
        output = ga.cycle()
        print(f"Generation {i+1} of {generations}")

        drivers = output[0]
        individual = output[1]

        fitness[individual] = sb.simulate_body(body, amplitude=drivers[individual][0:4],
                                               phase_offset=drivers[individual][4:8])[-1]

        ga.setFitness(fitness)

        # Add most fit member of the population to dataframe
        most_fit = ga.getMostFit()
        new_data = [i+1, most_fit[1]]
        new_data.extend(most_fit[0])
        df.loc[len(df.index)] = new_data

    # Set the generation as the index in the datafram
    df.set_index('Generation', inplace=True)
    print(df)

    # Print best fitness and most fit body
    best_body = ga.getMostFit()
    print(f"Best Fitness: {best_body[1]}, Body: {best_body[0]}")

    df.to_csv(f'body_2_drivers/driver_trial_{title}.csv')

    return drivers, fitness
