#!/usr/bin/env python
import os
import time
import json
from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer

MESSAGE_INTERVAL_SECONDS=5
topic="ingester"

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

conf = {
    "bootstrap.servers": "10.227.52.245:31090,10.227.52.246:31091,10.227.52.247:31092",
    "on_delivery": delivery_report,
    "schema.registry.url": "http://10.227.52.247:30553"
}
value_schema = avro.load("./schemas/{}-key.avsc".format(topic))
key_schema = avro.load("./schemas/{}-key.avsc".format(topic))

avroProducer = AvroProducer(conf, default_key_schema=key_schema, default_value_schema=value_schema)

with open('./data/example_ingest_messages.json', 'r') as json_file:
  messages = json.load(json_file)
  for key, value in messages:
    print(topic, key, value)
    avroProducer.produce(topic=topic, key=key, value=value)
    avroProducer.poll(0)
    time.sleep(MESSAGE_INTERVAL_SECONDS)
avroProducer.flush()
