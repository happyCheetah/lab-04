import socket
import time
import paho.mqtt.client as mqtt


def on_connect(client,userdata, flags, rc):
    client.subscribe("mlguo/pong")
    client.message_callback_add("mlguo/pong", on_message_from_pong)


def on_message_from_pong(client, userdata, message):
    
    #time.sleep(1)
    received = message.payload.decode()
    print("START_CHAIN message from PONG: " + message.payload.decode())
    received_num = int(received)
    incremented_num = received_num + 1
    
    client.publish("mlguo/ping", f"{incremented_num}")
    print()
    time.sleep(1)
    
    


if __name__ == '__main__':
    
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(host="172.20.10.2", port=1883, keepalive=60)
    
    

    init_msg = 0
    time.sleep(4)
    client.publish("mlguo/ping", f"{init_msg}")
    print("START_CHAIN published init_msg")
    
    
    client.loop_forever()
