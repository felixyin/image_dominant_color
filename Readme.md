
# 5种不同的方式获取图片主要颜色

## 采用python编写，用thrift封装为服务端
    下载后，用pycharm打开 image_dominat_color即可
    virtualenv venv
    source even/bin/active
    pip install -Ur requirements.txt
    
## 客户端采用php编写
    下载后，用phpstorm打开 thrift_client_php
    composer require apache/thrift
    或者
    compose install
    
## thrift生成py和php代码
    brew install thrift 
    thrift -r --gen py imagecolor.thrift
    thrift -r --gen php imagecolor.thrift