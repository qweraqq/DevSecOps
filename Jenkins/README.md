# Jenkins
## 说明
Jenkins官方Docker镜像中没有包含maven

创建了基于官方docker镜像的Jenkins-with-Maven的dockerfile

## 使用方式
Jenkins官方推荐使用volume(而非bind mount)的方式
```
docker run -d -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home qweraqq/jenkins-with-maven:lts
```