# Sonarqube

## 使用方式
```docker run -d -p 9000:9000 sonarqube:lts```

注意:
* docker方式使用了H2内存数据库，无法直接用于生产，可参考[https://stackoverflow.com/questions/38817344/how-to-persist-configuration-analytics-across-container-invocations-in-sonarqu](https://stackoverflow.com/questions/38817344/how-to-persist-configuration-analytics-across-container-invocations-in-sonarqu)配置数据库