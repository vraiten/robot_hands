import RPi.GPIO as GPIO
import time

ANGLE_0 = 3
ANGLE_45 = 5
ANGLE_90 = 7
ANGLE_180 = 11 

DELAY = 5
 
pin = 12 # PWM pin num 18
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, 50)
p.start(0)
cnt = 0

try:
    while True:
        p.ChangeDutyCycle(ANGLE_0)
        print ("angle 0 : "+str(ANGLE_0))
        time.sleep(DELAY)

        p.ChangeDutyCycle(ANGLE_90)
        print ("angle 90 : "+str(ANGLE_45))
        time.sleep(DELAY)

        p.ChangeDutyCycle(ANGLE_45)
        print ("angle 45 : "+str(ANGLE_90))
        time.sleep(DELAY)

        p.ChangeDutyCycle(ANGLE_180)
        print ("angle 180 : "+str(ANGLE_180))
        time.sleep(DELAY)

except KeyboardInterrupt:
    p.stop()
GPIO.cleanup()


