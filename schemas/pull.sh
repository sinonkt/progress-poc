TOPIC=ingester
SCHEMA_REGISTRY_ENDPOINT=10.227.52.244:30553
KEY_VERSION=latest
VALUE_VERSION=latest

wget http://${SCHEMA_REGISTRY_ENDPOINT}/subjects/${TOPIC}-key/versions/${KEY_VERSION}/schema -O $TOPIC-key.avsc
wget http://${SCHEMA_REGISTRY_ENDPOINT}/subjects/${TOPIC}-value/versions/${VALUE_VERSION}/schema -O $TOPIC-value.avsc