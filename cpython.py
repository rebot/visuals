import time
from pyaudio import PyAudio, paFloat32

RATE = 48000
CHUNK = 1024

pa = PyAudio()

stream = pa.open(format = paFloat32,
                 channels = 1,
                 rate = RATE,
                 output = True,
                 frames_per_buffer = CHUNK)

while stream.is_active():
    time.sleep(0.1)

stream.close()
pa.terminate()





# Ref: http://bastibe.de/2012-11-02-real-time-signal-processing-in-python.html
