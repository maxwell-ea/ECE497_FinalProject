"""
© 2024 Emily Maxwell <maxwelea@rose-hulman.edu>
SPDX License: BSD-3-Clause

test_trial.py

Last Modified: 11/18/2024
"""

import generate_bodies as gb
import simulate_body as sb

num_bodies = 1

body_urdfs = gb.generate_bodies(num_bodies)
sb.simulate_body(body_urdfs[0])