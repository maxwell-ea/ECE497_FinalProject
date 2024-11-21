"""
© 2024 Emily Maxwell <maxwelea@rose-hulman.edu>
SPDX License: BSD-3-Clause

evolve_bodies.py

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

    bodies = str(final_state[0])
    bodies_file = open("bodies.txt", "w")
    bodies_file.write(bodies)
    bodies_file.write("\n")
    bodies_file.close()

    fitness = str(final_state[1])
    fitness_file = open("fitness.txt", "w")
    fitness_file.write(fitness)
    fitness_file.write("\n")
    fitness_file.close()

    print("Finished trial {}".format(actual_trial))

print("Evolve Body Trials Complete")
