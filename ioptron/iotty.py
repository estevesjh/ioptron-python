# Interface to a serial device

import time
import sys
import serial

class iotty:

  def __init__(self, port = 'COM5', baud=115200):
    self.send_wait = 0.25

    try:
      self.ser = serial.Serial(port, baud)
    except serial.SerialException as e:
      sys.stderr.write('ERROR: Could not open port: ' + port + '\n')
      sys.exit(1)

  def open(self):
    self.ser.isOpen()

  def send(self, string):
    b = string.encode('utf-8')
    self.ser.write(b)
    time.sleep(self.send_wait)

  def recv(self):
    output = ''
    while self.ser.inWaiting() > 0:
      output += self.ser.read(1).decode('utf-8')
    return output

  def close(self):
    self.ser.close()
