import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

fs = 44100
duration = 5 #seconds
sd._terminate()
sd._initialize()
print(sd.query_devices())
my_recording = sd.rec(duration * fs, samplerate=fs, channels=2, dtype='float64')

sd.wait()

sd.play(my_recording, fs)

sd.wait()

