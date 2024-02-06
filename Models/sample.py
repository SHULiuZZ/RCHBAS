from scipy.io import wavfile

sample_rate, sig = wavfile.read('00003~1.wav')
print(sample_rate)
print(sig)
print(sig.dtype)