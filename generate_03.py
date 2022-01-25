

import pyrosim.pyrosim as pyrosim

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Link0", pos=[0, 0, 0.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="Link0_Link1", parent="Link0", child="Link1", type="revolute", position=[0.5, 0, 0.5])
    pyrosim.Send_Cube(name="Link1", pos=[0.5, 0, 1.0], size=[1, 1, 1])
    pyrosim.Send_Joint(name="Link1_Link2", parent="Link1", child="Link2", type="revolute", position=[0, 0, -0.5])
    pyrosim.Send_Cube(name="Link2", pos=[1.5, 0, 0.5], size=[1, 1, 1])
    pyrosim.End()

Create_Robot()


def Create_box():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="box", pos=[4, 0, 0.5], size=[1, 1, 1])
    pyrosim.End()

Create_box()

