 # Variables
IMAGE_NAME = hangman-app
CONTAINER_NAME = hangman-container
PORT = 5000

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run the container interactively with port mapping
run:
	docker run -it -p $(PORT):$(PORT) --name $(CONTAINER_NAME) $(IMAGE_NAME)

# Clean up: Remove the container and image
clean:
	docker rm -f $(CONTAINER_NAME) || true
	docker rmi -f $(IMAGE_NAME) || true

# Rebuild the image
rebuild: clean build

# List all Docker images
images:
	docker images

# List all running containers
ps:
	docker ps -a
