
#adding my first pyfile

import pybullet as p
import time

physicsClient = p.connect(p.GUI)

print("Start : %s" % time.ctime())
time.sleep(50)
print("End : %s" % time.ctime())


p.disconnect()

