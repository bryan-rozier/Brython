import serial
import warnings

cycles=0
boots=0
fails=0

user = "root"
cmd=[]
cmd.append(("gatewayip","10.10.10.1"))
cmd.append(("netmask","255.255.128.0"))
cmd.append(("serverip","10.10.10.15"))
cmd.append(("ipaddr","10.10.11.0"))
cmd.append(("boot","ramfs"))
cmd.append(("tftp_version","LINUXBSP-500"))


for name,val in cmd:
    print name
    print val
board = serial.Serial('COM10',115200,timeout=1)
try:
		line=""
		while "Booting" not in line:
		    print line
		    line=board.readline()
		#U-Boot is starting lets stop it asap
		while "#" not in line:
		    board.write("\n")	 
		    line=board.readline()
		    print line
		print "At prompt"
		board.close()
		print "board booting"

except KeyboardInterrupt:
    print "Halting Execution"

board.close()
print ("End")
