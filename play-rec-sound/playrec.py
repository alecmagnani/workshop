import sounddevice as sd

fs = 48000 # frames per sec
duration = 10 # seconds

sd.default.samplerate = fs
sd.default.channels = 2

myrec = sd.rec(duration * fs, samplerate=fs, channels=2)
sd.wait()
print(myrec)
