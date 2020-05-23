FROM jenkins/jenkins:lts
ARG user=jenkins
USER root
RUN apt-get update && apt-get install -y maven git ant gradle && && rm -rf /var/lib/apt/lists/*
install-plugins.sh ldap kubernetes workflow-job workflow-aggregator credentials-binding git configuration-as-code fortify sonar
USER ${user}
