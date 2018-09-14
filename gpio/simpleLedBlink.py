import RPi.GPIO as gpio
import time

led_pin = 5

gpio.setmode(gpio.BCM)
gpio.setup(led_pin, gpio.OUT)

try:
    for i in range(0, 20):
        print("Iteration " + str(i+1))
        gpio.output(led_pin, True)
        time.sleep(1)
        gpio.output(led_pin, False)
        time.sleep(1)
    print("Blink Finished")
    gpio.cleanup()
except KeyboardInterrupt:
    gpio.cleanup()
    
