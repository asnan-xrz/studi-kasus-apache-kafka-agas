from confluent_kafka import Producer
import json
import random
import time

producer = Producer({'bootstrap.servers': 'localhost:9092'})

sensor_ids = ['S1', 'S2', 'S3']

def send_message(producer, topic, value):
    producer.produce(topic, value=json.dumps(value).encode('utf-8'))
    producer.flush()

while True:
    sensor_id = random.choice(sensor_ids)
    suhu = random.randint(70, 100)
    data = {'sensor_id': sensor_id, 'suhu': suhu}

    send_message(producer, 'sensor-suhu', data)
    print(f'Kirim: {data}')

    time.sleep(1)