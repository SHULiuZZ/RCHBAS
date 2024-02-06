##Minimum software and hardware requirements for training models
###Hardware
*CPU: 4-core (x86_64, amd64)+
*RAM: 16 GB+
*GPU: NVIDIA, Graph Memory 11GB+(starting from 1080ti)
*Hard drive: 500 GB mechanical hard drive (or solid-state drive)
###Software
*Linux: Ubuntu 18.04+/CentOS 7+
*Python: 3.6+
*TensorFlow: 1.15, 2. x+(it is not recommended to use the latest and larger versions of x.x.0)
##Quick Start
Taking the operation under Linux system as an example:
Firstly, clone this project onto your computer through Git, and then download the dataset required for training this project. Please refer to the download link at the end of the document（ https://github.com/nl8590687/ASRT_SpeechRecognition#data -Sets -% E6% 95% B0% E6% 8D% AE% E9% 9B% 86).
```Shell
$git clone https://github.com/nl8590687/ASRT_SpeechRecognition.git
```
Alternatively, you can use the "Fork" button to make a copy of this project and then clone it locally using your own SSH key.
After cloning the repository through git, enter the project root directory; And create a subdirectory for storing data, such as `/data/speed '_ Data ` (can be replaced by a soft link), and then extract the downloaded dataset directly into it
Note that in the current version, six datasets, Thchs30, ST-CMDS, Primewords, aishell-1, aidatatang200, and MagicData, have been added by default in the configuration file. If not needed, please delete them yourself. If you want to use other datasets, you need to add your own data configuration and organize the data in advance using the standard format supported by ASRT.
```Shell
$cd ASRT_ SpeedRecognition
$mkdir/data/speed_ Data
$tar zxf<dataset compressed file name>- C/data/speed_ Data/
```
Download the pinyin label file for the default dataset:
```Shell
$Python download_ Default_ Datalist.py
```
The currently available models are 24, 25, 251, and 251bn
Before running this project, please install the necessary [Python 3 version dependency libraries]（ https://github.com/nl8590687/ASRT_SpeechRecognition#python -Import
To begin training for this project, please execute:
```Shell
$python3 train_ Speech_ Model. py
```
Please execute the following steps to start testing this project:
```Shell
$python3 evaluate_ Speech_ Model. py
```
Before testing, please ensure that the model file path filled in the code exists.
Predicting speech recognition text for a single audio file:
```Shell
$python3 predict_ Speech_ File.py
```
To start the ASRT API server, please execute:
```Shell
$python3 asrserver_ Http. py
```
Whether the local test call to API service was successful:
```Shell
$python3 client_ Http. py
```
Please note that after opening the API server, you need to use the client software corresponding to this ASRT project for speech recognition. Please refer to the Wiki documentation for details. [Download ASRT Speech Recognition Client SDK and Demo]（ https://wiki.ailemon.net/docs/asrt-doc/download ）.
If you want to train and use a non 251bn version of the model, please use the ` import speech 'in the code_ Model_ Make modifications to the corresponding position of 'zoo'.
Deploy ASRT directly using Docker:
```Shell
Docker pull ailemondocker/asrt_ Service: 1.2.0
$Docker run -- rm - it - p 20001:20001-- name asrt server - d ailemondocker/asrt_ Service: 1.2.0
```
CPU only runs inference recognition without training
##Model
###Speech Model
DCNN+CTC
Among them, the maximum time length of the input audio is 16 seconds, and the output is the corresponding Chinese Pinyin sequence
*Regarding the issue of downloading pre trained models
The trained model is included in the compressed package of the released server program. The released finished server program can be downloaded here: [ASRT Download Page]（ https://wiki.ailemon.net/docs/asrt-doc/download ）.
Github's warehouse [Releases]（ https://github.com/nl8590687/ASRT_SpeechRecognition/releases ）The page also includes introduction information for different versions, and the zip file below each version also contains compressed versions of the pre trained model's published server program.
###Language Model
Maximum Entropy Hidden Markov Model Based on Probability Graph
Input as Chinese Pinyin sequence, output as corresponding Chinese text
##Python dependency libraries
*TensorFlow (1.15-2. x)
*Numpy
*Wave
*Matplotlib
*Math
*Scipy
*Requests
*Flask
*Waitress
Run the following command directly (provided that there is a GPU and CUDA 11.2 and cudnn 8.1 are already installed):
```Shell
$pip install - r requirements. txt
```
[Dependent environment and performance configuration requirements]（ https://wiki.ailemon.net/docs/asrt-doc/asrt-doc-1deobk7bmlgd6 ）
##Data Sets
For complete content, please refer to: [Several latest free and open-source Chinese voice datasets]（ https://blog.ailemon.net/2018/11/21/free-open-source-chinese-speech-datasets/ ）
|Dataset | Duration | Size | Download 1 | Download 2|
|-|-|-|-|-|
|THCHS30 | 40h | 6.01G | [data_thchs30. tgz]< http://openslr.magicdatatech.com/resources/18/data_thchs30.tgz >| [data_thchs30. tgz]< http://www.openslr.org/resources/18/data_thchs30.tgz >)|
|ST-CMDS | 100h | 7.67G | [ST-CMDS-20170001_1 OS. tar. gz]< http://openslr.magicdatatech.com/resources/38/ST-CMDS-20170001_1-OS.tar.gz >ST-CMDS-20170001_1 OS. tar. gz< http://www.openslr.org/resources/38/ST-CMDS-20170001_1-OS.tar.gz >)|
|AIShell 1 | 178h | 14.51G | [data.aishell. tgz] (< http://openslr.magicdatatech.com/resources/33/data_aishell.tgz >) | [data-aishell. tgz] (< http://www.openslr.org/resources/33/data_aishell.tgz >)|
|Primewords | 100h | 8.44G | [primewords md_2018_set1. tar. gz]< http://openslr.magicdatatech.com/resources/47/primewords_md_2018_set1.tar.gz >) | [primewords_md_2018_set1. tar. gz]< http://www.openslr.org/resources/47/primewords_md_2018_set1.tar.gz >)|
|Aidatang_ 200zh | 200h | 17.47G | [aidatang_200zh. tgz]< http://openslr.magicdatatech.com/resources/62/aidatatang_200zh.tgz >[aidatatang_200zh. tgz]< http://www.openslr.org/resources/62/aidatatang_200zh.tgz >)|
|MagicData | 755h | 52G/1.0G/2.2G | [train_set. tar. gz]< http://openslr.magicdatatech.com/resources/68/train_set.tar.gz >)/[dev_set. tar. gz] (< http://openslr.magicdatatech.com/resources/68/dev_set.tar.gz >()/[test_set. tar. gz] (< http://openslr.magicdatatech.com/resources/68/test_set.tar.gz >| [train_set. tar. gz]< http://www.openslr.org/resources/68/train_set.tar.gz >)/[dev_set. tar. gz] (< http://www.openslr.org/resources/68/dev_set.tar.gz >()/[test_set. tar. gz] (< http://www.openslr.org/resources/68/test_set.tar.gz >)|
Note: AISHELL-1 dataset decompression method
```
$tar xzf data_ Aishell.tgz
$cd data_ Aishell/wav
$for tar in *. tar. gz; Do tar xvf $tar; Done
```
If the provided dataset link cannot be opened and downloaded, please click on the link [OpenSLR]（ http://www.openslr.org ）
