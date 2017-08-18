import sys
sys.path.append("C:\Brython")
print sys.path

import prologixGPIBUSB

prologixGPIBUSB.open_connection()
prologixGPIBUSB.write("*IDN?")
prologixGPIBUSB.readline()
prologixGPIBUSB.get_address()
prologixGPIBUSB.get_mode()
