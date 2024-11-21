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
trials = 1

for i in range(trials):
    print(f"Starting trial {i+4}")

    final_state = dt.driver_trial(num_drivers, body_num, generations, f"{i+4}")

    print(f"Finished trial {i+4}")

print("Evolve Driver Trials Complete")
