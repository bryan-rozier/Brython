########################################################
# Functions for talking to the CRTU-RU Spectrum Analyzer
# Expects that CRTU.init() has been called
#################################################################
import prologixGPIBUSB
from exceptions import IOError

def dump_status():
  commands=[
  '1;SENSe:SPECtrum:FREQuency:STARt <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ]  | MAXimum | MINimum | DEFault',
  '1;SENSe:SPECtrum:FREQuency:STARt? [ MAXimum | MINimum | DEFault]',
  '1;SENSe:SPECtrum:FREQuency:SPAN <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ]  | MAXimum | MINimum | DEFault',
  '1;SENSe:SPECtrum:FREQuency:SPAN? [ MAXimum | MINimum | DEFault]',
  '1;SENSe:SPECtrum:FREQuency:STOP <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ]  | MAXimum | MINimum | DEFault',
  '1;SENSe:SPECtrum:FREQuency:STOP? [ MAXimum | MINimum | DEFault]',
  '1;SENSe:SPECtrum:FREQuency:CENTer <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ]  | MAXimum | MINimum | DEFault',
  '1;SENSe:SPECtrum:FREQuency:CENTer? [ MAXimum | MINimum | DEFault]',
  '1;SENSe:SPECtrum:FREQuency:BANDwidth <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ]  | MAXimum | MINimum | DEFault | AUTO',
  '1;SENSe:SPECtrum:FREQuency:BANDwidth? [ MAXimum | MINimum | DEFault]',
  '1;SENSe:SPECtrum:FREQuency:BANDwidth:RESolution <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ]  | MAXimum | MINimum | DEFault | AUTO',
  '1;SENSe:SPECtrum:FREQuency:BANDwidth:RESolution? [ MAXimum | MINimum | DEFault]',
  '1;SENSe:SPECtrum:FREQuency:BWIDth <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ]  | MAXimum | MINimum | DEFault | AUTO',
  '1;SENSe:SPECtrum:FREQuency:BWIDth? [ MAXimum | MINimum | DEFault]',
  '1;SENSe:SPECtrum:FREQuency:BWIDth:RESolution <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ]  | MAXimum | MINimum | DEFault | AUTO',
  '1;SENSe:SPECtrum:FREQuency:BWIDth:RESolution? [ MAXimum | MINimum | DEFault]',
  '1;SENSe:SPECtrum:LEVel:RANGe <numeric> [ DB | PO | PC | PM | PPM ]  | MAXimum | MINimum | DEFault',
  '1;SENSe:SPECtrum:LEVel:RANGe? [ MAXimum | MINimum | DEFault]',
  '1;SENSe:SPECtrum:DETector MAXimum | MINimum | DEFault | PEAK | RMS',
  '1;SENSe:SPECtrum:DETector? [ MAXimum | MINimum | DEFault]',
  '1;CONFigure:ARRay:SPECtrum:RANGe <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ]  | MAXimum | MINimum | DEFault, <numeric>  | MAXimum | MINimum | DEFault',
  '1;CONFigure:ARRay:SPECtrum:RANGe? [ MAXimum | MINimum | DEFault, MAXimum | MINimum | DEFault]',
  '1;CONFigure:SUBarrays:SPECtrum ALL | ARIThmetical | MINimum | MAXimum | IVALue | XMINimum | XMAXimum | PAVG, <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ] , <numeric> , [ <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ] , <numeric> , [ <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ] , <numeric> , [ <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ] , <numeric> , [ <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ] , <numeric> , [ <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ] , <numeric> , [ <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ] , <numeric> , [ <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ] , <numeric> , [ <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ] , <numeric> , [ <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ] , <numeric> , [ <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ] , <numeric> , [ <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ] , <numeric> , [ <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ] , <numeric> , [ <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ] , <numeric> , [ <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ] , <numeric> , [ <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ] , <numeric> , [ <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ] , <numeric> , [ <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ] , <numeric> , [ <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ] , <numeric> , [ <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ] , <numeric> , [ <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ] , <numeric> , [ <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ] , <numeric> , [ <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ] , <numeric> , [ <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ] , <numeric> , [ <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ] , <numeric> , ]]]]]]]]]]]]]]]]]]]]]]]]',
  '1;CONFigure:SUBarrays:SPECtrum?',
  '1;CONFigure:SPECtrum:EREPorting DEFault | SRQ | SOPC | SRSQ | OFF',
  '1;CONFigure:SPECtrum:EREPorting? [ DEFault]',
  '1;CONFigure:SPECtrum:CONTrol DEFault | SCALar | ARRay, <numeric>  | DEFault | MINimum | MAXimum | NONE',
  '1;CONFigure:SPECtrum:CONTrol? [ DEFault, DEFault | MINimum | MAXimum]',
  '1;CONFigure:SPECtrum:CONTrol:REPetition <numeric>  | DEFault | CONTinuous | SINGleshot, DEFault | NONE | SONerror, DEFault | NONE | STEP',
  '1;CONFigure:SPECtrum:CONTrol:REPetition? [ DEFault, DEFault, DEFault]',
  '1;CONFigure:SPECtrum:CONTrol:MODE DEFault | CUR | AVG | MIN | MAX',
  '1;CONFigure:SPECtrum:CONTrol:MODE? [ DEFault]',
  '1;INITiate:SPECtrum',
  '1;STOP:SPECtrum',
  '1;CONTinue:SPECtrum',
  '1;ABORt:SPECtrum',
## remove these commands as they are the reading data.
## READ -> Single Shot
## FETCH -> Read measured results (Unsyncronized)
## SAMPLE -> Read Results Synchronised
#  '1;FETCh:ARRay:SPECtrum?',
#  '1;FETCh:ARRay:SPECtrum:RESult?',
#  '1;FETCh:ARRay:SPECtrum:RESult:CURRent?',
#  '1;FETCh:ARRay:SPECtrum:RESult:AVERage?',
#  '1;FETCh:ARRay:SPECtrum:RESult:MINimum?',
#  '1;FETCh:ARRay:SPECtrum:RESult:MAXimum?',
#  '1;FETCh:SUBarrays:SPECtrum?',
#  '1;FETCh:SUBarrays:SPECtrum:RESult?',
#  '1;FETCh:SUBarrays:SPECtrum:RESult:CURRent?',
#  '1;FETCh:SUBarrays:SPECtrum:RESult:AVERage?',
#  '1;FETCh:SUBarrays:SPECtrum:RESult:MAXimum?',
#  '1;FETCh:SUBarrays:SPECtrum:RESult:MINimum?',
#  '1;FETCh:SPECtrum:STATus?',
#  '1;FETCh:SPECtrum:MARKer:ABSolute? <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ] ',
#  '1;FETCh:SPECtrum:MARKer:RELative? <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ] , <numeric> [ HZ | AHZ | FHZ | PHZ | NHZ | UHZ | MIHZ | KHZ | MHZ | GHZ | THZ | PEHZ | EXHZ ] ',
#  '1;FETCh:SPECtrum:MARKer:PEAK?',
  '1;WAIT:SPECtrum:STATus?',
  '1;DEFault:SPECtrum:CONTrol DEFault | ON',
  '1;DEFault:SPECtrum:CONTrol? [ DEFault]',
#  '1;READ:ARRay:SPECtrum?',
#  '1;READ:ARRay:SPECtrum:RESult?',
#  '1;READ:ARRay:SPECtrum:RESult:CURRent?',
#  '1;READ:ARRay:SPECtrum:RESult:AVERage?',
#  '1;READ:ARRay:SPECtrum:RESult:MINimum?',
#  '1;READ:ARRay:SPECtrum:RESult:MAXimum?',
#  '1;READ:SUBarrays:SPECtrum?',
#  '1;READ:SUBarrays:SPECtrum:RESult?',
#  '1;READ:SUBarrays:SPECtrum:RESult:CURRent?',
#  '1;READ:SUBarrays:SPECtrum:RESult:AVERage?',
#  '1;READ:SUBarrays:SPECtrum:RESult:MAXimum?',
#  '1;READ:SUBarrays:SPECtrum:RESult:MINimum?',
#  '1;SAMPle:ARRay:SPECtrum?',
#  '1;SAMPle:ARRay:SPECtrum:RESult?',
#  '1;SAMPle:ARRay:SPECtrum:RESult:CURRent?',
#  '1;SAMPle:ARRay:SPECtrum:RESult:AVERage?',
#  '1;SAMPle:ARRay:SPECtrum:RESult:MINimum?',
#  '1;SAMPle:ARRay:SPECtrum:RESult:MAXimum?',
#  '1;SAMPle:SUBarrays:SPECtrum?',
#  '1;SAMPle:SUBarrays:SPECtrum:RESult?',
#  '1;SAMPle:SUBarrays:SPECtrum:RESult:CURRent?',
#  '1;SAMPle:SUBarrays:SPECtrum:RESult:AVERage?',
#  '1;SAMPle:SUBarrays:SPECtrum:RESult:MAXimum?',
#  '1;SAMPle:SUBarrays:SPECtrum:RESult:MINimum?',
  '1;DISPlay:SPECtrum:CONTrol:GRID DEFault | ON | OFF',
  '1;DISPlay:SPECtrum:CONTrol:GRID? [ DEFault]'
  ]
  for command in commands:
  	if '?' in command: # only send status requests
	    command=command.split(' ',1) # remove optional chars from command
	    prologixGPIBUSB.write(command[0])
	    print "%s==%s" % (command[0], prologixGPIBUSB.readline().strip('\r\n'))

def set_frequency(centre, span):
	prologixGPIBUSB.write("1;SENSe:SPECtrum:FREQuency:CENTer %d HZ\r\n" % centre)
	prologixGPIBUSB.write("1;SENSe:SPECtrum:FREQuency:SPAN %d HZ\r\n" % span)

def fetch_max ():
	prologixGPIBUSB.write('1;FETCh:ARRay:SPECtrum:RESult:MAXimum?')
	data = prologixGPIBUSB.readline().strip('\r\n')
	return data