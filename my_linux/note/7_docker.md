
## docker

**`sudo usermod -aG docker $USER`**：将当前用户添加到`docker`用户组，可以省去`sudo`权限
**`newgrp docker`**：更新用户组

**`adduser user_name`**：添加用户`user_name`
**`usermod -aG sudo user_name`**：给用户`user_name`分配`sudo`权限

- **镜像(images)**
  - **`docker pull ubuntu:22.04`**：拉取一个镜像
  - **`docker images`**：列出本地所有镜像
  - **`docker image rm ubuntu:22.04`** 或 **`docker rmi ubuntu:22.04`**：删除镜像ubuntu:22.04
  - **`docker [container] commit CONTAINER IMAGE_NAME:TAG`**：创建某个`container`的镜像
  - **`docker save -o ubuntu_22_04.tar ubuntu:22.04`**：将镜像`ubuntu:22.04`导出到本地文件`ubuntu_22_04.tar`中
  - **`docker load -i ubuntu_22_04.tar`**：将镜像`ubuntu:22.04`从本地文件`ubuntu_22_04.tar`中加载出来
  
- **容器(container)**
  - **`docker [container] create -it ubuntu:22.04`**：利用镜像`ubuntu:22.04`创建一个容器
  - **`docker ps -a`**：：查看本地的所有容器
  - **`docker [container] start CONTAINER`**：启动容器
  - **`docker [container] stop CONTAINER`**：停止容器
  - **`docker [container] restart CONTAINER`**：重启容器
  - **`docker [contaienr] run -itd ubuntu:22.04`**：创建并启动一个容器(`-it`创建启动并进入)
  - **`docker [container] attach CONTAINER`**：进入容器
  - **`docker [container] exec CONTAINER COMMAND`**：在容器中执行命令
  - **`docker [container] rm CONTAINER`**：删除容器
  - **`docker container prune`**：删除所有已停止的容器
  - **`docker export -o xxx.tar CONTAINER`**：将容器`CONTAINER`导出到本地文件`xxx.tar`中
  - **`docker import xxx.tar image_name:tag`**：将本地文件`xxx.tar`导入成镜像，并将镜像命名为`image_name:tag`
  - **`docker export/import`** 与 **`docker save/load的区别`**：
    - `export/import`会丢弃历史记录和元数据信息，仅保存容器当时的快照状态
    - `save/load`会保存完整记录，体积更大
  - **`docker top CONTAINER`**：查看某个容器内的所有进程
  - **`docker stats`**：查看所有容器的统计信息，包括CPU、内存、存储、网络等信息
  - **`docker cp xxx CONTAINER:xxx`**：在本地和容器间复制文件(可逆)
  - **`docker rename CONTAINER1 CONTAINER2`**：重命名容器
  - **`docker update CONTAINER --memory 500MB`**：修改容器限制
  - **`docker run -p 1314:22 --name ubuntu_docker -it ubuntu:22.4`**：创建运行并进入`ubuntu_docker`，映射`22`端口为`1314`
  - **`Ctrl + p, Ctrl + q`**：挂起容器
  - **`docker cp -L /usr/share/zoneinfo/Asia/Shanghai  [容器名]:/etc/localtime`**: 同步容器时间
