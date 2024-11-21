"""
© 2024 Emily Maxwell <maxwelea@rose-hulman.edu>
SPDX License: BSD-3-Clause

evolve_drivers_results.py

Last Modified: 11/21/2024
"""

from gen_sim_viz import visualize_drivers as vd

number_of_trials = 5
trial_number = 0
body_number = 2

# Uncomment for simulation of a single trial and body
vd.driver_results(trial_number, body_number)

# Uncomment for plotting best drivers for all trials for each leg motor
#vd.plot_drivers(number_of_trials, body_number)
