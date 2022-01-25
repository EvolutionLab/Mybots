
#adding my first pyfile
#
import pybullet_data
import pybullet as p
import time
physicsClient = p.connect(p.GUI)
#打开或关闭GUI控件，“0”等于关闭
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 1)

#该语句的作用是禁用tinyrenderer，也就是不让CPU上的集成显卡来参与渲染工作
p.configureDebugVisualizer(p.COV_ENABLE_TINY_RENDERER, 0)



p.setGravity(0,0,-9.8)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

planeId = p.loadURDF("plane.urdf")
#p.loadSDF("box.sdf")
p.loadSDF("world.sdf")

for i in range(1000):
    p.stepSimulation()
    time.sleep(1/60)


p.disconnect()