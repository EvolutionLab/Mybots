

import pyrosim.pyrosim as pyrosim


pyrosim.Start_SDF("box.sdf")

#size: length, width, and height.
pyrosim.Send_Cube(name="Box1", pos=[0,0,0.5] , size=[1,1,1])
pyrosim.Send_Cube(name="Box2", pos=[1,0,1.5] , size=[1,1,1])

pyrosim.End()