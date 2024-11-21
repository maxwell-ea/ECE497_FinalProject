"""
© 2024 Emily Maxwell <maxwelea@rose-hulman.edu>
SPDX License: BSD-3-Clause

simulate_body_nogui.py

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
    if keys.get(108):  #L
        xyz = cam[11]
        x = float(xyz[0]) + 0.125
        y = xyz[1]
        z = xyz[2]
        p.resetDebugVisualizerCamera(cameraYaw=cam[8], cameraPitch=cam[9], cameraDistance=cam[10],
                                     cameraTargetPosition=[x, y, z])
    if keys.get(106):  #J
        xyz = cam[11]
        x = float(xyz[0]) - 0.125
        y = xyz[1]
        z = xyz[2]
        p.resetDebugVisualizerCamera(cameraYaw=cam[8], cameraPitch=cam[9], cameraDistance=cam[10],
                                     cameraTargetPosition=[x, y, z])
    if keys.get(105):  #I
        xyz = cam[11]
        x = xyz[0]
        y = float(xyz[1]) + 0.125
        z = xyz[2]
        p.resetDebugVisualizerCamera(cameraYaw=cam[8], cameraPitch=cam[9], cameraDistance=cam[10],
                                     cameraTargetPosition=[x, y, z])
    if keys.get(107):  #K
        xyz = cam[11]
        x = xyz[0]
        y = float(xyz[1]) - 0.125
        z = xyz[2]
        p.resetDebugVisualizerCamera(cameraYaw=cam[8], cameraPitch=cam[9], cameraDistance=cam[10],
                                     cameraTargetPosition=[x, y, z])


def get_distances(positions):
    distances = [None] * len(positions)

    for i in range(len(positions)):
        position = positions[i]

        distance = math.sqrt((positions[0][0] - position[0]) ** 2 +
                             (positions[0][1] - position[1]) ** 2 +
                             (positions[0][2] - position[2]) ** 2)

        distances[i] = distance

    return distances


def simulate_body(body:str, duration=10000, amplitude=(1, -1, -1, 1), phase_offset=(0, 0, 0, 0)):
    # Configuration

    # For GUI version
    # p.connect(p.GUI)
    # p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)

    # For no GUI version (much faster)
    p.connect(p.DIRECT)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0, 0, -9.8)

    # Load plane and robot body
    p.loadURDF("plane.urdf")
    robot_id = p.loadURDF(body)

    # Prepare body for simulation
    ps.Prepare_To_Simulate(robot_id)
    body_pos = [None] * duration

    # Prepare driver functions for motors
    x = np.linspace(0, 0.003 * duration * np.pi, duration)
    y_1 = amplitude[0] * np.sin(x + phase_offset[0])
    y_2 = amplitude[1] * np.cos(x + phase_offset[1])
    y_3 = amplitude[2] * np.cos(x + phase_offset[2])
    y_4 = amplitude[3] * np.sin(x + phase_offset[3])

    # Progress Measuring Setup
    ten_percent = duration//10
    percent_complete = 0

    # Begin simulation loop
    # print(f"Starting Simulation of {body}...")
    for i in range(duration):

        # Set position of Leg 1
        ps.Set_Motor_For_Joint(bodyIndex=robot_id,
                               jointName=b'Body_Leg1',
                               controlMode=p.POSITION_CONTROL,
                               targetPosition=y_1[i],
                               maxForce=500)

        # Set position of Leg 2
        ps.Set_Motor_For_Joint(bodyIndex=robot_id,
                               jointName=b'Body_Leg2',
                               controlMode=p.POSITION_CONTROL,
                               targetPosition=y_2[i],
                               maxForce=500)

        # Set position of Leg 3
        ps.Set_Motor_For_Joint(bodyIndex=robot_id,
                               jointName=b'Body_Leg3',
                               controlMode=p.POSITION_CONTROL,
                               targetPosition=y_3[i],
                               maxForce=500)

        # Set position of Leg 4
        ps.Set_Motor_For_Joint(bodyIndex=robot_id,
                               jointName=b'Body_Leg4',
                               controlMode=p.POSITION_CONTROL,
                               targetPosition=y_4[i],
                               maxForce=500)

        # Uncomment when using GUI to move camera
        # move_camera()

        # Next step in simulation
        p.stepSimulation()

        # Record current position of body's center
        body_pos[i] = p.getBasePositionAndOrientation(robot_id)[0]

        # Uncomment for print out
        # if i % ten_percent == 0:
        #     percent_complete += 10
        #     print(f"{percent_complete}% Complete")

        # Uncomment when using GUI for visualization
        # time.sleep(1 / 500)

    p.disconnect()

    # print("Simulation Complete")

    body_dist = get_distances(body_pos)
    # print(f"Final Distance: {body_dist[-1]}")
    #
    # plt.plot(body_dist, 'b')
    #
    # plt.title("Distance between Body and Starting Position")
    # plt.xlabel('Time')
    # plt.ylabel('Distance')
    #
    # plt.show()

    return body_dist
