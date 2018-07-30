# import librosa as rs
# import soundcard as nd

import pyaudio
import wave

import os.path

save_path = "C:\\Users\\Imam\\Documents\\PROGRAMMING PROJECTS\\LaunchX" #any directory

name_of_file = input("What is the name of the file: ")

WAVE_OUTPUT_FILENAME = os.path.join(save_path, name_of_file + ".wav")

# WAVE_OUTPUT_FILENAME = "output.wav"

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 30


p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()



wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

# -------------------------------------------------------------------

# import os.path

# save_path = "C:\\Users\\Imam\\Documents\\PROGRAMMING PROJECTS"

# name_of_file = input("What is the name of the file: ")

# completeName = os.path.join(save_path, name_of_file + ".txt")   

# file1 = open(completeName, "wb")

# # file1.write(str(final_list))

# # for line in final_list:
# #     file1.write(line)

# file1.close()

print("hello world")
