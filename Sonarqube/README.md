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

## 生产数据库配置方式
1. 安装数据库，注意官方文档中的数据库版本要求。对于LTS版本，可以使用centos7官方源中的postgresql版本。
```bash
sudo yum install postgresql-server postgresql-contrib # version 9.2.24
sudo postgresql-setup initdb
sudo passwd postgres # 设置密码
```
2. 配置数据库
```bash
su - postgres
createuser sonar
psql # 进入postgresql命令行
# 以下在psql中执行，注意修改密码
ALTER USER sonar WITH ENCRYPTED password 'SonarPassword';
CREATE DATABASE sonar WITH ENCODING 'UTF8' OWNER sonar TEMPLATE=template0;
\q # 执行完成退出psql
```
3. 允许docker(远程)访问数据库，可参考[https://support.plesk.com/hc/en-us/articles/115003321434-How-to-enable-remote-access-to-PostgreSQL-server-on-a-Plesk-server-](https://support.plesk.com/hc/en-us/articles/115003321434-How-to-enable-remote-access-to-PostgreSQL-server-on-a-Plesk-server-),这里注意找到本地docker的地址并对应修改。
4. 完成所有配置，运行sonarqube并进行相关配置。
```bash
docker run -d -p 9000:9000 -v sonar_home:/opt/sonarqube -e sonar.jdbc.username=sonar -e sonar.jdbc.password=SonarPassword -e sonar.jdbc.url=jdbc:postgresql://${宿主机ip}/sonar qweraqq/sonarqube
```