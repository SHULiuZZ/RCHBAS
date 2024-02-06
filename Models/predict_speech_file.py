#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2016-2099 Ailemon.net
#
# This file is part of ASRT Speech Recognition Tool.
#
# ASRT is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# ASRT is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ASRT.  If not, see <https://www.gnu.org/licenses/>.
# ============================================================================

"""
@author: nl8590687
用于通过ASRT语音识别系统预测一次语音文件的程序
"""

import os

from speech_model import ModelSpeech
from speech_model_zoo import SpeechModel251BN
from speech_features import Spectrogram
from language_model3 import ModelLanguage
import tensorflow as tf
config = tf.compat.v1.ConfigProto()
# 配置GPU内存分配方式，按需增长，很关键
config.gpu_options.allow_growth = True
# 在创建session的时候把config作为参数传进去
session = tf.compat.v1.InteractiveSession(config=config)


# config = tf.compat.v1.ConfigProto()
# config.gpu_options.per_process_gpu_memory_fraction = 0.5  # 控制占用显卡最高显存为50%， 这个提供多人使用
# config.gpu_options.allow_growth = True  # 设置动态分配GPU
# os.environ["CUDA_VISIBLE_DEVICES"] = '0'  # 使用编号为0 的显卡

global predicttext


import torch
import argparse
import numpy as np
from transformers import AutoModelForSequenceClassification, AutoTokenizer
global emotiontext
import time


def emotional(emotionaltext):
    # args = parse_args()
    # device = torch.device(args.device)
    device = torch.device("cpu")
    model = AutoModelForSequenceClassification.from_pretrained('bert-base-chinese', num_labels=6)
    print(f'Loading checkpoint:  ...')
    # checkpoint = torch.load(args.model_path)
    checkpoint = torch.load('wb/best.pt', map_location='cpu')
    missing_keys, unexpected_keys = model.load_state_dict(checkpoint['state_dict'], strict=True)
    # print(f'missing_keys: {missing_keys}\n'
    #       f'===================================================================\n')
    # print(f'unexpected_keys: {unexpected_keys}\n'
    #       f'===================================================================\n')

    label = {0: '快乐', 1: '愤怒', 2: '悲伤', 3: '恐惧', 4: '惊讶', 5: '中性'}
    tokenizer = AutoTokenizer.from_pretrained('bert-base-chinese')
    token = tokenizer(emotionaltext, padding='max_length', truncation=True, max_length=140)
    # token = tokenizer(args.input, padding='max_length', truncation=True, max_length=140)
    input_ids = torch.tensor(token['input_ids']).unsqueeze(0)
    model.eval()
    model.to(device)
    input_ids.to(device)
    with torch.no_grad():
        output = model(input_ids)
    pred = np.argmax(output.logits.detach().cpu().numpy(), axis=1).tolist()[0]
    print(f'##################### result: {label[pred]} #####################')
    return label[pred]
# '''



os.environ["CUDA_VISIBLE_DEVICES"] = "0"

AUDIO_LENGTH = 1600
AUDIO_FEATURE_LENGTH = 200
CHANNELS = 1
# 默认输出的拼音的表示大小是1428，即1427个拼音+1个空白块
OUTPUT_SIZE = 1428
sm251bn = SpeechModel251BN(
    input_shape=(AUDIO_LENGTH, AUDIO_FEATURE_LENGTH, CHANNELS),
    output_size=OUTPUT_SIZE
    )
feat = Spectrogram()
ms = ModelSpeech(sm251bn, feat, max_label_length=64)

ms.load_model('save_models/' + sm251bn.get_model_name() + '.model.h5')
res = ms.recognize_speech_from_file('00003~1.wav')
print('*[提示] 声学模型语音识别结果：\n', res)

ml = ModelLanguage('model_language')
ml.load_model()
str_pinyin = res
res = ml.pinyin_to_text(str_pinyin)
emotional(res)
print('语音识别最终结果：\n',res)

# '''
