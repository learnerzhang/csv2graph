### 说明文档

### 运行
python  production_app.py -p 1234


## Docker 运行

#### 编译镜像  
 docker build -t csv2graph .
 
#### 保存镜像

docker save -o csv2graph.tar csv2graph

 
#### 装载镜像tar  
docker load -i csv2graph.tar

#### 三种启动服务的方式(-p 指定端口号)

> 直接启动

docker run  csv2graph -p 1234

> 后台启动

docker run -d --net=host csv2graph -p 1234

> 挂着日志文件,后台启动, 需要在当前运行目录下建立docker_logs文件

docker run -d --net=host -v $(pwd)/docker_logs:/csv2graph/logs csv2graph -p 1234


## 部署步骤

* 加载镜像
    
    docker load -i csv2graph.tar
    
* 启动服务(需要在当前运行目录下创建 docker_logs; 第一个p本地端口到docker容器映射,第二p指定容器端口号)
    
    docker run -p 1234:1234 -v $(pwd)/docker_logs:/csv2graph/logs csv2graph -p 1234
    
    docker run -d -p 1234:1234 -v $(pwd)/docker_logs:/csv2graph/logs csv2graph -p 1234
    # 设置为8080
    docker run -d -p 8080:1134 -v $(pwd)/docker_logs:/csv2graph/logs csv2graph -p 1134
    
    
## python 离线安装

    pip install --no-index --find-links=file:///path_to/packages/dependences -r requirements.txt


## 打包项目

    tar -zcvf  csv2graph.tar.gz --exclude=csv2graph/dependences  csv2graph
