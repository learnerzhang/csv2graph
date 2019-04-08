### 说明文档

### 运行
python  production_app.py -p 1234


## Docker 运行

#### 编译镜像  
 docker build -t csv2graph .

#### 装载镜像tar  
docker load -i csv2graph.tar

#### 三种启动服务的方式(-p 指定端口号)

> 直接启动

docker run  csv2graph -p 2234

> 后台启动

docker run -d --net=host csv2graph -p 2234

> 挂着日志文件,后台启动, 需要在当前运行目录下建立docker_logs文件

docker run -d --net=host -v $(pwd)/docker_logs:/csv2graph/logs csv2graph -p 1234



## 部署步骤

* 加载镜像
    
    docker load -i csv2graph.tar
    
* 启动服务(需要在当前运行目录下创建 docker_logs; -p 指定端口号)
    
    docker run -d --net=host -v $(pwd)/docker_logs:/csv2graph/logs csv2graph -p 1234