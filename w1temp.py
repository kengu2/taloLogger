#!/usr/bin/python

import sys
import getopt


temperature=[None]*4
sensorfile=''

def main(argv):
   sensor = ''
   try:
      opts, args = getopt.getopt(argv,"s:",["sensor="])
   except getopt.GetoptError:
      print 'w1temp.py -s <sensorid>'
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-s", "--sensor"):
         sensor = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
#   print 'Sensor file is ', sensor
   sensorfile = "/sys/bus/w1/devices/"+sensor+"/w1_slave"
#   print sensorfile


   for x in range(0, 4):

        tfile = open(sensorfile)
        text = tfile.read()
        tfile.close()
        temperature_data = text.split()[-1]
        temperature[x] = float(temperature_data[2:])
        temperature[x] = temperature[x] / 1000

#   print temperature
   print max(temperature)


if __name__ == "__main__":
   main(sys.argv[1:])

