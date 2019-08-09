import RPi.GPIO as GPIO
import time

ANGLE_0 = 3
ANGLE_45 = 5
ANGLE_90 = 7.5
ANGLE_180 = 12 
 
servo_pin_1 = 12  # PWM pin num 12
servo_pin_2 = 2  # pwm pin num 2
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin_1, GPIO.OUT)
GPIO.setup(servo_pin_2, GPIO.OUT)

p1 = GPIO.PWM(servo_pin_1,50)
p2 = GPIO.PWM(servo_pin_2,50)

p1.start(0)
p2.start(0)



def servo_action(pin, angle ,delays) : 
	try:
		
		pin.ChangeDutyCycle(angle)
		print ("angle"+str(pin)+ " : "+str(angle))
		time.sleep(delays)
	
		

	except:
		pin.stop()


# while True : 

# 	servo_action(p1,ANGLE_0,DELAY)
# 	time.sleep(1)
	
# 	servo_action(p2,ANGLE_180,DELAY)
# 	time.sleep(1)
	
# 	servo_action(p1,ANGLE_180,DELAY)
# 	time.sleep(1)
		
# 	servo_action(p2,ANGLE_0,DELAY)
# 	time.sleep(1)        

p1.stop()
p2.stop()
GPIO.cleanup()

