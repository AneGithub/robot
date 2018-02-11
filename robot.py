# -*- coding: utf-8 -*-

"""
__autor__ : AnE

"""
from voice import Voice
import voiceAPI

def main():
    voice = Voice()
    baiduAPI = voiceAPI.BaiDuAPI()
    turlingAPI = voiceAPI.TurLingAPI()
    baiduAPI.getToken()

    while True:
        voice.recordVoice()
        recognition_result = baiduAPI.voiceRecognition()
        if recognition_result:
            if "退出对话" in recognition_result:
                break

            reply_result = turlingAPI.turlingReply(recognition_result)
            if reply_result:
                baiduAPI.voiceSynthesis(reply_result)
                voice.playVoice()
            else:
                baiduAPI.voiceSynthesis("对不起,获取回复失败")
                voice.playVoice()
                continue
        else:
            baiduAPI.voiceSynthesis("对不起,识别失败")
            voice.playVoice()
            continue

    baiduAPI.voiceSynthesis("退出成功")
    voice.playVoice()


if __name__ == '__main__':
    main()



