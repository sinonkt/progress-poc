# progress-poc

### Install Environement
```
conda create -n confluent-kafka  -f environment.yml
```

### Listen to kafka natively
```
kafkacat -b 10.227.52.244:31090 -C -t test_progress
```

### Listen to kafka regarding to Confluent Message Schema
```
./consume.py
```

### Mock up messages lies here
```
data
```

### Progress Event Schema
```
schemas
```

### Produce messages
```
./produce.py
```
