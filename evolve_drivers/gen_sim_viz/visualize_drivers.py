"""
© 2024 Emily Maxwell <maxwelea@rose-hulman.edu>
SPDX License: BSD-3-Clause

visualize_bodies.py

Last Modified: 11/20/2024
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import simulate_body_gui as sbg


def visualize_trial(trial_number: int, body_number: int):

    filename = f"body_{body_number}_drivers/driver_trial_{trial_number}.csv"
    df = pd.read_csv(filename)

    fitness = np.array(df.Fitness)

    plt.plot(fitness)
    plt.xlabel("Generation")
    plt.ylabel("Distance from Start (Fitness)")
    plt.title(f"Fitness over generations in trial {trial_number}")
    plt.show()


def load_simulate_driver(trial_number: int, body_number: int):
    filename = f"body_{body_number}_drivers/driver_trial_{trial_number}.csv"
    df = pd.read_csv(filename)
    amp = list(df.loc[1000]['amp_1':'amp_4'])
    phase = list(df.loc[1000]['phase_1':'phase_4'])

    urdf = f"gen_sim_viz/body_{body_number}.urdf"
    distance = sbg.simulate_body_gui(urdf, amplitude=amp, phase_offset=phase)

    return distance


def driver_results(trial_number: int, body_number: int):
    visualize_trial(trial_number, body_number)
    load_simulate_driver(trial_number, body_number)


def plot_drivers(num_trials: int, body_number: int):
    amp1 = []
    amp2 = []
    amp3 = []
    amp4 = []

    phase1 = []
    phase2 = []
    phase3 = []
    phase4 = []

    for i in range(num_trials):
        filename = f"body_{body_number}_drivers/driver_trial_{i}.csv"
        df = pd.read_csv(filename)
        amp1.append(df.loc[1000]['amp_1'])
        amp2.append(df.loc[1000]['amp_2'])
        amp3.append(df.loc[1000]['amp_3'])
        amp4.append(df.loc[1000]['amp_4'])
        phase1.append(df.loc[1000]['phase_1'])
        phase2.append(df.loc[1000]['phase_2'])
        phase3.append(df.loc[1000]['phase_3'])
        phase4.append(df.loc[1000]['phase_4'])

    duration = 10000
    x = np.linspace(0, 0.003 * duration * np.pi, duration)

    plt.figure(figsize=(15, 9))

    legend_labels = []
    for i in range(len(amp1)):
        plt.plot(amp1[i]*np.sin(x + phase1[i]), lw=1)
        legend_labels.append(f"Trial{i}")

    plt.title("Leg 1 Motor Most Fit")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.legend(legend_labels)

    legend_labels = []
    plt.figure(figsize=(15, 9))
    for i in range(len(amp2)):
        plt.plot(amp2[i]*np.cos(x + phase2[i]), lw = 1)
        legend_labels.append(f"Trial{i}")

    plt.title("Leg 2 Motor Most Fit")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.legend(legend_labels)

    legend_labels = []
    plt.figure(figsize=(15, 9))
    for i in range(len(amp3)):
        plt.plot(amp3[i]*np.cos(x + phase3[i]), lw = 1)
        legend_labels.append(f"Trial{i}")

    plt.title("Leg 3 Motor Most Fit")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.legend(legend_labels)

    legend_labels = []
    plt.figure(figsize=(15, 9))
    for i in range(len(amp4)):
        plt.plot(amp4[i]*np.sin(x + phase4[i]), lw = 1)
        legend_labels.append(f"Trial{i}")

    plt.title("Leg 4 Motor Most Fit")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.legend(legend_labels)

    plt.show()
