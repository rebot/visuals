import numpy as np
from pyaudio import PyAudio, paInt16

RATE = 44100 # time resolution of the recording device (Hz)
CHUNK = int(RATE/20) # RATE / number of updates per second)

p = PyAudio() # start the PyAudio class
stream = p.open(format=paInt16, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK) # uses default input device

# create a numpy array holding a single read of audio data
for i in range(int(10*44100/1024)): 
    data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
    peak = np.average(np.abs(data))*2
    bars = "#"*int(50*peak/2**16)
    print("%04d %05d %s" % (i, peak, bars))

stream.stop_stream()
stream.close()
p.terminate()
