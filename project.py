import RPi.GPIO as GPIO
# import Adafruit_CharLCD as LCD
import Adafruit_DHT as DHT
import time

irsensor1 = 3
irsensor2 = 5
tempsensor = 7
led = 11

# lcd1 = 32
# lcd2 = 26
# lcd3 = 24
# lcd4 = 22
# lcd5 = 18
# lcd6 = 16

# lcd = LCD.Adafruit_CharLCD(lcd1, lcd2, lcd3, lcd4, lcd5, lcd6, 0, 16, 2)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(irsensor1,GPIO.IN)
GPIO.setup(irsensor2,GPIO.IN)
GPIO.setup(tempsensor,GPIO.IN)
GPIO.setup(led,GPIO.OUT)


def loop():
    personcount = 0
    while True:
        humidity, temperature = DHT.read_retry(Adafruit_DHT.DHT11, tempsensor)

        # if GPIO.input(tempsensor):
        #     lcd.cursor_position(0,1); 
        #     lcd.message("Temperature:")
        #     lcd.cursor_position(12,1)
        #     lcd.message(temperature)
        #     time.sleep(3)    

        if GPIO.input(irsensor1):
            personcount += 1
            # lcd.clear()
            # lcd.cursor_position(0,0)
            # lcd.message("People In Room:")
            # lcd.cursor_position(15,0)
            # lcd.message(count)
            time.sleep(1)
        
        if GPIO.input(irsensor2) and personcount != 0:
            personcount -= 1
            # lcd.clear()
            # lcd.cursor_position(0,0)
            # lcd.message("People In Room:")
            # lcd.cursor_position(15,0)
            # lcd.message(count)
            time.sleep(1)
        
        print(personcount)
        print(temperature)

        if personcount == 0:
            GPIO.output(led, GPIO.LOW)
        else:
            GPIO.output(led, GPIO.HIGH)
        time.sleep(1)


if __name__ == '__main__':
    try:
        # lcd.message("Visitor Counter")
        loop()
    except KeyboardInterrupt:
        pass