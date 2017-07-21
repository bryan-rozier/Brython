# Copyright 2010 Jim Bridgewater

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# 12/28/10 Jim Bridgewater
# Changed module to remember port number where Prologix device
# was last found, but still searches other ports in case it
# moved to a different port (e.g. by unplugging and reconnecting)

# 06/2/10 Jim Bridgewater
# New module to manage the Prologix GPIB/USB interface.

#################################################################
# The user functions defined in this module are:
#################################################################
# clear_selected_device():
# close_connection():
# open_connection():
# readline():
# set_address(address):
# write(command):

#################################################################
# Import libraries
#################################################################
import serial
from exceptions import IOError

#################################################################
# Global Declarations
#################################################################
Debug = 0  # set to 1 to enable printing of error codes
port = 1

#################################################################
# Function definitions
#################################################################

# Clear currently addressed GPIB device.
def clear_selected_device():
  ser.write("++clr\r\n")


# Close the Prologix virtual serial port.
def close_connection():
  try:
    ser.close()
  except:
    pass


# Open the Prologix virtual serial port.
def open_connection():
  global ser, port
  port_found = 0
  ports_tried = 0

  while not port_found and ports_tried < 10:
    try:
      # open serial port, 9600 baud, 8 data bits, no parity, 1 stop bit,
      # 1 second timeout, no software flow control, RTS/CTS flow control
      # 1 second write timeout
      ser = serial.Serial("COM%d" % port,9600,8,'N',1,1,0,1,1)
      ser.write("++ver\r\n")
      if "Prologix" in ser.readline():
        port_found = 1
        #print "Prologix found on port",port
      else:
        ser.close()
        ports_tried = ports_tried + 1
        port = (port % 10) + 1
    except serial.serialutil.SerialException:
      ports_tried = ports_tried + 1
      port = (port % 10) + 1

  if port_found:
    ser.write("++mode 1\r\n")    # put Prologix in controller mode
    ser.write("++auto 0\r\n")    # turn off Prologix Read-After-Write mode
    ser.flushInput()             # discard data in serial buffer
  else:
    raise IOError("ERROR: Unable to locate the Prologix USB/GPIB interface.")
    

# Read data from Prologix virtual serial port.
def readline():
  ser.write("++read 10\r\n")
  return ser.readline()

  
# Set Prologix GPIB address.
def set_address(address):
  ser.write("++addr %d\r\n" % address)

  
# Write data to the Prologix virtual serial port.
def write(command_code):
  ser.write(command_code + "\r\n")

