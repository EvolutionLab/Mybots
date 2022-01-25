
#adding my first pyfile
#
import pybullet_data
import pybullet as p
import time
physicsClient = p.connect(p.GUI)
#打开或关闭GUI控件，“0”等于关闭
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)

#该语句的作用是禁用tinyrenderer，也就是不让CPU上的集成显卡来参与渲染工作
p.configureDebugVisualizer(p.COV_ENABLE_TINY_RENDERER, 0)


#设置重力，当设置成+10的时候，物体会飘走
#设置重力，当设置成-10的时候，物体会落在地上
#graX, float, gravity force along the X world axis
#graY, float, gravity force along the Y world axis
#graZ, float, gravity force along the Z world axis
p.setGravity(0,0,-10)

#添加资源路径
p.setAdditionalSearchPath(pybullet_data.getDataPath())

#加载URDF模型，此处是加载蓝白相间的陆地
#改变环境的路径C:\Users\win10\anaconda3\Lib\site-packages\pybullet_data
planeId = p.loadURDF("plane100.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

# p.setRealTimeSimulation(1)
# while True:
#     pass

# 开始一千次迭代，也就是一千次交互，每次交互后停顿1/240
# 注释代码和取消注释代码的快捷键都一样
# ctrl + /

for i in range(1000):
    p.setRealTimeSimulation(1)
    time.sleep(1/240)


p.disconnect()