import librosa
import os
import soundfile as sf

def slice_audio_folder(input_folder, output_folder, slice_duration=4):
    """
    将一个文件夹下的所有音频文件切片并保存到指定的输出文件夹中。

    参数：
        input_folder (str): 输入文件夹路径，包含所有要切片的音频文件。
        output_folder (str): 输出文件夹的路径，用于保存切片后的音频文件。
        slice_duration (int): 切片时长（秒）。

    返回：
        None
    """
    # 创建输出文件夹（如果不存在）
    os.makedirs(output_folder, exist_ok=True)

    # 获取输入文件夹中所有音频文件的路径
    audio_files = [f for f in os.listdir(input_folder) if f.endswith('.wav')]

    for audio_file in audio_files:
        # 输入音频文件的完整路径
        input_file_path = os.path.join(input_folder, audio_file)

        # 加载音频文件并指定dtype为float32
        y, sr = librosa.load(input_file_path, sr=None, dtype='float32')

        # 计算音频时长（秒）
        audio_duration = librosa.get_duration(y=y, sr=sr)

        # 计算需要切片的片段数
        num_slices = int(audio_duration // slice_duration)

        # 切片并保存每个片段
        for i in range(num_slices):
            start_time = i * slice_duration
            end_time = (i + 1) * slice_duration
            slice_data = y[int(start_time * sr):int(end_time * sr)]

            # 生成输出文件名
            output_file = os.path.join(output_folder, f"{audio_file.split('.')[0]}_slice_{i+1}.wav")

            # 保存切片到输出文件
            sf.write(output_file, slice_data, sr)

if __name__ == "__main__":
    input_audio_folder = "D:\\djangoproject\\zwork\\audio"
    output_folder = "D:\\djangoproject\\zwork\\newaudio"
    slice_duration = 4  # 切片时长（秒）

    slice_audio_folder(input_audio_folder, output_folder, slice_duration)

