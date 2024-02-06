




## Introduction 简介

本项目使用tensorFlow.keras基于深度卷积神经网络和长短时记忆神经网络、注意力机制以及CTC实现。

## 训练模型的最低软硬件要求
### 硬件
* CPU: 4核 (x86_64, amd64) +
* RAM: 16 GB +
* GPU: NVIDIA, Graph Memory 11GB+ (1080ti起步)
* 硬盘: 500 GB 机械硬盘(或固态硬盘)

### 软件
* Linux: Ubuntu 18.04 + / CentOS 7 +
* Python: 3.6 +
* TensorFlow: 1.15, 2.x + (不建议使用最新版和大版本的x.x.0版)

## 快速开始

以在Linux系统下的操作为例：

首先通过Git将本项目克隆到您的计算机上，然后下载本项目训练所需要的数据集，下载链接详见[文档末尾部分](https://github.com/nl8590687/ASRT_SpeechRecognition#data-sets-%E6%95%B0%E6%8D%AE%E9%9B%86)。
```shell
$ git clone https://github.com/nl8590687/ASRT_SpeechRecognition.git
```

或者您也可以通过 "Fork" 按钮，将本项目Copy一份副本，然后通过您自己的SSH密钥克隆到本地。

通过git克隆仓库以后，进入项目根目录；并创建一个存储数据的子目录， 例如 `/data/speech_data` (可使用软链接代替)，然后将下载好的数据集直接解压进去

注意，当前版本中，在配置文件里，默认添加了Thchs30、ST-CMDS、Primewords、aishell-1、aidatatang200、MagicData 六个数据集，如果不需要请自行删除。如果要使用其他数据集需要自行添加数据配置，并提前使用ASRT支持的标准格式整理数据。

```shell
$ cd ASRT_SpeechRecognition

$ mkdir /data/speech_data

$ tar zxf <数据集压缩文件名> -C /data/speech_data/ 
```

下载默认数据集的拼音标签文件：
```shell
$ python download_default_datalist.py
```

目前可用的模型有24、25、251和251bn

运行本项目之前，请安装必要的[Python3版依赖库](https://github.com/nl8590687/ASRT_SpeechRecognition#python-import)

本项目开始训练请执行：
```shell
$ python3 train_speech_model.py
```
本项目开始测试请执行：
```shell
$ python3 evaluate_speech_model.py
```
测试之前，请确保代码中填写的模型文件路径存在。

预测单条音频文件的语音识别文本：
```shell
$ python3 predict_speech_file.py
```

ASRT API服务器启动请执行：
```shell
$ python3 asrserver_http.py
```

本地测试调用API服务是否成功：
```shell
$ python3 client_http.py
```

请注意，开启API服务器之后，需要使用本ASRT项目对应的客户端软件来进行语音识别，详见Wiki文档[下载ASRT语音识别客户端SDK和Demo](https://wiki.ailemon.net/docs/asrt-doc/download)。

如果要训练和使用非251bn版模型，请在代码中 `import speech_model_zoo` 的相应位置做修改。

使用docker直接部署ASRT：
```shell
$ docker pull ailemondocker/asrt_service:1.2.0
$ docker run --rm -it -p 20001:20001 --name asrt-server -d ailemondocker/asrt_service:1.2.0
```
仅CPU运行推理识别，不作训练

## Model 模型

### Speech Model 语音模型

DCNN + CTC

其中，输入的音频的最大时间长度为16秒，输出为对应的汉语拼音序列

* 关于下载已经训练好的模型的问题

已经训练好的模型包含在发布版服务端程序压缩包里面，发布版成品服务端程序可以在此下载：[ASRT下载页面](https://wiki.ailemon.net/docs/asrt-doc/download)。

Github本仓库下[Releases](https://github.com/nl8590687/ASRT_SpeechRecognition/releases)页面里面还包括各个不同版本的介绍信息，每个版本下方的zip压缩包也是包含已经训练好的模型的发布版服务端程序压缩包。

### Language Model 语言模型

基于概率图的最大熵隐马尔可夫模型

输入为汉语拼音序列，输出为对应的汉字文本

## About Accuracy 关于准确率

当前，最好的模型在测试集上基本能达到85%的汉语拼音正确率

## Python依赖库

* tensorFlow (1.15 - 2.x)
* numpy
* wave
* matplotlib
* math
* scipy
* requests
* flask
* waitress

不会安装环境的同学请直接运行以下命令(前提是有GPU且已经安装好 CUDA 11.2 和 cudnn 8.1)：

```shell
$ pip install -r requirements.txt
```

[依赖环境和性能配置要求](https://wiki.ailemon.net/docs/asrt-doc/asrt-doc-1deobk7bmlgd6)

## Data Sets 数据集

完整内容请查看：[几个最新免费开源的中文语音数据集](https://blog.ailemon.net/2018/11/21/free-open-source-chinese-speech-datasets/)

|数据集|时长|大小|下载1|下载2|
|-|-|-|-|-|
|THCHS30|40h|6.01G|[data_thchs30.tgz](<http://openslr.magicdatatech.com/resources/18/data_thchs30.tgz>)|[data_thchs30.tgz](<http://www.openslr.org/resources/18/data_thchs30.tgz>)|
|ST-CMDS|100h|7.67G|[ST-CMDS-20170001_1-OS.tar.gz](<http://openslr.magicdatatech.com/resources/38/ST-CMDS-20170001_1-OS.tar.gz>)|[ST-CMDS-20170001_1-OS.tar.gz](<http://www.openslr.org/resources/38/ST-CMDS-20170001_1-OS.tar.gz>)|
|AIShell-1|178h|14.51G|[data_aishell.tgz](<http://openslr.magicdatatech.com/resources/33/data_aishell.tgz>)|[data_aishell.tgz](<http://www.openslr.org/resources/33/data_aishell.tgz>)|
|Primewords|100h|8.44G|[primewords_md_2018_set1.tar.gz](<http://openslr.magicdatatech.com/resources/47/primewords_md_2018_set1.tar.gz>)|[primewords_md_2018_set1.tar.gz](<http://www.openslr.org/resources/47/primewords_md_2018_set1.tar.gz>)|
|aidatatang_200zh|200h|17.47G|[aidatatang_200zh.tgz](<http://openslr.magicdatatech.com/resources/62/aidatatang_200zh.tgz>)|[aidatatang_200zh.tgz](<http://www.openslr.org/resources/62/aidatatang_200zh.tgz>)|
|MagicData|755h|52G/1.0G/2.2G| [train_set.tar.gz](<http://openslr.magicdatatech.com/resources/68/train_set.tar.gz>) / [dev_set.tar.gz](<http://openslr.magicdatatech.com/resources/68/dev_set.tar.gz>) / [test_set.tar.gz](<http://openslr.magicdatatech.com/resources/68/test_set.tar.gz>)|[train_set.tar.gz](<http://www.openslr.org/resources/68/train_set.tar.gz>) / [dev_set.tar.gz](<http://www.openslr.org/resources/68/dev_set.tar.gz>) / [test_set.tar.gz](<http://www.openslr.org/resources/68/test_set.tar.gz>)|

  注：AISHELL-1 数据集解压方法

  ```
  $ tar xzf data_aishell.tgz
  $ cd data_aishell/wav
  $ for tar in *.tar.gz;  do tar xvf $tar; done
  ```



如果提供的数据集链接无法打开和下载，请点击该链接 [OpenSLR](http://www.openslr.org)


