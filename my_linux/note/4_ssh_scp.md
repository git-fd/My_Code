
## ssh and scp

### ssh

- **基本用法**

        ssh user@HostName
            user        # 用户名
            HostName    # ip地址或者域名

- **默认端口为 22**  **`ssh user@HostName -p 22`**

- **配置文件**
    创建文件`~/.ssh/config`

        Host myserver       # 配置完成可直接使用 ssh myserver 登录
            HostName    ip
            User        name
        ......

- **密钥登录**
  **`ssh-keygen`**
  在`~/.ssh/`下出现两个文件
  - `id_rsa`:私钥
  - `id_rsa.pub`:公钥
    持有公钥的机器可以被持有私钥的机器免密登录
  - **`ssh-copy-id myserver`**:一键配置免密登录

- **远程执行命令**
  **`ssh user@HostName command`**

      ssh myserver ll -a`
      a=1
      ssh myserver  "echo $a"   # 双引号是在本地服务器进行转义了，所以传过去命令不是echo $a，而是echo 1
      ssh myserver  'echo $a'   # 单引号不进行转义，传过去的是echo $a

### scp

- **基本用法** **`scp source user@HostName:destination`** 将`source`路径下的文件复制到远程机器的`destination`

- **复制多个文件** **`scp source1 ... user@HostName:destination`**

- **复制文件夹** **`scp -r ~/tmp myserver:~/`** 将本地家目录中的tmp文件夹复制到myserver服务器家目录下

- **指定端口** **`scp -P 22 source ... myserver:destination`**

- ***可反向复制***
