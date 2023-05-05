import paho.mqtt.client as mqtt
import time
def on_connect(client, userdata, flags, rc):
    print(">>>CONNECTED TO SERVER")
    client.subscribe("mlguo/ping")


    client.message_callback_add("mlguo/ping", on_message_from_ping)


def on_message_from_ping(client, userdata, message):
    received = message.payload.decode()
    print("CONT_CHAIN mesage: " + received)
    print()

    received_num =int(received)
    incremented_num = received_num + 1
    client.publish("mlguo/pong", f"{incremented_num}")
    time.sleep(0.5)



if __name__ == '__main__':
    
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(host="172.20.10.3", port=1883, keepalive=60)
    
    
    
    
    client.loop_forever()


