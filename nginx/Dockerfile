# Set default values for environment variables
# image version can be changed by "docker build --build-arg image_version={{new_image_version}}"
ARG image_name=nginx
ARG image_version=latest

# Use an the image from variables
FROM ${image_name}:${image_version}

# Copy your custom Nginx configuration file to the container
COPY nginx.conf /etc/nginx/conf.d/

# Expose port 80 for HTTP traffic
EXPOSE 80