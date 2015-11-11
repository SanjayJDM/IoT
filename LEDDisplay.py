from flask import Flask #flask to enable this as a web service invocation
import RPi.GPIO as GPIO
import time
app=Flask(__name__)

@app.route("/") # root
def hello():
 try:
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(7,GPIO.OUT) # red LED 
  GPIO.setup(11,GPIO.OUT) # blue LED
  #Switch ON/Off every 2 secs
  for x in range(0,3):
   GPIO.output(7,True)
   time.sleep(2) 
   GPIO.output(7,False)
   GPIO.output(11, True)
   time.sleep(2)
   GPIO.output(11,False)
  GPIO.cleanup()
 except:
   GPIO.cleanup()
 return "Lights Off"
if __name__=="__main__":
  app.run(host='0.0.0.0', port=80, debug=True) # server runs on the default port
