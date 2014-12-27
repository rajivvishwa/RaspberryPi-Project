import wiringpi2 as wiringpi

# Declare Constants
RELAY = 0

INPUT = 0
OUTPUT = 1

HIGH = 1
LOW = 0

# Turn first pin 0 as output and switch it off
wiringpi.pinMode(RELAY, OUTPUT)

try:
	while True:
		wiringpi.digitalWrite(RELAY, LOW) # switch off RELAY
		wiringpi.delay(5)
	else:
		wiringpi.digitalWrite(RELAY, HIGH) # switch on RELAY
		wiringpi.delay(5)

finally:                                 # when you CTRL+C exit, we clean up
  wiringpi.digitalWrite(RELAY, LOW)         # switch off LED.
  wiringpi.pinMode(RELAY, INPUT)              # sets Relay to Input