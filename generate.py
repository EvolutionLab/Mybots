

import pyrosim.pyrosim as pyrosim


pyrosim.Start_SDF("world.sdf")
#pyrosim.Start_URDF("body.urdf")

#size: length, width, and height.
x = 0
y = 0
z = 0.5

length = 1
width = 1
height = 1

Cubes = [1,2,3,4,5,6,7,8,9,10]
for i in range(1, 10, 1):
    pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])
    z = z + 1
    length = length - length*0.10
    width = width - width*0.10
    height = height - height*0.10
#pyrosim.Send_Cube(name="Box", pos=[length,width,height] , size=[1,1,1])
#pyrosim.Send_Cube(name="Box", pos=[length,width,1.5] , size=[1,1,1])


pyrosim.End()