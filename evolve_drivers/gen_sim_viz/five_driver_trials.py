"""
© 2024 Emily Maxwell <maxwelea@rose-hulman.edu>
SPDX License: BSD-3-Clause

five_driver_trials.py

Last Modified: 11/20/2024
"""

import driver_trial as dt

num_drivers = 20
body_num = 2
generations = 1000
trials = 5

for i in range(trials):
    print(f"Starting trial {i}")

    final_state = dt.driver_trial(num_drivers, 1, generations, f"{i}")

    print(f"Finished trial {i}")

print("Evolve Driver Trials Complete")
