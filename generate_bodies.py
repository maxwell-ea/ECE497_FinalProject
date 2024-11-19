"""
© 2024 Emily Maxwell <maxwelea@rose-hulman.edu>
SPDX License: BSD-3-Clause

generate_bodies.py

Last Modified: 11/18/2024
"""

import pyrosim.pyrosim as ps
import numpy as np


def generate_bodies(num_bodies, body_dim_limit=(10, 10, 10), leg_dim_limit=(10, 10, 10)):
    bodies = num_bodies
    body_urdfs =[]

    body_w_lim = body_dim_limit[0]
    body_l_lim = leg_dim_limit[1]
    body_h_lim = body_dim_limit[2]

    leg_w_lim = leg_dim_limit[0]
    leg_l_lim = leg_dim_limit[1]
    leg_h_lim = leg_dim_limit[2]

    x = 0
    y = 0
    z = 0

    for i in range(num_bodies):
        body_w = np.random.uniform(0, body_w_lim)
        body_l = np.random.uniform(0, body_l_lim)
        body_h = np.random.uniform(0, body_h_lim)

        leg_w = np.random.uniform(0, leg_w_lim)
        leg_l = np.random.uniform(0, leg_l_lim)
        leg_h = np.random.uniform(0, leg_h_lim)

        body_urdf = f"body_{i}.urdf"
        body_urdfs.append(body_urdf)

        ps.Start_URDF(body_urdf)
        ps.Send_Cube(name="Body", pos=[x, y, z + (leg_h + 0.5*body_h)], size=[body_w, body_l, body_h])  # Body
        ps.Send_Joint(name="Body_Leg1", parent="Body", child="Leg1", type="revolute", position=[x - (0.5*body_w),
                                                                                                y - (0.5*body_l),
                                                                                                z + leg_h])
        ps.Send_Cube(name="Leg1", pos=[-(0.5*leg_w), -0.5*leg_l, -0.5*leg_h], size=[leg_w, leg_l, leg_h])  # Leg1
        ps.End()

    return body_urdfs
