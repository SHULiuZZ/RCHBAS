# import subprocess
#
# import pytest
# from moviepy.editor import *
# import os
# import filetype
# import warnings
# from sklearn import svm
#
#
# warnings.filterwarnings("ignore")
#
#
# # 修改文件后缀例如： C:/dir/a/b.png 需要转为 C:/dir/a/b.jpg  调用函数：trAffter('C:/dir/a/b.png', 'jpg')
# def trAffter(path, Type):
#     a = path.split('/')
#     b = a[-1].split('.')
#     b[-1] = Type
#     a[-1] = '.'.join(b)
#     return '/'.join(a)
#
#
# def extractMp3(video_path, root):
#     voiceType = "wav"
#     print("提取文件：", video_path)
#     src_path = os.path.dirname(video_path)
#     audio = VideoFileClip(video_path).audio
#     # 音频保存的路径
#     voice_path = trAffter(video_path.replace(src_path, root), voiceType)
#     print("\t音频保存至：", voice_path)
#     audio.write_audiofile(voice_path, codec='libmp3lame')
#
#
# def testVioce(video_path, dst_rootVoice):
#     video_path = "D:/djangoproject/media/20230214-143601.mp4"
#     dst_rootVoice = "D:\\djangoproject\\zwork\\audio\\"
#     extractMp3(video_path, dst_rootVoice)
#
#     # 运行第二个脚本
#     subprocess.run(['python', 'slicer.py'])
#     # 运行第三个脚本
#     subprocess.run(['python', 'testEmotion.py'])
#     #testEmotion
#     # 清除之前处理的文件
#     folders_to_clear = [dst_rootVoice, 'D:\\djangoproject\\zwork\\newaudio','D:\\djangoproject\\zwork\\newvideo']
#     for folder_path in folders_to_clear:
#         print(f"Clearing folder: {folder_path}")
#         for file_name in os.listdir(folder_path):
#             file_path = os.path.join(folder_path, file_name)
#             if os.path.isfile(file_path):
#                 os.unlink(file_path)
#             elif os.path.isdir(file_path):
#                 shutil.rmtree(file_path)
#
#
#  @pytest.fixture
#  def video_path():
#      return 'D:\\20230214-143601.mp4'
#
#  @pytest.fixture
#  def dst_rootVoice():
#      return 'D:\\djangoproject\\zwork\\audio\\'
#
#
# if __name__ == '__main__':
#     video_path = "D:\\djangoproject\\media\\20230214-143601.mp4"
#     dst_rootVoice = "D:\\djangoproject\\zwork\\audio\\"
#     voiceType = "wav"
#     testVioce(video_path, dst_rootVoice)

import subprocess
from moviepy.editor import *
import os
import filetype
import warnings
from sklearn import svm


warnings.filterwarnings("ignore")


# 修改文件后缀例如： C:/dir/a/b.png 需要转为 C:/dir/a/b.jpg  调用函数：trAffter('C:/dir/a/b.png', 'jpg')
def trAffter(path, Type):
    a = path.split('/')
    b = a[-1].split('.')
    b[-1] = Type
    a[-1] = '.'.join(b)
    return '/'.join(a)


def extractMp3(video_path, root):
     voiceType = "wav"
     print("提取文件：", video_path)
     src_path = os.path.dirname(video_path)
     audio = VideoFileClip(video_path).audio
     # 音频保存的路径
     voice_path = trAffter(video_path.replace(src_path, root), voiceType)
     print("\t音频保存至：", voice_path)
     #audio.write_audiofile(voice_path, codec='libmp3lame')
     audio.write_audiofile(voice_path, codec='libmp3lame',logger = None)


def mytestVioce(video_path, dst_rootVoice):

    extractMp3(video_path, dst_rootVoice)

    # 运行第二个脚本
    subprocess.run(['python', 'slicer.py'])
    # 运行第三个脚本
    subprocess.run(['python', 'testEmotion.py'])
    #testEmotion
    # 清除之前处理的文件
    folders_to_clear = [dst_rootVoice, 'D:\\djangoproject\\zwork\\newaudio','D:\\djangoproject\\zwork\\newvideo']
    for folder_path in folders_to_clear:
        print(f"Clearing folder: {folder_path}")
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)


if __name__ == '__main__':
    video_path = 'D:\\djangoproject\\media\\20230214-143601.mp4'
    dst_rootVoice = "D:\\djangoproject\\zwork\\audio\\"
    voiceType = "wav"
    mytestVioce(video_path, dst_rootVoice)

