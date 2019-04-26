# Sonarqube

## 说明
Sonarqube官方Docker镜像中缺少一些插件

创建了基于官方docker镜像的Sonarqube-with-plugins的dockerfile

Dockerfile持续更新中


## 使用方式
```docker run -d -p 9000:9000 qweraqq/sonarqube```

或者
```docker run -d -p 9000:9000 sonarqube:lts```

注意:
* docker方式使用了H2内存数据库，无法直接用于生产，可参考[https://stackoverflow.com/questions/38817344/how-to-persist-configuration-analytics-across-container-invocations-in-sonarqu](https://stackoverflow.com/questions/38817344/how-to-persist-configuration-analytics-across-container-invocations-in-sonarqu)配置数据库