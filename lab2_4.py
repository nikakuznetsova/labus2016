__author__ = 'student'
import math
import pylab
from matplotlib import mlab

gmin = -20.0
gmax = 20.0
dg = 0.01
glist = mlab.frange (gmin, gmax, dg)

a=0

pylab.ion()

for t in range (50):
          xlist = [math.sin (t + a) for x in glist]
          ylist = [math.cos(2*t) for y in glist]
pylab.clf()
pylab.plot (xlist, ylist)

pylab.draw()
a +=0.5
pylab.pause(0.3)



pylab.close()