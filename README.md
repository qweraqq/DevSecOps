# DevSecOps

## 在Jenkins中调用Sonarqube
Sonarqube官方给出了一个不是特别详细的说明文档[https://docs.sonarqube.org/display/SCAN/Analyzing+with+SonarQube+Scanner+for+Jenkins](https://docs.sonarqube.org/display/SCAN/Analyzing+with+SonarQube+Scanner+for+Jenkins)

这里补充一些实际使用时候发现的结果:
1. 至少有两种方式可以在Jenkins实现Sonarqube的自动调用
	* 第一种是使用maven，这种方式不需要特别的Jenkins的配置，和一般build中的maven配置没有很大区别
	```mvn sonar:sonar Dsonar.host.url=http://$SONAR_IP:9000 Dsonar.login=$SONAR_TOKEN```
  		- 这种方式不会在Jenkins出现Sonarqube的图标和连接
  		- 这种方式可以在Sonarqube中查看相关结果
  	* 第二种方式是参考官方的说明文档，插件[https://plugins.jenkins.io/sonar](https://plugins.jenkins.io/sonar)的安装及Manage Jenkins/Configure System参照教程即可，接着在Manage Jenkins/Global tool configuration中配置SonarQube Scanner，选择自动安装即可
  		- 这种方式在配置任务时候**需要配置sonar.java.binaries**这个参数以指定.class文件的位置，原因参考[https://docs.sonarqube.org/display/PLUG/Java+Plugin+and+Bytecode](https://docs.sonarqube.org/display/PLUG/Java+Plugin+and+Bytecode)
  		- 这种方式可以在Jenkins出现Sonarqube的图标和链接
  		- 给出一个参考配置
```
# unique project identifier (required)
sonar.projectKey=qweraqq:cknife

# project metadata (used to be required, optional since SonarQube 6.1)
sonar.projectName=cknife
sonar.projectVersion=1.0

# path to source directories (required)
sonar.sources=src/main

sonar.java.binaries=target/classes  
```


