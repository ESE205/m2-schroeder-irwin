import argparse
import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep from time module
from time import time

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
parser.add_argument('run_time', type=int)
parser.add_argument('blink_interval', type=int)
args = parser.parse_args()
debug = args.debug
run_time = args.run_time
blink_interval = args.blink_interval

start_time = time()


def write_to_file(msg):
    with open('data.txt', 'a') as f:
        f.write(msg + '\n')


GPIO.setup(OUTPUT_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(INPUT_PIN, GPIO.IN)


while time() - start_time < run_time:  # Run ITER_COUNT times
    input_pin = GPIO.input(INPUT_PIN)
    write_to_file(f'{time() - start_time}:\tinput_pin = {input_pin}')
    print_debug(f'{time() - start_time}:\tinput_pin = {input_pin}')
    if (input_pin == GPIO.LOW):
        GPIO.output(OUTPUT_PIN, GPIO.HIGH)  # Turn on
        sleep(blink_interval)
        GPIO.output(OUTPUT_PIN, GPIO.LOW)  # Turn off
        sleep(blink_interval)

GPIO.cleanup()
