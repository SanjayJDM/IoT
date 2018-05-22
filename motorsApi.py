from flask import Flask
#from flask_api import FlaskAPI
import RPi.GPIO as GPIO
import time # Import the Time library
# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Set variables for the GPIO motor pins 
pinMotorAForwards = 10 
pinMotorABackwards = 9 
pinMotorBForwards = 8 
pinMotorBBackwards = 7
# Set the GPIO Pin mode
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

#app = FlaskAPI(__name__)
app = Flask(__name__)

@app.route('/', methods=["GET"])

# Turn all motors off
def StopMotors():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 0)
# Turn both motors forwards
def Forwards():
    GPIO.output(pinMotorAForwards, 1)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 1)
    GPIO.output(pinMotorBBackwards, 0)
# Turn both motors backwards
def Backwards():
   GPIO.output(pinMotorAForwards, 0) 
   GPIO.output(pinMotorABackwards, 1) 
   GPIO.output(pinMotorBForwards, 0) 
   GPIO.output(pinMotorBBackwards, 1)
# Turn left
def Left():
   GPIO.output(pinMotorAForwards, 0) 
   GPIO.output(pinMotorABackwards, 1) 
   GPIO.output(pinMotorBForwards, 1)
   GPIO.output(pinMotorBBackwards, 0)
# Turn Right
def Right():
   GPIO.output(pinMotorAForwards, 1) 
   GPIO.output(pinMotorABackwards, 0) 
   GPIO.output(pinMotorBForwards, 0) 
   GPIO.output(pinMotorBBackwards, 1)

def api_root():
    return {
           "url": request.url 
                         }  
@app.route('/sanjayrover/fwd/', methods=["GET", "POST"])
def api_fwds_control():
    Forwards()
@app.route('/sanjayrover/back/', methods=["GET", "POST"])
    Backwards()
@app.route('/sanjayrover/stop/', methods=["GET", "POST"])
def api_stp_control():
    StopMotors()
@app.route('/sanjayrover/right/', methods=["GET", "POST"])
def api_right_control():
    Right()
@app.route('/sanjayrover/left/', methods=["GET", "POST"])
def api_left_control():
    Left()

if __name__ == "__main__":
    app.run()
