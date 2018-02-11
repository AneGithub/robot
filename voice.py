# -*- coding: utf-8 -*-

"""
__autor__ : AnE

"""
import sys
import os

reload(sys)
sys.setdefaultencoding("utf-8")

class Voice:
    def __init__(self):
        self.RECORD_PATH = r"./record_voice.wav"

    # def savaVoice(self,data): #保存录音文件
    #     f = wave.open(self.RECORD_PATH,"wb")
    #     f.setframerate(self.RATE)
    #     f.setnchannels(self.CHANNELS)
    #     f.setsampwidth(pyaudio.PyAudio().get_sample_size(self.FORMAT))
    #     f.writeframes("".join(data))
    #     f.close()

    # def recordVoice(self): #录音
    #     pa = pyaudio.PyAudio()
    #
    #     stream = pa.open(format = self.FORMAT,
    #             channels = self.CHANNELS,
    #             rate = self.RATE,
    #             frames_per_buffer = self.CHUNK,
    #             input = True)
    #
    #     voicedata_list = []
    #     print u"正在录音..."
    #     for i in range(0,int(self.RATE/self.CHUNK*self.record_time)):
    #         voicedata = stream.read(self.CHUNK)
    #         voicedata_list.append(voicedata)
    #     print u"录音结束..."
    #
    #     stream.stop_stream()
    #     stream.close()
    #     pa.terminate()
    #     self.savaVoice(voicedata_list)
    def recordVoice(self):
        print "开始录音..."
        os.system('sudo arecord -D "plughw:1" -f S16_LE -r 16000 -d 4 %s'%self.RECORD_PATH)
        print "录音结束..."

    def playVoice(self,url): #播放声音
        print url
        os.system('mpg123 "%s"'%url)
