FROM jenkins/jenkins:lts

ARG user=jenkins

USER root
RUN apt-get update && apt-get install -y maven

USER ${user}
