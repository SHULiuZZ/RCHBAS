! [Python version]（ https://img.shields.io/badge/python-3.8 +-Orange. svg)
! [GitHub forks]（ https://img.shields.io/github/forks/yeyupiaoling/PPASR ）
! [GitHub Repo stars]（ https://img.shields.io/github/stars/yeyupiaoling/PPASR ）
! [GitHub]（ https://img.shields.io/github/license/yeyupiaoling/PPASR ）
! [Support System]（ https://img.shields.io/badge/ Support System - Win/Linux/MAC-9cm)
**The environment used in this project:**
-Anaconda 3
-Python 3.8
-PaddlePaddle 2.3.2
-Windows 10 or Ubuntu 18.04
##Model Download
This project supports streaming recognition models such as' deepspeech2 'and' deepspeech2 '_ Big `, non streaming model ` deepspeech2_ No_ Stream, deepspeech2_ Big_ No_ Stream `.
|Usage Model | Dataset | Preprocessing Method | Parameter Size (M) ` * ` | Language | Test Set Word Error Rate (Word Error Rate) | Download Address|
|: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --|
|Deepspeech2_ Big | [WenetSpeech] (./docs/wenetspeech. md) (10000 hours) | fbank | 167 | Chinese | 0.07392 (test set for AIShell) | [Click to download]（ https://pan.baidu.com/s/1DDU92HGH3RRMySBfroXz5w?pwd=ai6p ）|
|Deepspeech2 | [aishell]（ https://openslr.magicdatatech.com/resources/33 ）(179 hours) | fbank | 35 | Chinese | 0.07280 | [Click to download]（ https://pan.baidu.com/s/1KFRDIxxlW092Ad70-TNKlw?pwd=m0e0 ）|
|Deepspeech2_ Big | [aishell]（ https://openslr.magicdatatech.com/resources/33 ）(179 hours) | fbank | 167 | Chinese | 0.05370 | [Click to download]（ https://pan.baidu.com/s/1KFRDIxxlW092Ad70-TNKlw?pwd=m0e0 ）|
|Deepspeech2_ No_ Stream | [aishell]（ https://openslr.magicdatatech.com/resources/33 ）(179 hours) | fbank | 98 | Chinese | 0.07253 | [Click to download]（ https://pan.baidu.com/s/1KFRDIxxlW092Ad70-TNKlw?pwd=m0e0 ）|
|Deepspeech2 | [Librispeech]（ https://openslr.magicdatatech.com/resources/12 ）(960 hours) | fbank | 35 | English | 0.16369 | [Click to download]（ https://download.csdn.net/download/qq_33200967/77978970 ）|
|Deepspeech2_ Big | [Librispeech]（ https://openslr.magicdatatech.com/resources/12 ）(960 hours) | fbank | 167 | English | 0.12779 | [Click to download]（ https://pan.baidu.com/s/1xfVPDuOAA3rc_6_1JaR5QQ?pwd=673u ）|
|Deepspeech2_ No_ Stream | [Librispeech]（ https://openslr.magicdatatech.com/resources/12 ）(960 hours) | fbank | 98 | English | 0.09131 | [Click to download]（ https://pan.baidu.com/s/1xfVPDuOAA3rc_6_1JaR5QQ?pwd=673u ）|
-----------Configuration file parameters-----------
Ctc_ Beam_ Search_ Decoder: {'alpha ': 2.2,' beta ': 4.3,' beam_size ': 300,' num_processes': 10, 'cutoff process': 0.99,' cutoff topn ': 40,' language model path ':' lm/zh_giga. no_cna_cmn. rune01244. klm '}
Dataset: {'batch size ': 32,' num workers': 4, 'min_duration': 0.5, 'max_duration': 20, 'train_manifest': 'dataset/manifest. train', 'test_manifest': 'dataset/manifest. test', 'dataset vocab': 'dataset/vocabulary. txt', 'mean_std_path': 'dataset/mean_std. json', 'noise_manifest_path': 'dataset/manifest. noise_manifest' se '}
Decoder: ctc_ Beam_ Search
Metrics_ Type: cer
Num_ Epoch: 65
Optimizer: {'learning rate ':' 5e-5 ',' gamma ': 0.93,' clip norm ': 3.0,' weight_decay ':' 1e-6 '}
Preprocess: {'feature_method ':' fbank ',' n_mels': 80, 'n_mfcc': 40, 'sample_rate': 16000, 'used_Bnormalization': True, 'target_dB': -20}
Use_ Model: deepspeech2
------------------------------------------------
Consumption time: 132, recognition result: In recent years, not only have I used books to send New Year's greetings to my daughter, but I also advised my family and friends not to give her New Year's money and instead send New Year's greetings books. Score: 94
```
-Long speech prediction
```Shell script
Python Infer_ Path. py -- wav_ Path=/ Dataset/test_ Vad. wav -- is_ Long_ Audio=True
```
##Reference materials
- https://github.com/PaddlePaddle/PaddleSpeech
- https://github.com/jiwidi/DeepSpeech-pytorch
- https://github.com/wenet-e2e/WenetSpeech
