import time
import board
import neopixel
import analogio

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.01, auto_write=False)
pixels.fill((0, 0, 0))
pixels.show()

light = analogio.AnalogIn(board.LIGHT)

while True:
    for i in range(10):
        print(light.value)
        if light.value <= 800:
            pixels[i] = (255, 255, 255)
        else:
            pixels[i] = (0, 0, 0)
    pixels.show()
    time.sleep(0.9)
