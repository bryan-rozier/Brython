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


board = serial.Serial('COM10',115200,timeout=1)
print "Waiting for power cycle"
try:
    line=""
    while "Booting" not in line:
        line=board.readline()
        if line!="":
            print line.strip()
    #U-Boot is starting lets stop it asap
    while "#" not in line:
        board.write("\n")     
        line=board.readline()
        print line.strip()
    print "At prompt"
    while line != "":
        line=board.readline()
    for name,val in cmd:
        #print "Processing: (%s, %s)" % (name,val)
        board.write("setenv "+name+" "+val+"\n")
        line = board.readline()#eat echo
        print "Processing: %s" % line.strip()
        line = board.readline()#read response [prompt]
        if "## Error:" in line:
            print "resp: %s" % line
    print "Checking Variables"
    for  name,val in cmd:
        board.write("printenv "+name+"\n")
        line = board.readline()#eat echo
        #print "Processing: %s" % line.strip()
        line = board.readline()#read response [prompt]
        if name in line and val in line:
            print "OK: %s" % line.strip()
        else:
            print "ERROR: %s" % line.strip()
        
    print "board booting"
    board.write("boot\n")
    board.close()
except KeyboardInterrupt:
    print "Halting Execution"

board.close()
print ("End")
