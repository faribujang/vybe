import pyaudio
import time
import numpy as np
from matplotlib import pyplot as plt
import scipy.signal as signal

print('import ok')

CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()
fulldata = np.array([])
dry_data = np.array([])
left = np.array([])
right = np.array([])

def main():
    stream = p.open(format=pyaudio.paFloat32,
        channels=CHANNELS,
        rate=RATE,
        output=True,
        input=True,
        stream_callback=callback)
    stream.start_stream()
    while stream.is_active():
        time.sleep(2)
        stream.stop_stream()
        #pass
    stream.close()

    numpydata = np.hstack(fulldata)
    plt.plot(numpydata)
    plt.title("Wet")
    plt.show()


    numpydata = np.hstack(dry_data)
    plt.plot(numpydata)
    plt.title("Dry")
    plt.show()
    p.terminate()

    numpydata = np.hstack(left)
    plt.plot(numpydata)
    plt.title("Left")
    plt.show()
    p.terminate()

    numpydata = np.hstack(right)
    plt.plot(numpydata)
    plt.title("Right")
    plt.show()
    p.terminate()

def callback(in_data, frame_count, time_info, flag):
    global b,a,fulldata,dry_data,frames,left,right
    audio_data = np.fromstring(in_data, dtype=np.float32)
    dry_data = np.append(dry_data,audio_data)
    #do processing here
    fulldata = np.append(fulldata,audio_data)
    result = np.fromstring(audio_data, dtype=np.float32)
    result = np.reshape(audio_data, (1024, 2))
    left = np.append(left,result[:, 0])
    right = np.append(right,result[:, 1])
    return (audio_data, pyaudio.paContinue)

main()
