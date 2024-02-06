import os
from random import shuffle
from zwork.train import getFeature
from zwork.drawRadar import draw
import joblib
import numpy as np
import pyaudio
import wave
import pymysql
import time

path = r'D:\djangoproject\zwork\newaudio'

wav_paths = []
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".wav"):
            wav_path = os.path.join(root, file)
            wav_paths.append(wav_path)
'''person_dirs = os.listdir(path)
for person in person_dirs:
    if person.endswith('txt'):
     continue
    emotion_dir_path = os.path.join(path, person)
    emotion_dirs = os.listdir(emotion_dir_path)
    for emotion_dir in emotion_dirs:
        if emotion_dir.endswith('.ini'):
            continue
        emotion_file_path = os.path.join(emotion_dir_path, emotion_dir)
        emotion_files = os.listdir(emotion_file_path)
        for file in emotion_files:
            if not file.endswith('wav'):
                continue
            wav_path = os.path.join(emotion_file_path, file)
            wav_paths.append(wav_path)'''

# 将语音文件随机排列
# shuffle(wav_paths)

model = joblib.load('D:\\djangoproject\\zwork\\Models\\C_13_mfccNum_48.m')

p = pyaudio.PyAudio()
for wav_path in wav_paths:
    f = wave.open(wav_path, 'rb')
    stream = p.open(
        format=p.get_format_from_width(f.getsampwidth()),
        channels=f.getnchannels(),
        rate=f.getframerate(),
        output=True)
    data = f.readframes(f.getparams()[3])
    stream.write(data)
    stream.stop_stream()
    stream.close()
    f.close()
    data_feature = getFeature(wav_path, 48)
    # print(model.predict([data_feature]))
    # 数据库操作
    # conn = pymysql.connect(port=3306, user='root', password='', charset='utf8', db='gx_day16')
    # cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    #
    # imgPath = os.path.basename(wav_path)
    # print(imgPath)

    arr = model.predict_proba([data_feature])[0]
    max_val = max(arr)
    print(max_val)
    print('ceshi')
    # mark表 生气：0 焦虑：1 疲惫：2 中性：3 惊讶：4 快乐：5
    Anger = arr[0]
    Anxious = arr[1]
    Happy = arr[2]
    Neutral = arr[3]
    Tired = arr[4]
    Surprise = arr[5]

    # # 记录检测时间
    # texttime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    # print(texttime)
    #
    # if Anger == max_val:
    #     sql2 = "insert into app01_audio_list(img_name,angry,anxious,happy," \
    #            "neutral,tired,surprise,detection_date,mark) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    #     cursor.execute(sql2, [imgPath,
    #                           model.predict_proba([data_feature])[0][0],
    #                           model.predict_proba([data_feature])[0][1],
    #                           model.predict_proba([data_feature])[0][2],
    #                           model.predict_proba([data_feature])[0][3],
    #                           model.predict_proba([data_feature])[0][4],
    #                           model.predict_proba([data_feature])[0][5],
    #                           texttime, 1])
    #     conn.commit()
    # if Anxious == max_val:
    #     sql2 = "insert into app01_audio_list(img_name,angry,anxious,happy," \
    #            "neutral,tired,surprise,detection_date,mark) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    #     cursor.execute(sql2, [imgPath,
    #                           model.predict_proba([data_feature])[0][0],
    #                           model.predict_proba([data_feature])[0][1],
    #                           model.predict_proba([data_feature])[0][2],
    #                           model.predict_proba([data_feature])[0][3],
    #                           model.predict_proba([data_feature])[0][4],
    #                           model.predict_proba([data_feature])[0][5],
    #                           texttime, 2])
    #     conn.commit()
    # if Happy == max_val:
    #     sql2 = "insert into app01_audio_list(img_name,angry,anxious,happy," \
    #            "neutral,tired,surprise,detection_date,mark) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    #     cursor.execute(sql2, [imgPath,
    #                           model.predict_proba([data_feature])[0][0],
    #                           model.predict_proba([data_feature])[0][1],
    #                           model.predict_proba([data_feature])[0][2],
    #                           model.predict_proba([data_feature])[0][3],
    #                           model.predict_proba([data_feature])[0][4],
    #                           model.predict_proba([data_feature])[0][5],
    #                           texttime, 3])
    #     conn.commit()
    # if Neutral == max_val:
    #     sql2 = "insert into app01_audio_list(img_name,angry,anxious,happy," \
    #            "neutral,tired,surprise,detection_date,mark) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    #     cursor.execute(sql2, [imgPath,
    #                           model.predict_proba([data_feature])[0][0],
    #                           model.predict_proba([data_feature])[0][1],
    #                           model.predict_proba([data_feature])[0][2],
    #                           model.predict_proba([data_feature])[0][3],
    #                           model.predict_proba([data_feature])[0][4],
    #                           model.predict_proba([data_feature])[0][5],
    #                           texttime, 4])
    #     conn.commit()
    # if Tired == max_val:
    #     sql2 = "insert into app01_audio_list(img_name,angry,anxious,happy," \
    #            "neutral,tired,surprise,detection_date,mark) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    #     cursor.execute(sql2, [imgPath,
    #                           model.predict_proba([data_feature])[0][0],
    #                           model.predict_proba([data_feature])[0][1],
    #                           model.predict_proba([data_feature])[0][2],
    #                           model.predict_proba([data_feature])[0][3],
    #                           model.predict_proba([data_feature])[0][4],
    #                           model.predict_proba([data_feature])[0][5],
    #                           texttime, 5])
    #     conn.commit()
    # if Surprise == max_val:
    #     sql2 = "insert into app01_audio_list(img_name,angry,anxious,happy," \
    #            "neutral,tired,surprise,detection_date,mark) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    #     cursor.execute(sql2, [imgPath,
    #                           model.predict_proba([data_feature])[0][0],
    #                           model.predict_proba([data_feature])[0][1],
    #                           model.predict_proba([data_feature])[0][2],
    #                           model.predict_proba([data_feature])[0][3],
    #                           model.predict_proba([data_feature])[0][4],
    #                           model.predict_proba([data_feature])[0][5],
    #                           texttime, 6])
    #     conn.commit()
    #
    # # 关闭
    # cursor.close()
    # conn.close()
    print(model.predict_proba([data_feature])[0])
    # print(max_val)
    # print(model.predict_proba([data_feature]))

    labels = np.array(['angry', 'anxious', 'happy', 'neutral', 'tired', 'surprise'])

    # draw(model.predict_proba([data_feature])[0], labels, 6)

p.terminate()
