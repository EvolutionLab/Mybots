
#adding my first pyfile
#
import pybullet_data
import pybullet as p
import time


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("box.sdf")


print("Start : %s" % time.ctime())
time.sleep(50)
print("End : %s" % time.ctime())


p.disconnect()