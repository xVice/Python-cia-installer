import os
import time
import sys

def list_files(directory, extension):
    return (f for f in os.listdir(directory) if f.endswith('.' + extension))

def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

if len(sys.argv) < 2:
    print('Usage: ' + sys.argv[0] + ' <console ip>')
    sys.exit(1)

version = " b1"
print("AutoInstall" + version)
directory = 'CIAS/'
ipList = sys.argv[1:]
ip = listToString(ipList)
print("ConsoleIP: " + ip)
print("CIAS directory: " + directory)
files = list_files(directory, "cia")
print("Sending cias to 3ds...")
print("----------------------------")
try:
    for f in files:
        os.system("servefiles.py " + ip + ' CIAS/' + f)
        print("Send: " + f)
except Exception as e:
    print("An exception occured: " + e)
finally:
    print("----------------------------")
    print("successfully send all files to 3DS with IP: " + ip)
    time.sleep(5)

