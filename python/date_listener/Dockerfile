# Set default values for environment variables
# image version can be changed by "docker build --build-arg image_version={{new_image_version}}"
ARG image_name=python
ARG image_version=3.10-slim

# Use an the image from variables
FROM ${image_name}:${image_version}

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ../../for_jobs /app

EXPOSE 8080

# Run the Python program when the container starts
CMD [ "python", "date_listener.py" ]
