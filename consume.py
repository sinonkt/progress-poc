#!/usr/bin/env python
from confluent_kafka import avro
from confluent_kafka.avro import AvroConsumer
from confluent_kafka.avro.serializer import SerializerError

conf = {
    "bootstrap.servers": "10.227.52.244:31090,10.227.52.244:31091,10.227.52.244:31092",
    "schema.registry.url": "http://10.227.52.244:30553",
    "group.id": "testeiei"
}
topic="ingester"

key_schema = avro.load("./schemas/{}-key.avsc".format(topic))
value_schema = avro.load("./schemas/{}-value.avsc".format(topic))
# c = AvroConsumer(conf, reader_key_schema=key_schema, reader_value_schema=value_schema)
c = AvroConsumer(conf)
c.subscribe([topic])

while True:
    try:
        msg = c.poll(1)
        # There were no messages on the queue, continue polling
        if msg is None:
            print(".")
            continue

        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue
        print(msg.key(), msg.value())
    except SerializerError as e:
        # Report malformed record, discard results, continue polling
        print("Message deserialization failed {}".format(e))
        continue
    except KeyboardInterrupt:
        break
    print("Waiting...")

print("Shutting down consumer..")
c.close()
