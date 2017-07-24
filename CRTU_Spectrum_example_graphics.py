import CRTU
import CRTU_Spectrum

from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg

CRTU.init()
CRTU.reset()
CRTU_Spectrum.dump_status()
CRTU_Spectrum.set_frequency(7.930000E+008,1.000000E+007)
CRTU_Spectrum.set_mode_continuous()
CRTU_Spectrum.dump_status()
CRTU_Spectrum.set_init()# also kicks off acquisition
data_points=CRTU_Spectrum.fetch_current()
#print data_points
print len(data_points)
#QtGui.QApplication.setGraphicsSystem('raster')
app = QtGui.QApplication([])
#mw = QtGui.QMainWindow()
#mw.resize(800,800)

win = pg.GraphicsWindow(title="Basic Spectrum example")
win.resize(1000,600)
win.setWindowTitle('Spectrum example: Plotting')

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

#p1 = win.addPlot(title="Maximum Value")

#p1.plot(data_points)

p6 = win.addPlot(title="Current Value")
curve = p6.plot(pen='y')
data = np.random.normal(size=(10,1000))
ptr = 0
def update():
    global curve, data, ptr, p6, data_points
    data_points=CRTU_Spectrum.fetch_current()
    if len(data_points)==560:
    	curve.setData(data_points)
    else:
    	print len(data_points)
#    if ptr == 0:
#        p6.enableAutoRange('xy', False)  ## stop auto-scaling after the first data set is plotted
#    ptr += 1
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(30)


## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
