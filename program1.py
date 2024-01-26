import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library

GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering

OUTPUT_PIN = 13
INPUT_PIN = 11

GPIO.setup(OUTPUT_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(INPUT_PIN, GPIO.IN)

while True:
    state = GPIO.input(INPUT_PIN)
    if state == GPIO.HIGH:
        GPIO.output(OUTPUT_PIN, GPIO.HIGH)
    else:
        GPIO.output(OUTPUT_PIN, GPIO.LOW)
