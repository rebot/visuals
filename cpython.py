from pyaudio import PyAudio, paFloat32

RATE = 48000
CHUNK = 1024

pa = PyAudio()

stream = pa.open(format = paFloat32,
                 channels = 1,
                 rate = RATE,
                 input = True,
                 frames_per_buffer = CHUNK,
                 stream_callback = callback)

while stream.is_active():
    sleep(0.1)

stream.close()
pa.terminate()





# Ref: http://bastibe.de/2012-11-02-real-time-signal-processing-in-python.html
