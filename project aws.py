from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import RPi.GPIO as GPIO
import Adafruit_DHT as DHT
import datetime
import time

irsensor1 = 3
irsensor2 = 5
tempsensor = 7
led = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(irsensor1,GPIO.IN)
GPIO.setup(irsensor2,GPIO.IN)
GPIO.setup(tempsensor,GPIO.IN)
GPIO.setup(led,GPIO.OUT)

myMQTTClient = AWSIoTMQTTClient("Group8ClientID") #random key, if another connection using the same key is opened the previous one is auto closed by AWS IOT
myMQTTClient.configureEndpoint("a3rvuxlfs3wna4-ats.iot.ap-south-1.amazonaws.co m", 8883)
myMQTTClient.configureCredentials("/home/pi/Documents/aws/AmazonRootCA1.pem","/home/pi/Documents/aws/private.pem.key","/home/pi/Documents/aws/certificate.pem.crt")
myMQTTClient.configureOfflinePublishQueueing(-1)	#	Infinite	offline	Publish queueing
myMQTTClient.configureDrainingFrequency(2) # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10) # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5) # 5 sec
print('Initiating Realtime Data Transfer From Raspberry Pi...')
myMQTTClient.connect()

def loop():
    personcount = 0
    while True:
        if GPIO.input(irsensor1):
            personcount += 1
            time.sleep(1)
        
        if GPIO.input(irsensor2) and personcount != 0:
            personcount -= 1
            time.sleep(1)

        if personcount == 0:
            GPIO.output(led, GPIO.LOW)
        else:
            GPIO.output(led, GPIO.HIGH)

        humidity, temperature = DHT.read_retry(Adafruit_DHT.DHT11, tempsensor)

        timestamp = datetime.datetime.now()
        myMQTTClient.publish(topic="test/HelloWorld", 
            QoS=1, 
            payload = '{"TimeStamp": "' + str(timestamp) + 
                '" , "Temperature":' + str(temperature) + 
                ', "Person count":' + str(personcount) + '}')
        time.sleep(5)


if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        pass
