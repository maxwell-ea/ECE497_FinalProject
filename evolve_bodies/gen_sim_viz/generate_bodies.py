"""
© 2024 Emily Maxwell <maxwelea@rose-hulman.edu>
SPDX License: BSD-3-Clause

generate_bodies.py

Last Modified: 11/18/2024
"""

import pyrosim.pyrosim as ps
import numpy as np


def generate_bodies(num_bodies, body_dim_limit=(5, 5, 5), leg_dim_limit=(5, 5, 5)):
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

        leg_w = np.random.uniform(0, leg_w_lim, 4)
        leg_l = np.random.uniform(0, leg_l_lim, 4)
        leg_h = np.random.uniform(0, leg_h_lim, 4)

        print(leg_w, leg_l, leg_h)

        body_urdf = f"body_{i}.urdf"
        body_urdfs.append(body_urdf)

        ps.Start_URDF(body_urdf)
        ps.Send_Cube(name="Body", pos=[x, y, z + (max(leg_h) + 0.5*body_h)], size=[body_w, body_l, body_h])  # Body

        # Joint 1, Leg 1
        ps.Send_Joint(name="Body_Leg1", parent="Body", child="Leg1", type="revolute", position=[x - (0.5*body_w),
                                                                                                y - (0.5*body_l),
                                                                                                z + max(leg_h)])
        ps.Send_Cube(name="Leg1", pos=[-(0.5*leg_w[0]), -0.5*leg_l[0], -0.5*leg_h[0]],
                     size=[leg_w[0], leg_l[0], leg_h[0]])  # Leg1

        # Joint 2, Leg 2
        ps.Send_Joint(name="Body_Leg2", parent="Body", child="Leg2", type="revolute", position=[x + (0.5 * body_w),
                                                                                                y - (0.5 * body_l),
                                                                                                z + max(leg_h)])
        ps.Send_Cube(name="Leg2", pos=[(0.5 * leg_w[1]), -0.5 * leg_l[1], -0.5 * leg_h[1]],
                     size=[leg_w[1], leg_l[1], leg_h[1]])  # Leg2

        # Joint 3, Leg 3
        ps.Send_Joint(name="Body_Leg3", parent="Body", child="Leg3", type="revolute", position=[x + (0.5 * body_w),
                                                                                                y + (0.5 * body_l),
                                                                                                z + max(leg_h)])
        ps.Send_Cube(name="Leg3", pos=[(0.5 * leg_w[2]), 0.5 * leg_l[2], -0.5 * leg_h[2]],
                     size=[leg_w[2], leg_l[2], leg_h[2]])  # Leg3

        # Joint 4, Leg 4
        ps.Send_Joint(name="Body_Leg4", parent="Body", child="Leg4", type="revolute", position=[x - (0.5 * body_w),
                                                                                                y + (0.5 * body_l),
                                                                                                z + max(leg_h)])
        ps.Send_Cube(name="Leg4", pos=[-(0.5 * leg_w[3]), 0.5 * leg_l[3], -0.5 * leg_h[3]],
                     size=[leg_w[3], leg_l[3], leg_h[3]])  # Leg4

        ps.End()

    return body_urdfs
