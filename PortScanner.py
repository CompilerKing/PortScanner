__author__ = 'Samuel Decanio'
#***This code is based off code found at the tutorial linked in the README***

import socket
import subprocess
import sys
from datetime import datetime

#Clears the screen
subprocess.call('clear', shell=True)

#Ask for input
remoteServer = raw_input("Enter a remote host that you would like to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

#Displaying info on the host we are scanning
print "-" * 60
print "Please wait, scanning the remote host", remoteServerIP
print "-" * 60

#Checking what time the scan began
time1 = datetime.now()

#Using the range function to specify ports (here it scans all ports from 1 - 1024)
try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))

        if result == 0:
            print "Port {}: \tOpen".format(port)

        sock.close()

except KeyboardInterrupt:
    print "You Pressed Ctrl+C"
    sys.exit()

except socket.galerror:
    print "Hostname could not be resolved. Exiting now."

except socket.error:
    print "Couldn't connect to server"
    sys.exit()

#Checking time again
time2 = datetime.now()

#Checking the amount of time it took to run the script
timeDifference = time2 - time1
print "Scan completed in: ", timeDifference

