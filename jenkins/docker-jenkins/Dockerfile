#after push run "kubectl rollout restart deployment/jenkins"
# Set default values for environment variables
# image version can be changed by "docker build --build-arg image_version={{new_image_version}}"
ARG image_name=jenkins/jenkins
ARG image_version=lts-slim
ARG packages='apt-utils unzip wget vim'
ARG plugins='blueocean kubernetes ansible terraform docker-plugin locale configuration-as-code docker-slaves docker-workflow docker-build-step'
ARG jenkins_url='192.168.49.2'
ARG jenkins_port='32000'

# Use an the image from variables
FROM ${image_name}:${image_version}

USER root
RUN apt-get update -y
RUN apt-get install -y ${packages}
RUN apt-get update -y
COPY jenkins.yaml /var/jenkins_home/jenkins.yaml
#RUN mkdir -p /scripts
#COPY jenkins_update.sh .
#RUN chmod +x jenkins_update.sh
#RUN . /jenkins_update.sh
RUN jenkins-plugin-cli --plugins ${plugins}