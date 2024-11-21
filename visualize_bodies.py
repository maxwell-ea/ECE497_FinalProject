"""
© 2024 Emily Maxwell <maxwelea@rose-hulman.edu>
SPDX License: BSD-3-Clause

visualize_bodies.py

Last Modified: 11/20/2024
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def visualize_trial(trial_number:int):
    filename = f"body_trial_{trial_number}.csv"
    df = pd.read_csv(filename)

    fitness = np.array(df.Fitness)

    plt.plot(fitness)
    plt.show()


for i in range(10):
    visualize_trial(i)
