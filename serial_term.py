import sys, serial
print 'Starting Terminal on:', sys.argv[1]
ser = serial.Serial(sys.argv[1], 115200, timeout=1)
ser.write("\r\r")
#send CTL-D
ser.write('\x04')
print ser.read(255)
