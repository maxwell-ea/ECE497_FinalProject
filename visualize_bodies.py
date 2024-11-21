"""
© 2024 Emily Maxwell <maxwelea@rose-hulman.edu>
SPDX License: BSD-3-Clause

visualize_bodies.py

Last Modified: 11/20/2024
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import body_trial as bt
import simulate_body_gui as sbg


def visualize_trial(trial_number:int):
    filename = f"body_trial_{trial_number}.csv"
    df = pd.read_csv(filename)

    fitness = np.array(df.Fitness)

    plt.plot(fitness)
    plt.xlabel("Generation")
    plt.ylabel("Distance from Start (Fitness)")
    plt.title(f"Fitness over generations in trial {trial_number}")
    plt.show()


def load_simulate_body(trial_number:int):
    filename = f"body_trial_{trial_number}.csv"
    df = pd.read_csv(filename)
    last = np.array(df.loc[1000]['body_w':'legh_4'])

    urdf = bt.generate_urdf(last)
    distance = sbg.simulate_body_gui(urdf)

    return distance


def body_results(trial_number:int):
    visualize_trial(trial_number)
    load_simulate_body(trial_number)
