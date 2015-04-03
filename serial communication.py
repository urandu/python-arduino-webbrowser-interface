import serial
import time
import socket
import json

print ("Opening Serial port...")
ser = serial.Serial(port='COM3', baudrate=9600, timeout =1)
ser.close()
ser.open()
time.sleep(2)
##print ("Read complete")
var = ser.read(10)
print (len(var))
##print (s)
if var is not '':
   print (var)

s = socket.socket()         
print ("Socket successfully created")

# reserve a port on my computer 
port = 1234

# Next bind to the port
s.bind(('', 1234))

# put the socket into listening mode
s.listen(5)     
print ("socket is listening") 

# a forever loop until we interrupt it or 
# an error occurs
while True:
   # Establish connection with client.
   c, addr = s.accept()     
   print ('Got connection from'), addr
   var = ''
   var = ser.read(10)   
##   print (len(var))
   var=var.decode("utf-8")
   var.replace("\n", "")
   var.replace("\r", "")
   while len(var) != 10:
       print ("Reading card again")
       var =ser.read(10)
       var=var.decode("utf-8")
       var.replace("\n", "")
       var.replace("\r", "")
   
   ##print (s)
   if var is not '':
      print (var)
   # send a thank you message to the client.
   var=var.encode("utf-8")
   c.sendall(var)
   time.sleep(5)
   # Close the connection with the client
   c.close()
