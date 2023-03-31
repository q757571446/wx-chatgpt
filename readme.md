# 快速开始
前置条件：
* Python >= 3.6
* 安装微信[3.6.0.18版本](https://pan.baidu.com/s/1OFVmmmbrHTAqZUAE71tvyA?pwd=qka8)。
* 下载[version.dll](https://github.com/q757571446/WeixinClient-Python/blob/master/version.dll), 放入微信安装目录
## 安装
```
pip install wxchat
pip install openai
```

## 运行
1. 启动微信，弹出窗口，显示以下消息则运行成功
```
服务已启动, 端口号1: 10086, 端口号2: 10010
```

2. 填入openai的apikey，并运行main.py文件
```
openai.api_key = "input your apikey"
```


## 注意
如果微信运行在其他机器上，初始化client时请填入ip地址和端口号
```
client = WeixinClient("ip", port1, port2)
```



