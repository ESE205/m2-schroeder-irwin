import argparse
import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep from time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering

OUTPUT_PIN = 13
INPUT_PIN = 11

# parser = argparse.ArgumentParser(
#     prog='program.py', description='Blink LED for a specified time and interval', epilog='Enjoy the program!')
# parser.add_argument('count', type=int, default=5, nargs='?')
# args = parser.parse_args()
# count = args.count


def write_to_file(msg):
    with open('log.txt', 'a') as f:
        f.write(msg + '\n')


GPIO.setup(OUTPUT_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(INPUT_PIN, GPIO.IN)


while True:  # Run ITER_COUNT times
    while (GPIO.input(INPUT_PIN) == GPIO.LOW):
        write_to_file(f'input_pin = {GPIO.input(INPUT_PIN)}')
        GPIO.output(OUTPUT_PIN, GPIO.HIGH)  # Turn on
        sleep(1)                     # Sleep for 1 second
        GPIO.output(OUTPUT_PIN, GPIO.LOW)  # Turn off
        sleep(1)                     # Sleep for 1 second

GPIO.cleanup()
