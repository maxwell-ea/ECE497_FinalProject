"""
© 2024 Emily Maxwell <maxwelea@rose-hulman.edu>
SPDX License: BSD-3-Clause

evolve_bodies.py

Last Modified: 11/20/2024

Distribution Statement: 
"""

import body_trial as bt

num_bodies = 5
generations = 10
title = "test"

final_state = bt.body_trial(num_bodies, generations, title)

bodies = str(final_state[0])
bodies_file = open("bodies.txt", "w")
bodies_file.write(bodies)
bodies_file.write("\n")
bodies_file.close()

fitness = str(final_state[1])
fitness_file = open("fitness.txt", "w")
fitness_file.write(bodies)
fitness_file.write("\n")
fitness_file.close()
