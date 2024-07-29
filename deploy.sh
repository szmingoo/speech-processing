#!/bin/bash
# Set variables
IMAGE_NAME="speech-processing-image"
HARBOR_URL="harbor.xxx.com/xxx"
TAG="V20240725"

# Build Docker image
echo "Building Docker image..."
docker build -t ${IMAGE_NAME}:${TAG} .

# Check if the build was successful
if [ $? -ne 0 ]; then
  echo "Docker image build failed."
  exit 1
fi

# Tag Docker image for Harbor
echo "Tagging Docker image..."
docker tag ${IMAGE_NAME}:${TAG} ${HARBOR_URL}/${IMAGE_NAME}:${TAG}

# Check if the tag was successful
if [ $? -ne 0 ]; then
  echo "Docker image tagging failed."
  exit 1
fi

# Login to Harbor
echo "Logging in to Harbor..."
docker login ${HARBOR_URL}

# Check if the login was successful
if [ $? -ne 0 ]; then
  echo "Docker login failed."
  exit 1
fi

# Push Docker image to Harbor
echo "Pushing Docker image to Harbor..."
docker push ${HARBOR_URL}/${IMAGE_NAME}:${TAG}

# Check if the push was successful
if [ $? -ne 0 ]; then
  echo "Docker image push failed."
  exit 1
fi

# Output success message
echo "Docker image ${HARBOR_URL}/${IMAGE_NAME}:${TAG} pushed to Harbor successfully."
