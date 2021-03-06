import os
from flask import Flask, flash, request, redirect, jsonify, send_file
#from movement.delete_file import del_file
#import movement.audio_predict as voice_recognition
#import movement.pathfinding_test_2 as pf
import movement.servo_handler as servo
import movement.ultrasonic_sensors as ultrasonic
import threading
import time

################ PINS ################

sensor_trigger = 38
sensor_echo = 40
servo1 = 23
servo2 = 21

######################################

app = Flask(__name__)
sensors = ultrasonic.UltrasonicHandler([sensor_trigger, sensor_echo])
sensors.start_measuring()

#app.secret_key = os.urandom(12).hex()

@app.route('/', methods=['GET'])
def index():
    return jsonify({'reply': 'Alive'})

@app.route('/move', methods=['GET'])
def move_test():
    #seconds = int(request.args.get("sec"))
    movetest_mover()
    return jsonify({'reply': 'Success'})
###^^^^ above's movemement function
def movetest_mover(units = 4):
    mover = servo.ServoHandler(servo1, servo2)
    mover.move(units)
    mover.release()

@app.route('/rotate', methods=['GET'])
def move_test():
    #seconds = int(request.args.get("sec"))
    rotater()
    return jsonify({'reply': 'Success'})
###^^^^ above's movemement function
def rotater(clockwise = True):
    deg = 90 if clockwise else -90
    mover = servo.ServoHandler(servo1, servo2)
    mover.rotate(90 * deg)
    mover.release()

@app.route('/sensordata', methods=['GET'])
def get_data():
    return jsonify({'reply':'alive', 'front':str(sensors.front)})

if __name__ == '__main__':
    #pf.start('yellow')
    app.run(debug=True, port=8080, host='0.0.0.0')
    #print("!"*50)