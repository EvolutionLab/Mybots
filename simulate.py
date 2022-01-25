
#adding my first pyfile
#
import pybullet_data
import pybullet as p
import time
physicsClient = p.connect(p.GUI)

p.setGravity(0,0,-9.8)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

planeId = p.loadURDF("plane.urdf")
#p.loadSDF("box.sdf")
p.loadSDF("world.sdf")

for i in range(1000):
    p.stepSimulation()
    time.sleep(1/60)


p.disconnect()