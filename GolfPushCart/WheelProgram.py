import RPi.GPIO as GPIO
# https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/

import time

# We are going to use the BCM not BOARD layout
GPIO.setmode(GPIO.BCM)  
GPIO.setwarnings(False)

# LEFT WHEEL -----------------------------------------------------------

RPWM = 19;  # GPIO pin 19 to the RPWM on the BTS7960
LPWM = 26;  # GPIO pin 26 to the LPWM on the BTS7960

# For enabling "Left" and "Right" movement
L_EN = 20;  # connect GPIO pin 20 to L_EN on the BTS7960
R_EN = 21;  # connect GPIO pin 21 to R_EN on the BTS7960

# Set all of our PINS to output
GPIO.setup(RPWM, GPIO.OUT)
GPIO.setup(LPWM, GPIO.OUT)
GPIO.setup(L_EN, GPIO.OUT)
GPIO.setup(R_EN, GPIO.OUT)

# Enable "Left" and "Right" movement on the HBRidge
GPIO.output(R_EN, True)
GPIO.output(L_EN, True)

rpwm= GPIO.PWM(RPWM, 25)
lpwm= GPIO.PWM(LPWM, 25)

rpwm.ChangeDutyCycle(0) # Forward
lpwm.ChangeDutyCycle(0) # Reverse

rpwm.start(0)
lpwm.start(0)

# RIGHT WHEEL ----------------------------------------------------------

RRPWM = 16;  # GPIO pin 16 to the RPWM on the BTS7960
RLPWM = 12;  # GPIO pin 12 to the LPWM on the BTS7960

# For enabling "Left" and "Right" movement
RL_EN = 5;  # connect GPIO pin 5 to L_EN on the BTS7960
RR_EN = 6;  # connect GPIO pin 6 to R_EN on the BTS7960

# Set all of our PINS to output
GPIO.setup(RRPWM, GPIO.OUT)
GPIO.setup(RLPWM, GPIO.OUT)
GPIO.setup(RL_EN, GPIO.OUT)
GPIO.setup(RR_EN, GPIO.OUT)

# Enable "Left" and "Right" movement on the HBRidge
GPIO.output(RR_EN, True)
GPIO.output(RL_EN, True)

rrpwm= GPIO.PWM(RRPWM, 25)
rlpwm= GPIO.PWM(RLPWM, 25)

rrpwm.ChangeDutyCycle(0) # Controls Speed R Wheel
rlpwm.ChangeDutyCycle(0)

rrpwm.start(0)
rlpwm.start(0)

# WHEEL CASE -----------------------------------------------------------

def control_cart(command):
    match command:
        case "forward":
            print("Cart is moving forward.")
            rpwm.ChangeDutyCycle(25)  # LEFT WHEEL
            rrpwm.ChangeDutyCycle(25) # RIGHT WHEEL
            lpwm.ChangeDutyCycle(0)
            rlpwm.ChangeDutyCycle(0)  
            
        case "backward":
            print("Cart is moving backward.")
            rpwm.ChangeDutyCycle(0)  
            rrpwm.ChangeDutyCycle(0) 
            lpwm.ChangeDutyCycle(25)  # LEFT WHEEL
            rlpwm.ChangeDutyCycle(25) # RIGHT WHEEL   
            
        case "left":
            print("Cart is turning left.")
            rpwm.ChangeDutyCycle(0)              
            rrpwm.ChangeDutyCycle(25) # RIGHT WHEEL
            lpwm.ChangeDutyCycle(0)
            rlpwm.ChangeDutyCycle(0)
            
        case "right":
            print("Cart is turning right.")
            rpwm.ChangeDutyCycle(25)  # LEFT WHEEL
            rrpwm.ChangeDutyCycle(0)
            lpwm.ChangeDutyCycle(0)
            rlpwm.ChangeDutyCycle(0)
            
        case "stop":
            print("Cart has stopped.")
            rpwm.ChangeDutyCycle(0)  # LEFT WHEEL
            rrpwm.ChangeDutyCycle(0) # RIGHT WHEEL
            lpwm.ChangeDutyCycle(0)
            rlpwm.ChangeDutyCycle(0)  
            
        case _:
            print("Unknown command.")
            rpwm.ChangeDutyCycle(0)  # LEFT WHEEL
            rrpwm.ChangeDutyCycle(0) # RIGHT WHEEL
            lpwm.ChangeDutyCycle(0)
            rlpwm.ChangeDutyCycle(0)  
    
# WHILE LOOP -----------------------------------------------------------

while 1:
  """
  control_cart("right")
  time.sleep(2) # PAUSES THEN GOES FORWARD
  control_cart("forward")
  time.sleep(10) # PAUSES THEN GOES FORWARD
  """
  
  command = input("Enter command: ")
  control_cart(command)
  time.sleep(2)
  control_cart("stop")
  



              


"""
while 1:

  for x in range(30):
    print("Speeding up " + str(x))
    rpwm.ChangeDutyCycle(x)
    rrpwm.ChangeDutyCycle(x)
    
    time.sleep(0.25)

  time.sleep(5)

  for x in range(30):

    print("Slowing down " + str(x))
    rpwm.ChangeDutyCycle(30-x)
    rrpwm.ChangeDutyCycle(x)
    
    time.sleep(0.25)
"""
