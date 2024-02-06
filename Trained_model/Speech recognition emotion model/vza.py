from moviepy.editor import *
import os
import filetype
import argparse

# 修改这里啊
root = "E:\\app\\pycharm\\PyCharm2020.1\\pytest\\djangoproject\\zwork\\newvideo\\"
rootVoice = "E:\\app\\pycharm\\PyCharm2020.1\\pytest\\djangoproject\\zwork\\audio\\"
voiceType = "wav"
videoType = "video/mp4"


# 获取文件名称
def getName(video_name):
    return os.path.basename(video_name).split('.')[0]


# 修改文件后缀例如： C:/dir/a/b.png 需要转为 C:/dir/a/b.jpg  调用函数：trAffter('C:/dir/a/b.png', 'jpg')
def trAffter(path, type):
    a = path.split('/')
    b = a[-1].split('.')
    b[-1] = voiceType
    a[-1] = '.'.join(b)
    return '/'.join(a)


# 提取音频
def extractMp3(video_path):
    print("提取文件：", video_path)
    audio = VideoFileClip(video_path).audio
    # 音频保存的路径
    voice_path = video_path.replace(root, rootVoice)
    print("\t音频保存至：", trAffter(voice_path, voiceType))
    audio.write_audiofile(trAffter(voice_path, voiceType))


# 遍历目录下的所有文件
def getVideoList(path):
    # 是否为文件
    if not os.path.isdir(path):
        ft = filetype.guess(path)
        if ft is not None and ft.mime == videoType:
            extractMp3(path)
        else:
            print(f"跳过文件{path}")
        return
    # 递归遍历
    for dir in os.listdir(path):
        # 音频保存的路径目录不存在新建
        voice_path = path.replace(root, rootVoice)
        if not os.path.exists(voice_path):
            os.makedirs(voice_path)
        getVideoList(os.path.join(path, dir))


# 开始
getVideoList(root)
