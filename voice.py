# -*- coding: utf-8 -*-

"""
__autor__ : AnE

"""
import sys
import wave
import pyaudio
import mp3play
import time

reload(sys)
sys.setdefaultencoding("utf-8")

class Voice:
    def __init__(self):
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16 #16声道
        self.CHANNELS = 1 #声道
        self.RATE = 16000  #采样率
        self.record_time = 5 #录音时间
        self.RECORD_PATH = r"./record_voice.wav"
        self.PLAY_PATH = r"./play_voice.mp3"

    def savaVoice(self,data): #保存录音文件
        f = wave.open(self.RECORD_PATH,"wb")
        f.setframerate(self.RATE)
        f.setnchannels(self.CHANNELS)
        f.setsampwidth(pyaudio.PyAudio().get_sample_size(self.FORMAT))
        f.writeframes("".join(data))
        f.close()

    def recordVoice(self): #录音
        pa = pyaudio.PyAudio()

        stream = pa.open(format = self.FORMAT,
                channels = self.CHANNELS,
                rate = self.RATE,
                frames_per_buffer = self.CHUNK,
                input = True)

        voicedata_list = []
        print u"正在录音..."
        for i in range(0,int(self.RATE/self.CHUNK*self.record_time)):
            voicedata = stream.read(self.CHUNK)
            voicedata_list.append(voicedata)
        print u"录音结束..."

        stream.stop_stream()
        stream.close()
        pa.terminate()
        self.savaVoice(voicedata_list)

    def playVoice(self): #播放声音
        m = mp3play.load(self.PLAY_PATH)
        m.play()
        time.sleep(m.seconds())
        m.stop()
