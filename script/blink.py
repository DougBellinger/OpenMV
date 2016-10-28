import  pyb, time
print ("BLINK TEST")
red_led = pyb.LED(1)
red_led.on()
time.sleep(500)
red_led.off()

