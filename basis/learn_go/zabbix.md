基于web界面的提供分布式系统监视，以及网络监视功能的企业级的开源解决方案。
#### 1 Zabbix 简介 ####
**Zabbix agent**
一个部署在监控对象上的，能够主动监控本地资源和应用的程序；通过 TCP 连接到 proxy/server。
默认将数据发送至 server：
`no active checks on server [127.0.0.1:10051]: host [Zabbix server] not found`
修改 `zabbix_agent.conf` 的字段 `Hostname=Zabbix proxy` 后，agent 将数据发送至 proxy。 

**Zabbix proxy**
一个帮助Zabbix Server收集数据，分担Zabbix Server的负载的程序；通过 TCP 连接到 server。
- 是从一个或多个受监控设备收集监控数据，并将信息发送到 zabbix server 的**进程**，所有收集的数据都缓存在本地，然后传送到 proxy 所属的 server；
- 由 proxy 收集数据，建立 TCP 连接发送到 server，能减少 server 上的CPU消耗和磁盘IO负载，从而分担单个 server 的负载；
- 需要使用独立的数据库，是完成远程区域、分支机构、没有本地管理员的网络的集中监控的理想解决方案。

**Zabbix server**
Zabbix软件实现监控的核心程序，主要功能是与Zabbix proxies和Zabbix agents进行交互、触发器计算、发送告警通知；并将数据集中保存等。

#### 2 agent、proxy、server 的安装、运行 ####
**config zabbix repo**
```
# vi /etc/yum.repos.d/zabbix.repo
[zabbix]
name=zabbix
baseurl=http://repo.zabbix.com/zabbix/3.4/rhel/6/x86_64/
gpgcheck=0
enabled=1
[zabbix-deprecated]
enabled=1
```
**zabbix agent**
```
yum install zabbix-agent
service zabbix-agent start
service zabbix-agent stop
```
**zabbix proxy**
```
yum install zabbix-proxy-mysql
# create database
mysql -uroot -p
mysql > create database zabbix character set utf8 collate utf8_bin;
mysql > grant all privileges on zabbix.* to zabbix@localhost identified by 'zabbix';
mysql > quit;
# import data
zcat /usr/share/doc/zabbix-proxy-mysql-3.4.12/schema.sql.gz | mysql -uzabbix -p zabbix
# vi /etc/zabbix/zabbix_proxy.conf
DBHost=localhost
DBName=zabbix
DBUser=zabbix
DBPassword=zabbix

service zabbix-proxy start
service zabbix-proxy stop
```
**zabbix server**
```
# upgrade php version (> 5.4.0) on centos6
rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm
yum --enablerepo=remi install php php-fpm -y
php -v (5.4.45)

yum install zabbix-server-mysql
yum install zabbix-web
rpm -ql zabbix-web | grep example.conf

service zabbix-server start
service zabbix-server stop
```
