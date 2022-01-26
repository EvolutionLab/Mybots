

import pyrosim.pyrosim as pyrosim

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="BackLeg", pos=[0, 0, 0.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="BackLeg_Torso", parent="BackLeg", child="Torso", type="revolute", position=[0.5, 0, 0.5])
    pyrosim.Send_Cube(name="Torso", pos=[0.5, 0, 1.0], size=[1, 1, 1])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0, 0, -0.5])
    pyrosim.Send_Cube(name="FrontLeg", pos=[1.5, 0, 0.5], size=[1, 1, 1])
    pyrosim.End()

Create_Robot()


def Create_box():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="box", pos=[4, 0, 0.5], size=[1, 1, 1])
    pyrosim.End()

Create_box()

