import librosa

# Load an audio file -> returns (waveform, sample_rate)
y, sr = librosa.load("song.wav", sr=44100, mono=True)

print(type(y))      # <class 'numpy.ndarray'>
print(y.shape)       # (num_samples,) -- 1D array since mono=True
print(y.dtype)        # float32
print(sr)            # 44100