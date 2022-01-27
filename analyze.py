import matplotlib.pyplot
import numpy

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")

#同时绘制backLegSensorValues，frontLegSensorValues
matplotlib.pyplot.plot(backLegSensorValues, linewidth=2)
matplotlib.pyplot.plot(frontLegSensorValues,linewidth=2)

matplotlib.pyplot.legend(('BackLeg', 'FrontLeg'), loc='upper right')

matplotlib.pyplot.show()
