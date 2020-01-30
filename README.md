# progress-poc

### Install Environement
```
conda env create -f environment.yml
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

```
Status {
  Queueing,
  Submitting,
  Submitted,
  Running,
  Completed
}
```

```
Orignal Status
enum TaskStatus {
    NEW,        // task has just been created and not yet submitted for execution
    SUBMITTED,  // task has been submitted for execution
    RUNNING,    // task is currently running
    COMPLETED   // task execution completed either successfully or with with an error condition
}
```
