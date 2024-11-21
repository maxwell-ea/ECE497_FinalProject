"""
© 2024 Emily Maxwell <maxwelea@rose-hulman.edu>
SPDX License: BSD-3-Clause

ten_body_trials.py

Last Modified: 11/20/2024
"""

import body_trial as bt

num_bodies = 20
generations = 1000
trials = 3

for i in range(trials):
    actual_trial = i + 7
    print("Starting trial {}".format(actual_trial))

    final_state = bt.body_trial(num_bodies, generations, f"{actual_trial}")

    print("Finished trial {}".format(actual_trial))

print("Evolve Body Trials Complete")
