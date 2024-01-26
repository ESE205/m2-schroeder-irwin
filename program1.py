import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
import argparse

GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering

OUTPUT_PIN = 13
INPUT_PIN = 11


def print_debug(msg):
    if debug:
        print(msg)


parser = argparse.ArgumentParser(
    prog='program.py', description='Blink LED for a specified time and interval', epilog='Enjoy the program!')

parser.add_argument('-d', '--debug', action='store_true')

GPIO.setup(OUTPUT_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(INPUT_PIN, GPIO.IN)

args = parser.parse_args()
debug = args.debug

while True:

    state = GPIO.input(INPUT_PIN)
    print_debug(f'input_pin = {state}')
    if state == GPIO.HIGH:
        GPIO.output(OUTPUT_PIN, GPIO.HIGH)
    else:
        GPIO.output(OUTPUT_PIN, GPIO.LOW)
