# Docker Security

Docker安全可以从两个角度来说：
1. Docker自身的安全设计及安全机制
2. 企业如何正确安全地使用Docker

这里主要讨论第二个问题。材料主要来源于Docker的官方文档及官方会议资料。

有一本比较有意思的免费书籍 [https://scaledocker.com/](https://scaledocker.com/)
### Docker自身的安全设计
Docker自身的安全设计可以参考Docker官网上的这篇文章[https://docs.docker.com/engine/security/security/](https://docs.docker.com/engine/security/security/)


### 企业如何正确安全地使用Docker

##### 企业中Docker应用的四大安全需求
1. Docker镜像在持续集成部署(CI/CD pipeline)过程中的安全(Secure Supply Chain OR Docker content trust)
	- Docker镜像的安全扫描
		1. 防止Docker image中包含恶意代码(主要依靠数字签名)
		2. 防止Docker image包含通用型组件的漏洞:CVE
	- 数字签名
		1. 确保可信的Docker image
2. Docker运行状态下的安全(Runtime Security)
	-  持续的Docker镜像的安全扫描
		1. 持续检查Docker image包含通用型组件的漏洞(CVE)
		2. 可以定义发现CVE后的处置行为
	- 只运行具有可信签名的Docker image
	- 在镜像中启用一些运行态的安全机制(比如selinux, AppArmor)
	- 在一个容器中只启动一个服务(进程)
3. Docker运行设施的安全(Infrastructure Security)
	- 基础设施的系统配置
		1. Docker Bench for Security工具可以按照检测基础设施是否遵守了最佳的安全实践
		[https://github.com/docker/docker-bench-security](https://github.com/docker/docker-bench-security)
	- 管理手段
		1. 职责分离
4. 合规审计(Compliance)
	- 审计(操作)日志

##### 一些有用的开源工具
1. 开源的Docker镜像扫描器 
	- CORES clair: [https://github.com/coreos/clair](https://github.com/coreos/clair) 
		+ 局限性:类似于banner扫描，人工维护了主流image(比如操作系统)的漏洞信息，无法扫描比如自己编译的linux镜像
		+ 由于docker image layer的不可更改特性，所以扫描性能会比较高
2. Docker运行态
	- Cilium(Docker的NG iptables) [https://github.com/cilium/cilium](https://github.com/cilium/cilium)
	- TUF [https://github.com/theupdateframework/tuf](https://github.com/theupdateframework/tuf)
3. 基础设施的系统配置检查
	- Docker Bench for Security: [https://github.com/docker/docker-bench-security](https://github.com/docker/docker-bench-security)

# CORES clair
clair的部署架构为C/S
	- POSTGRES数据库服务,用于漏洞信息存储,数据源可以参考[https://github.com/coreos/clair/blob/master/Documentation/drivers-and-data-sources.md](https://github.com/coreos/clair/blob/master/Documentation/drivers-and-data-sources.md)
	- server端接收client端发送的layer信息并比对数据库
	- client调用server端的服务并进行结果展示
	


##### 使用[arminc/clair-local-scan](https://github.com/arminc/clair-local-scan)进行本地Docker镜像扫描
arminc维护了clair所需要的数据库(arminc/clair-db)并且根据官方不再维护的[analyze-local-images](https://github.com/coreos/analyze-local-images.git)开发了[clair-scanner](https://github.com/arminc/clair-scanner)

启动clair-local-scan，docker hub地址为[https://hub.docker.com/r/arminc/clair-local-scan](https://hub.docker.com/r/arminc/clair-local-scan)
```bash
docker run -d --name db arminc/clair-db:latest
docker run -p 6060:6060 --link db:postgres -d --name clair arminc/clair-local-scan:latest
```

下载clair-scanner的二进制包[https://github.com/arminc/clair-scanner/releases](https://github.com/arminc/clair-scanner/releases)并运行扫描
```bash
wget https://github.com/arminc/clair-scanner/releases/download/v12/clair-scanner_linux_amd64
mv clair-scanner_linux_amd64 clair-scanner
chmod +x clair-scanner
./clair-scanner --ip=YOUR_LOCAL_IP DOCKER_IAMGE_NAME
# EXAMPLE: ./clair-scanner --ip=127.0.0.1 -r result.json qweraqq/jenkins-with-maven:lts
```


##### 搭建独立的clair服务在CI/CD过程中进行镜像扫描

# Docker使用中遇到的一些问题
1. 已知的网络访问BUG：docker+防火墙的bug。docker无法访问本地宿主机网络中的服务(比如数据库)，必须在防火墙设置规则
[https://forums.docker.com/t/no-route-to-host-network-request-from-container-to-host-ip-port-published-from-other-container/39063/5](https://forums.docker.com/t/no-route-to-host-network-request-from-container-to-host-ip-port-published-from-other-container/39063/5)

ip地址修改为本地docker的网卡地址
```
 <rule family="ipv4">
     <source address="172.17.0.1/16"/>
     <accept/>
 </rule>
 ```
