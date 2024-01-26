import argparse
import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep from time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering

pin1 = 13

parser = argparse.ArgumentParser(
    prog='program.py', description='Blink LED for a specified time and interval', epilog='Enjoy the program!')
parser.add_argument('count', type=int)
args = parser.parse_args()
count = args.count

GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)

while count > 0:  # Run ITER_COUNT times
    count -= 1  # Decrement counter
    GPIO.output(pin1, GPIO.HIGH)  # Turn on
    sleep(1)                     # Sleep for 1 second
    GPIO.output(pin1, GPIO.LOW)  # Turn off
    sleep(1)                     # Sleep for 1 second
GPIO.cleanup()
