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
