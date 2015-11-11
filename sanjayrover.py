import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(07, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

GPIO.output(07,False)
GPIO.output(11,False)
GPIO.output(13,False)
GPIO.output(15,False)

fwd= GPIO.PWM(13,1500)
bck= GPIO.PWM(15,1500)

try:
 while True:
  x = raw_input()
  
  if (x == 'w'):
  # GPIO.output(13,True)
  # GPIO.output(15,False)
   bck.stop()
   fwd.start(100)
   fwd.ChangeDutyCycle(100)
   print "Forward"
  if (x == 's'):
  # GPIO.output(13,False)
  # GPIO.output(15,True)
   fwd.stop()
   bck.start(100)
   bck.ChangeDutyCycle(100)	
   print "Reverse"
  if (x == 'a'):
   GPIO.output(11,False)
   GPIO.output(07, True)
   print"Left"
  if (x == 'd'):
   GPIO.output(07,False)
   GPIO.output(11,True)
   print "Right" 	
  if (x == 'x'):
   GPIO.output(07,False)
   GPIO.output(11,False)
   GPIO.output(13,False)
   GPIO.output(15,False)
   fwd.stop()
   bck.stop()   
   print "stopped"
 #GPIO.output(15,False)
 #time.sleep(1)
 #GPIO.output(13,True)
 #print "13 On"
 #time.sleep(2)
 #print "13 Off"

 #GPIO.output(13,False)
 #time.sleep(1)

 #GPIO.output(07,True)
 #print "07 On"
 #time.sleep(3)
 #print "07 Off"
 #GPIO.output(07,False)

 #GPIO.output(11,True)
 #p = GPIO.PWM(11,50)
 #p.start(50) 
 #print "11 On"
 #time.sleep(10)
 #print "11 Off"
 #p.stop()
 #GPIO.output(11,False)

except KeyboardInterrupt:
 print "QUIT"
 GPIO.cleanup()

