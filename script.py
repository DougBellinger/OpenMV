import sys, serial, os
print 'Starting Terminal on:', sys.argv[1]
print 'Sending Script ', sys.argv[2]
s = serial.Serial(sys.argv[1], 115200, timeout=1)
s.write("\r\r")
#send CTL-D
s.write('\x04')
print s.read(255)
try:
    f = open(sys.argv[2], 'rU')
except IOError as e:
    print "error: ", e.errno
else:
    with f:
        for l in f.read().splitlines():
            # print "LINE:", l 
            s.write(l)
            s.write('\r')
            print s.readline().strip()
        f.close()
