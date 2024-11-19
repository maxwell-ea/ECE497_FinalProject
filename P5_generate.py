import pyrosim.pyrosim as ps

# Body 1 Starting Position
x = 0
y = -5
z = 0

# Body 2 Starting Position
x2 = -20
y2 = 0
z2 = 0

# Body 3 Starting Position
x3 = 0
y3 = 5
z3 = 0


def Create_Body1():
    ps.Start_URDF("body_1.urdf")
    ps.Send_Cube(name="Body",pos=[x, y, z + 1.5],size=[2, 2, 1])    # Body

    ps.Send_Joint(name="Body_Leg1", parent="Body", child="Leg1", type="revolute", position=[x + -1, y + -1, z + 1])
    ps.Send_Cube(name="Leg1",pos=[-0.25, -0.25, -0.5],size=[0.5, 0.5, 1]) # Leg1

    ps.Send_Joint(name="Body_Leg2", parent="Body", child="Leg2", type="revolute", position=[x + 1, y + -1, z + 1])
    ps.Send_Cube(name="Leg2", pos=[0.25, -0.25, -0.5], size=[0.5, 0.5, 1])  # Leg2

    ps.Send_Joint(name="Body_Leg3", parent="Body", child="Leg3", type="revolute", position=[x + 1, y + 1, z + 1])
    ps.Send_Cube(name="Leg3", pos=[0.25, 0.25, -0.5], size=[0.5, 0.5, 1])  # Leg3

    ps.Send_Joint(name="Body_Leg4", parent="Body", child="Leg4", type="revolute", position=[x + -1, y + 1, z + 1])
    ps.Send_Cube(name="Leg4", pos=[-0.25, 0.25, -0.5], size=[0.5, 0.5, 1])  # Leg4
    ps.End()


def Create_Body2():
    ps.Start_URDF("body_2.urdf")
    ps.Send_Cube(name="Body",pos=[x2, y2, z2 + 2.5],size=[2, 2, 1])    # Body

    ps.Send_Joint(name="Body_Leg1", parent="Body", child="Leg1", type="revolute", position=[x2 + -1, y2 + -1, z2 + 2])
    ps.Send_Cube(name="Leg1",pos=[-0.25, -0.25, -1],size=[0.5, 0.5, 2]) # Leg1

    ps.Send_Joint(name="Body_Leg2", parent="Body", child="Leg2", type="revolute", position=[x2 + 1, y2 + -1, z2 + 2])
    ps.Send_Cube(name="Leg2", pos=[0.25, -0.25, -1], size=[0.5, 0.5, 2])  # Leg2

    ps.Send_Joint(name="Body_Leg3", parent="Body", child="Leg3", type="revolute", position=[x2 + 1, y2 + 1, z2 + 2])
    ps.Send_Cube(name="Leg3", pos=[0.25, 0.25, -1], size=[0.5, 0.5, 2])  # Leg3

    ps.Send_Joint(name="Body_Leg4", parent="Body", child="Leg4", type="revolute", position=[x2 + -1, y2 + 1, z2 + 2])
    ps.Send_Cube(name="Leg4", pos=[-0.25, 0.25, -1], size=[0.5, 0.5, 2])  # Leg4
    ps.End()


def Create_Body3():
    ps.Start_URDF("body_3.urdf")
    ps.Send_Cube(name="Body",pos=[x3, y3, z3 + 1.5],size=[2, 2, 1])    # Body

    ps.Send_Joint(name="Body_Leg1", parent="Body", child="Leg1", type="revolute", position=[x3, y3 + -1, z3 + 1])
    ps.Send_Cube(name="Leg1",pos=[0, -0.25, -0.5],size=[1, 0.5, 1]) # Leg1

    ps.Send_Joint(name="Body_Leg2", parent="Body", child="Leg2", type="revolute", position=[x3 + 1, y3, z3 + 1])
    ps.Send_Cube(name="Leg2", pos=[0.25, 0, -0.5], size=[0.5, 1, 1])  # Leg2

    ps.Send_Joint(name="Body_Leg3", parent="Body", child="Leg3", type="revolute", position=[x3, y3 + 1, z3 + 1])
    ps.Send_Cube(name="Leg3", pos=[0, 0.25, -0.5], size=[1, 0.5, 1])  # Leg3

    ps.Send_Joint(name="Body_Leg4", parent="Body", child="Leg4", type="revolute", position=[x3 + -1, y3, z3 + 1])
    ps.Send_Cube(name="Leg4", pos=[-0.25, 0, -0.5], size=[0.5, 1, 1])  # Leg4
    ps.End()


Create_Body1()
Create_Body2()
Create_Body3()
