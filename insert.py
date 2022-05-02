from r305 import R305
import sys

device   = "/dev/ttyUSB0"
baudrate =57600 # the default baudrate for this module is 57600

dev = R305(device, baudrate)

def callback(data):
    x = input(data)

result = dev.StoreFingerPrint(IgnoreChecksum=True, callback=callback)

print(result)
