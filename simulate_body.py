"""
© 2024 Emily Maxwell <maxwelea@rose-hulman.edu>
SPDX License: BSD-3-Clause

simulate_body.py

Last Modified: 11/18/2024
"""
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as ps
import numpy as np
import time
import math
from matplotlib import pyplot as plt


def move_camera():
    """
    Credit to Inwernos on Stack Overflow for the following code
    Link: https://stackoverflow.com/questions/65987790/how-to-translate-camera-in-pybullet
    """

    keys = p.getKeyboardEvents()
    cam = p.getDebugVisualizerCamera()

    #Keys to change camera
    if keys.get(100):  #D
        xyz = cam[11]
        x = float(xyz[0]) + 0.125
        y = xyz[1]
        z = xyz[2]
        p.resetDebugVisualizerCamera(cameraYaw=cam[8], cameraPitch=cam[9], cameraDistance=cam[10],
                                     cameraTargetPosition=[x, y, z])
    if keys.get(97):  #Ad
        xyz = cam[11]
        x = float(xyz[0]) - 0.125
        y = xyz[1]
        z = xyz[2]
        p.resetDebugVisualizerCamera(cameraYaw=cam[8], cameraPitch=cam[9], cameraDistance=cam[10],
                                     cameraTargetPosition=[x, y, z])
    if keys.get(99):  #C
        xyz = cam[11]
        x = xyz[0]
        y = float(xyz[1]) + 0.125
        z = xyz[2]
        p.resetDebugVisualizerCamera(cameraYaw=cam[8], cameraPitch=cam[9], cameraDistance=cam[10],
                                     cameraTargetPosition=[x, y, z])
    if keys.get(102):  #F
        xyz = cam[11]
        x = xyz[0]
        y = float(xyz[1]) - 0.125
        z = xyz[2]
        p.resetDebugVisualizerCamera(cameraYaw=cam[8], cameraPitch=cam[9], cameraDistance=cam[10],
                                     cameraTargetPosition=[x, y, z])


def simulate_body(body:str, duration = 10000):
    # Configuration
    p.connect(p.GUI)
    p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0, 0, -9.8)

    # Load plane and robot body
    p.loadURDF("plane.urdf")
    robot_ID = p.loadURDF(body)

    # Prepare body for simulation
    ps.Prepare_To_Simulate(robot_ID)

    for i in range(duration):
        move_camera()
        p.stepSimulation()
        time.sleep(1 / 500)

    p.disconnect()