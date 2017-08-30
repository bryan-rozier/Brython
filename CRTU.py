########################################################
# General purpose functions for talking to the CRTU-RU
# This currenty only support talking to the CRTU using the 
# Prologix USB<->GPIO interface as the CRTU-RU serial is not responding 
# Probably needs real RS232 voltages -12V / + 12V
#################################################################

import prologixGPIBUSB
from exceptions import IOError

def init():
  prologixGPIBUSB.open_connection()
  mode=prologixGPIBUSB.get_mode()
  if "1" in mode.strip('\r\n'):
    print("PrologixGPIBUSB in command mode")
  addr=prologixGPIBUSB.get_address()
  addr = addr.strip('\r\n')
  addrs = addr.split(' ')
  if addrs[0]=='20':
    print("Primary Address OK")
  else:
    raise IOError("ERROR: PrologixGPIBUSB primary address not set to 20 = %d." &addrs[0])
  if addrs[1]=='97':
    print("Secondary Address OK")
  else:
    raise IOError("ERROR: PrologixGPIBUSB Secondary address not set to 97 = %d." &addrs[1])
  prologixGPIBUSB.write("*IDN?")
  id=prologixGPIBUSB.readline()
  id=id.strip('\r\n')
  #'Rohde&Schwarz,CRTU-RU 1138.4000.82,100091,V5.21\n'
  ids=id.split(',')
  if "Rohde&Schwarz" in ids[0]:
    print ("Manufacturer %s" % ids[0])
    print ("Model %s" % ids[1])
    print ("Serial %s" % ids[2])
    print ("Software Version %s" % ids[3])
  else:
    prologixGPIBUSB.close_connection()
    raise IOError("ERROR: No R&S device connected")
    
#prologixGPIBUSB.write("*IDN?")
#prologixGPIBUSB.readline()
#prologixGPIBUSB.get_address()
#prologixGPIBUSB.get_mode()

def dump_system():
  commands=[
  '0;*ESE?',
  '0;*SEC?',
  '0;*ESR?',
  '0;*IDN?',
  '0;*IST?',
  '0;*OPC?',
  '0;*OPT?',
  '0;*PRE?',
  '0;*PSC?',
  '0;*SRE?',
  '0;*STB?',
  '0;*TST?',
  '0;SYSTem:ERRor?',
  '0;SYSTem:VERSion?',
  '0;SYSTem:MQUeue?',
  '0;SYSTem:MQUeue:COMPlete?',
  '0;SYSTem:MQUeue:COMPlete:LIST?',
  '0;SYSTem:MQUeue:COMPlete:ITEM?',
  '0;SYSTem:OPTions?',
  '0;SYSTem:OPTions:INFO?',
  '0;SYSTem:OPTions:INFO:CURRent?',
  '0;SYSTem:OPTions:NOTKzero?',
  '0;SYSTem:OPTions:MEQuipment?',
  '0;SYSTem:PRINt:SELect?',
  '0;SYSTem:PRINt:PORT?',
  '0;SYSTem:PRINt:RESolution? [ MAXimum | MINimum | DEFault]',
  '0;SYSTem:PRINt:PSIZe?',
  '0;SYSTem:PRINt:BLWHite?',
  '0;SYSTem:PRINt:BLACkwhite?',
  '0;SYSTem:PRINt:HEADer:TEXT?',
  '0;SYSTem:PRINt:HEADer:STATe?',
  '0;SYSTem:PRINt:HEADer:DATetime?',
  '0;SYSTem:PRINt:FNAMe:DEFault?',
  '0;SYSTem:PRINt:LOGO?'
  ]
  for command in commands:
    command=command.split(' ',1) # remove optional chars from command
    prologixGPIBUSB.write(command[0])
    print "%s==%s" % (command[0], prologixGPIBUSB.readline().strip('\r\n'))
  

def reset(): 
    prologixGPIBUSB.write('*RST')
 	      
def close(): 
	prologixGPIBUSB.close_connection()