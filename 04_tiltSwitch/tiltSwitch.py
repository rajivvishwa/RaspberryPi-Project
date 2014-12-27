import wiringpi2 as wiringpi

# Declare Constants
LED = 0
TILT = 1

INPUT = 0
OUTPUT = 1
pwm = 2

HIGH = 1
LOW = 0

PUD_DOWN = 1
PUD_UP = 2
PUD_RESET = 0

# Turn first pin 0 as output and switch it off
wiringpi.pinMode(LED, OUTPUT)
wiringpi.digitalWrite(LED, LOW)

# Turn first pin 1 as input
wiringpi.pinMode(TILT, INPUT)
wiringpi.pullUpDnControl(TILT, PUD_UP) #pull up to 3.3V,make tiltPin a stable lev

try:
  while True:
    if not wiringpi.digitalRead(TILT):     # If tilt detected
      wiringpi.digitalWrite(LED, HIGH) # switch on LED.
    else:
      wiringpi.digitalWrite(LED, LOW) # switch off LED.
      #wiringpi.delay(1)                      # delay 0.05s

finally:                                 # when you CTRL+C exit, we clean up
  wiringpi.digitalWrite(LED, LOW)         # switch off LED.
  wiringpi.pinMode(LED, INPUT)              # sets ledPin to Input
  # tiltswitchPin is already an input, so no need to change anything
