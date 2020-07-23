FROM jenkins/jenkins:lts
ARG user=jenkins
USER root
RUN apt-get update && apt-get install -y maven git ant gradle subversion curl wget && rm -rf /var/lib/apt/lists/*
RUN install-plugins.sh ldap kubernetes workflow-job workflow-aggregator credentials credentials-binding git configuration-as-code fortify sonar subversion docker
USER ${user}
