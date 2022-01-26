import matplotlib.pyplot
import numpy

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")


matplotlib.pyplot.plot(backLegSensorValues)
matplotlib.pyplot.show()
