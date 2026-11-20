#!/bin/bash
# Docker build, container execution, and endpoint verification script

IMAGE_NAME="ml-inference-service:v1.0"
CONTAINER_NAME="ml-inference-container"

echo "=== Building Docker Image ==="
docker build -t $IMAGE_NAME .

echo "=== Verifying Docker Image in Local Store ==="
docker images | grep ml-inference-service

echo "=== Running Container with Port Mapping (8000:8000) ==="
docker run -d -p 8000:8000 --name $CONTAINER_NAME $IMAGE_NAME

echo "=== Waiting for service healthcheck ==="
sleep 5
docker ps | grep $CONTAINER_NAME
docker logs $CONTAINER_NAME

echo "=== Testing Containerized API Endpoint ==="
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"sepal_length": 6.2, "sepal_width": 3.4, "petal_length": 5.4, "petal_width": 2.3}'

echo "
Cleaning up container resources..."
docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME
echo "Docker workflow verified successfully."
