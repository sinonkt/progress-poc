TOPIC=ingester
SCHEMA_REGISTRY_HOST=10.227.52.247
SCHEMA_REGISTRY_PORT=30553

for schemaType in key value;
do
  escapedAvroSchemaValue=$(cat ${TOPIC}-${schemaType}.avsc | awk '{ gsub("\"","\\\"",$0); print $0 }' | tr -d '\n')
  # echo $escapedAvroSchemaValue
  curl -X POST -H "Content-Type: application/vnd.schemaregistry.v1+json" \
    --data "{ \"schema\": \"${escapedAvroSchemaValue}\" }" \
    http://${SCHEMA_REGISTRY_HOST}:${SCHEMA_REGISTRY_PORT}/subjects/${TOPIC}-${schemaType}/versions
done

# curl -X DELETE http://10.227.52.244:30553/subjects/ingester-key
# curl -X DELETE http://10.227.52.244:30553/subjects/ingester-value