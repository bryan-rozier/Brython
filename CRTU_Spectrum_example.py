import CRTU
import CRTU_Spectrum

def init():
  CRTU.init()
  CRTU.reset()
  CRTU_Spectrum.dump_status()
  CRTU_Spectrum.set_frequency(7.930000E+008,1.000000E+007)
  CRTU_Spectrum.dump_status()
  data=CRTU_Spectrum.fetch_max()
  data_points=data.split(',')
  for x in data_points:
    print "%s" % (x)
  CRTU.close()
