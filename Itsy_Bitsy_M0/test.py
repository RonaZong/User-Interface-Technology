# Write your code here :-)
import board
import analogio
photocell = analogio.AnalogIn(board.A1)
photocell.value

led = digitalio.DigitalInOut(board.A1)
led.direction = digitalio.Direction.OUTPUT
led.value = True
led.value = False
