import wiringpi2 as wiringpi

# Declare Constants
LED = 0
BTN = 1

INPUT = 0
OUTPUT = 1
pwm = 2

HIGH = 1
LOW = 0

PUD_DOWN = 1
PUD_UP = 2
PUD_RESET = 0


wiringpi.wiringPiSetup()


# Turn first pin 0 as output and switch it ON
wiringpi.pinMode(LED, OUTPUT)
wiringpi.digitalWrite(LED, HIGH)


# Turn first pin 1 as input
wiringpi.pinMode(BTN, INPUT)
wiringpi.pullUpDnControl(BTN, PUD_UP) #pull up to 3.3V,make btnPin a stable lev$


try:
        while True:
                if not wiringpi.digitalRead(BTN):     # If button is pressed
                        wiringpi.digitalWrite(LED, HIGH) # switch on LED.
                else:
                        wiringpi.digitalWrite(LED, LOW) # switch off LED.
                wiringpi.delay(1)                      # delay 0.05s
finally:                                 # when you CTRL+C exit, we clean up
        wiringpi.digitalWrite(LED, LOW)         # switch off LED.
        wiringpi.pinMode(LED, INPUT)              # sets ledPin to Input
    # btnPin is already an input, so no need to change anything
