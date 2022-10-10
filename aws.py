import random
import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

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
    while True:
        time.sleep(5)
        curtem = random.randint(1, 40)
        myMQTTClient.publish(topic="test/HelloWorld", QoS=1, payload='{"Weather":"'+str(curtem)+'"}')


if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        pass
