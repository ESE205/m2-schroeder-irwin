import argparse
import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep from time module
from time import time

GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering

OUTPUT_PIN = 13
INPUT_PIN = 11

start_time = time()


def write_to_file(msg):
    with open('data.txt', 'a') as f:
        f.write(msg + '\n')


GPIO.setup(OUTPUT_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(INPUT_PIN, GPIO.IN)


while True:  # Run ITER_COUNT times
    input_pin = GPIO.input(INPUT_PIN)
    write_to_file(f'{time() - start_time}:\tinput_pin = {input_pin}')
    while (input_pin == GPIO.LOW):
        GPIO.output(OUTPUT_PIN, GPIO.HIGH)  # Turn on
        sleep(1)                     # Sleep for 1 second
        GPIO.output(OUTPUT_PIN, GPIO.LOW)  # Turn off
        sleep(1)                     # Sleep for 1 second

GPIO.cleanup()
