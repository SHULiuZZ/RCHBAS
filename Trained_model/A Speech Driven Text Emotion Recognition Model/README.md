![python version](https://img.shields.io/badge/python-3.8+-orange.svg)
![GitHub forks](https://img.shields.io/github/forks/yeyupiaoling/PPASR)
![GitHub Repo stars](https://img.shields.io/github/stars/yeyupiaoling/PPASR)
![GitHub](https://img.shields.io/github/license/yeyupiaoling/PPASR)
![支持系统](https://img.shields.io/badge/支持系统-Win/Linux/MAC-9cf)



## 在线使用

**1. [在AI Studio平台训练预测](https://aistudio.baidu.com/aistudio/projectdetail/3290199)**

<!-- **2. [在线使用Dome](https://ppasr.yeyupiaoling.cn)** -->

<br/>

**本项目使用的环境：**
 - Anaconda 3
 - Python 3.8
 - PaddlePaddle 2.3.2
 - Windows 10 or Ubuntu 18.04




## 模型下载

本项目支持流式识别模型`deepspeech2`、`deepspeech2_big`，非流式模型`deepspeech2_no_stream`、`deepspeech2_big_no_stream`。

|         使用模型          |                                  数据集                                  | 预处理方式 | 参数大小（M）`*` | 语言  |     测试集字错率（词错率）      |                               下载地址                               |
|:---------------------:|:---------------------------------------------------------------------:|:-----:|:----------:|:---:|:--------------------:|:----------------------------------------------------------------:|
|    deepspeech2_big    |            [WenetSpeech](./docs/wenetspeech.md) (10000小时)             | fbank |    167     | 中文  | 0.07392(AIShell的测试集) | [点击下载](https://pan.baidu.com/s/1DDU92HGH3RRMySBfroXz5w?pwd=ai6p) |
|      deepspeech2      |   [aishell](https://openslr.magicdatatech.com/resources/33) (179小时)   | fbank |     35     | 中文  |       0.07280        | [点击下载](https://pan.baidu.com/s/1KFRDIxxlW092Ad70-TNKlw?pwd=m0e0) |
|    deepspeech2_big    |   [aishell](https://openslr.magicdatatech.com/resources/33) (179小时)   | fbank |    167     | 中文  |       0.05370        | [点击下载](https://pan.baidu.com/s/1KFRDIxxlW092Ad70-TNKlw?pwd=m0e0) |
| deepspeech2_no_stream |   [aishell](https://openslr.magicdatatech.com/resources/33) (179小时)   | fbank |     98     | 中文  |       0.07253        | [点击下载](https://pan.baidu.com/s/1KFRDIxxlW092Ad70-TNKlw?pwd=m0e0) |
|      deepspeech2      | [Librispeech](https://openslr.magicdatatech.com/resources/12) (960小时) | fbank |     35     | 英文  |       0.16369        | [点击下载](https://download.csdn.net/download/qq_33200967/77978970)  | 
|    deepspeech2_big    | [Librispeech](https://openslr.magicdatatech.com/resources/12) (960小时) | fbank |    167     | 英文  |       0.12779        | [点击下载](https://pan.baidu.com/s/1xfVPDuOAA3rc_6_1JaR5QQ?pwd=673u) | 
| deepspeech2_no_stream | [Librispeech](https://openslr.magicdatatech.com/resources/12) (960小时) | fbank |     98     | 英文  |       0.09131        | [点击下载](https://pan.baidu.com/s/1xfVPDuOAA3rc_6_1JaR5QQ?pwd=673u) | 



----------- 配置文件参数 -----------
ctc_beam_search_decoder: {'alpha': 2.2, 'beta': 4.3, 'beam_size': 300, 'num_processes': 10, 'cutoff_prob': 0.99, 'cutoff_top_n': 40, 'language_model_path': 'lm/zh_giga.no_cna_cmn.prune01244.klm'}
dataset: {'batch_size': 32, 'num_workers': 4, 'min_duration': 0.5, 'max_duration': 20, 'train_manifest': 'dataset/manifest.train', 'test_manifest': 'dataset/manifest.test', 'dataset_vocab': 'dataset/vocabulary.txt', 'mean_std_path': 'dataset/mean_std.json', 'noise_manifest_path': 'dataset/manifest.noise'}
decoder: ctc_beam_search
metrics_type: cer
num_epoch: 65
optimizer: {'learning_rate': '5e-5', 'gamma': 0.93, 'clip_norm': 3.0, 'weight_decay': '1e-6'}
preprocess: {'feature_method': 'fbank', 'n_mels': 80, 'n_mfcc': 40, 'sample_rate': 16000, 'use_dB_normalization': True, 'target_dB': -20}
use_model: deepspeech2
------------------------------------------------

消耗时间：132, 识别结果: 近几年不但我用书给女儿儿压岁也劝说亲朋不要给女儿压岁钱而改送压岁书, 得分: 94
```


 - 长语音预测

```shell script
python infer_path.py --wav_path=./dataset/test_vad.wav --is_long_audio=True
```



## 参考资料
 - https://github.com/PaddlePaddle/PaddleSpeech
 - https://github.com/jiwidi/DeepSpeech-pytorch
 - https://github.com/wenet-e2e/WenetSpeech
