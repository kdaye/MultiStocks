# MultiStocks


这个docker实现了多出口多入口的stocks5

## 简介

使用metacubex/mihomo官方镜像，增加了针对订阅url转化成配置文件。
目前只接受clash订阅yaml内容，其他内容请自行转换 [subconverter](https://github.com/tindy2013/subconverter)

## 使用方法
拉取docker

`docker pull keol/multistocks`

`docker run -e CONFIG_URL="http://example.com/config.yaml" -e START_PORT=40000 -p 40000-40010:40000-40010 kdaye/multistocks`



修改参数下面的参数
```
# 订阅地址
CONFIG_URL="http://example.com/config.yaml"
# 端口从40000开始
START_PORT=40000
# 如果预计有10个节点那么端口将开放40000到40010
-p 40000-40010:40000-40010 
```



### 本地使用
#### 生成docker
```
git clone https://github.com/kdaye/MultiStocks.git
docker build -t multistocks .
```
#### 使用方法
```
docker run -e CONFIG_URL="http://example.com/config.yaml" -e START_PORT=40000 -p 40000-40010:40000-40010 multistocks
```
