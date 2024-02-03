# syntax=docker/dockerfile:1
# Set default values for environment variables
# image version can be changed by "docker build --build-arg image_version={{new_image_version}}"
ARG image_name=python
ARG image_version=3.10-alpine

# Set environment variables
ENV image_name=${image_name}
ENV image_version=${image_version}

# Use an the image from variables
FROM ${image_name}:${image_version}

WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]