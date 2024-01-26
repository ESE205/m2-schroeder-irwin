import argparse
import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep from time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering

OUTPUT_PIN = 13
INPUT_PIN = 11

parser = argparse.ArgumentParser(
    prog='program.py', description='Blink LED for a specified time and interval', epilog='Enjoy the program!')
parser.add_argument('count', type=int, default=5, nargs='?')
args = parser.parse_args()
count = args.count

GPIO.setup(OUTPUT_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(INPUT_PIN, GPIO.IN)

while (GPIO.input(INPUT_PIN) == GPIO.LOW):
    sleep(0.1)

while count > 0:  # Run ITER_COUNT times
    count -= 1  # Decrement counter
    GPIO.output(OUTPUT_PIN, GPIO.HIGH)  # Turn on
    sleep(1)                     # Sleep for 1 second
    GPIO.output(OUTPUT_PIN, GPIO.LOW)  # Turn off
    sleep(1)                     # Sleep for 1 second

GPIO.cleanup()
