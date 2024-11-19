import pybullet as p
import pybullet_data
import pyrosim.pyrosim as ps
import numpy as np
import time
import math
from matplotlib import pyplot as plt


def get_distances(positions):
    distances = [None] * len(positions)

    for i in range(len(positions)):
        position = positions[i]

        distance = math.sqrt((positions[0][0] - position[0]) ** 2 +
                             (positions[0][1] - position[1]) ** 2 +
                             (positions[0][2] - position[2]) ** 2)

        distances[i] = distance

    return distances


# Credit to Inwernos on Stack Overflow for the following code
# Link: https://stackoverflow.com/questions/65987790/how-to-translate-camera-in-pybullet
def move_camera():
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


physicsClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")

robotId_1 = p.loadURDF("body_1.urdf")
robotId_2 = p.loadURDF("body_2.urdf")
robotId_3 = p.loadURDF("body_3.urdf")

duration = 10000

ps.Prepare_To_Simulate(robotId_1)
ps.Prepare_To_Simulate(robotId_2)
ps.Prepare_To_Simulate(robotId_3)

x = np.linspace(0, 0.003 * duration * np.pi, duration)
y_14 = np.sin(x) * np.pi / 4
y_23 = np.cos(x) * np.pi / 4

y2_14 = np.sin(x) * np.pi / 2
y2_23 = np.cos(x) * np.pi / 2

body1_pos = [None] * (duration)
body2_pos = [None] * (duration)
body3_pos = [None] * (duration)

for i in range(duration):
    ps.Set_Motor_For_Joint(bodyIndex=robotId_1,
                           jointName=b'Body_Leg1',
                           controlMode=p.POSITION_CONTROL,
                           targetPosition=y_14[i],
                           maxForce=500)

    ps.Set_Motor_For_Joint(bodyIndex=robotId_1,
                           jointName=b'Body_Leg2',
                           controlMode=p.POSITION_CONTROL,
                           targetPosition=-y_23[i],
                           maxForce=500)

    ps.Set_Motor_For_Joint(bodyIndex=robotId_1,
                           jointName=b'Body_Leg3',
                           controlMode=p.POSITION_CONTROL,
                           targetPosition=-y_23[i],
                           maxForce=500)

    ps.Set_Motor_For_Joint(bodyIndex=robotId_1,
                           jointName=b'Body_Leg4',
                           controlMode=p.POSITION_CONTROL,
                           targetPosition=y_14[i],
                           maxForce=500)

    ps.Set_Motor_For_Joint(bodyIndex=robotId_2,
                           jointName=b'Body_Leg1',
                           controlMode=p.POSITION_CONTROL,
                           targetPosition=y2_14[i],
                           maxForce=500)

    ps.Set_Motor_For_Joint(bodyIndex=robotId_2,
                           jointName=b'Body_Leg2',
                           controlMode=p.POSITION_CONTROL,
                           targetPosition=-y2_23[i],
                           maxForce=500)

    ps.Set_Motor_For_Joint(bodyIndex=robotId_2,
                           jointName=b'Body_Leg3',
                           controlMode=p.POSITION_CONTROL,
                           targetPosition=-y2_23[i],
                           maxForce=500)

    ps.Set_Motor_For_Joint(bodyIndex=robotId_2,
                           jointName=b'Body_Leg4',
                           controlMode=p.POSITION_CONTROL,
                           targetPosition=y2_14[i],
                           maxForce=500)

    ps.Set_Motor_For_Joint(bodyIndex=robotId_3,
                           jointName=b'Body_Leg1',
                           controlMode=p.POSITION_CONTROL,
                           targetPosition=y_14[i],
                           maxForce=500)

    ps.Set_Motor_For_Joint(bodyIndex=robotId_3,
                           jointName=b'Body_Leg2',
                           controlMode=p.POSITION_CONTROL,
                           targetPosition=-y_14[i],
                           maxForce=500)

    ps.Set_Motor_For_Joint(bodyIndex=robotId_3,
                           jointName=b'Body_Leg3',
                           controlMode=p.POSITION_CONTROL,
                           targetPosition=y_14[i],
                           maxForce=500)

    ps.Set_Motor_For_Joint(bodyIndex=robotId_3,
                           jointName=b'Body_Leg4',
                           controlMode=p.POSITION_CONTROL,
                           targetPosition=y_23[i],
                           maxForce=500)

    move_camera()
    p.stepSimulation()

    body1_pos[i] = p.getBasePositionAndOrientation(robotId_1)[0]
    body2_pos[i] = p.getBasePositionAndOrientation(robotId_2)[0]
    body3_pos[i] = p.getBasePositionAndOrientation(robotId_3)[0]

    time.sleep(1 / 500)

p.disconnect()

body1_dist = get_distances(body1_pos)
body2_dist = get_distances(body2_pos)
body3_dist = get_distances(body3_pos)

print(body1_dist)
print(body2_dist)
print(body3_dist)

plt.plot(body1_dist, 'b')
plt.plot(body2_dist, 'r')
plt.plot(body3_dist, 'g')

plt.legend(['Body 1', 'Body 2', 'Body 3'])

plt.xlabel('Time')
plt.ylabel('Distance from Start')
plt.title(f'Distance from Start for Each Body After {duration} Time Steps')

# # Plot of Body 1 Motors
# plt.figure(figsize=(10, 15))
#
# sub1 = plt.subplot(3, 1, 1)
# sub1.plot(y_14, 'b', -y_23, 'r')
# sub1.set_title('Driver Functions')
# plt.xlabel("Time")
# plt.ylabel("Position")
# plt.legend(["Leg 1, Leg 4", "Leg 2, Leg 3"])
#
# sub2 = plt.subplot(3, 1, 2)
# sub2.plot(y_14, 'b')
# sub2.set_title('Driver Function for Legs 1 and 4')
# plt.xlabel("Time")
# plt.ylabel("Position")
#
# sub3 = plt.subplot(3, 1, 3)
# sub3.plot(-y_23, 'r')
# sub3.set_title('Driver Function for Legs 2 and 3')
# plt.xlabel("Time")
# plt.ylabel("Position")
#
# # Plot of Body 2 Motors
# plt.figure(figsize=(10, 15))
#
# sub1 = plt.subplot(3, 1, 1)
# sub1.plot(y2_14, 'b', -y2_23, 'r')
# sub1.set_title('Driver Functions')
# plt.xlabel("Time")
# plt.ylabel("Position")
# plt.legend(["Leg 1, Leg 4", "Leg 2, Leg 3"])
#
# sub2 = plt.subplot(3, 1, 2)
# sub2.plot(y2_14)
# sub2.set_title('Driver Function for Legs 1 and 4')
# plt.xlabel("Time")
# plt.ylabel("Position")
#
# sub3 = plt.subplot(3, 1, 3)
# sub3.plot(-y2_23)
# sub3.set_title('Driver Function for Legs 2 and 3')
# plt.xlabel("Time")
# plt.ylabel("Position")
#
# # Plot of Body 3 Motors
# plt.figure(figsize=(10, 20))
#
# sub1 = plt.subplot(4, 1, 1)
# sub1.plot(y_14, 'b', -y_14, 'r', y_23, 'g')
# sub1.set_title('Driver Functions')
# plt.xlabel("Time")
# plt.ylabel("Position")
# plt.legend(["Leg 1, Leg 3", "Leg 2", "Leg 4"])
#
# sub2 = plt.subplot(4, 1, 2)
# sub2.plot(y_14, 'r')
# sub2.set_title('Driver Function for Legs 1 and 3')
# plt.xlabel("Time")
# plt.ylabel("Position")
#
# sub3 = plt.subplot(4, 1, 3)
# sub3.plot(-y_14, 'b')
# sub3.set_title('Driver Function for Leg 2')
# plt.xlabel("Time")
# plt.ylabel("Position")
#
# sub4 = plt.subplot(4, 1, 4)
# sub4.plot(y_23, 'g')
# sub4.set_title('Driver Function for Leg 4')
# plt.xlabel("Time")
# plt.ylabel("Position")

plt.show()
