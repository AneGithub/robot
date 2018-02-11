# -*- coding: utf-8 -*-

"""
__autor__ : AnE

"""
import sys
import requests
import json
import urllib2
import base64
import urllib

reload(sys)
sys.setdefaultencoding("utf-8")

class BaiDuAPI:
    def __init__(self):
        self.GRANT_TYPE = "client_credentials"
        self.CLIENT_ID = "b6lN1eECXn1aRoK9PiwiqwWT" #百度应用的 API Key
        self.CLIENT_SECRET = "t8KSgal9vgoy5z0AagKOATmPsUrfEiyx" #百度应用的 API Secret
        self.TOKEN_URL = "https://openapi.baidu.com/oauth/2.0/token"
        self.RECOGNITION_URL = "http://vop.baidu.com/server_api"
        self.CUID = "B8-27-EB-BA-24-14"
        self.RECOGNITION_PATH = r"./record_voice.wav"
        self.SYNTHESIS_PATH = r"./play_voice.mp3"

    def getToken(self): #获取access_token
        body = {
            "grant_type":self.GRANT_TYPE,
            "client_id":self.CLIENT_ID,
            "client_secret":self.CLIENT_SECRET
        }
        r = requests.post(self.TOKEN_URL,data=body,verify=True)
        self.access_token = json.loads(r.text)["access_token"]
        return self.access_token

    def voiceRecognition(self): #语音识别
        erro_dict = {
            3300:"输入参数不正确",
            3301:"音频质量过差",
            3302:"鉴权失败",
            3303:"语音服务器后端问题",
            3304:"用户的请求QPS超限",
            3305:"用户的日pv（日请求量）超限",
            3307:"语音服务器后端识别出错问题",
            3308:"音频过长",
            3309:"音频数据问题",
            3310:"输入的音频文件过大",
            3311:"采样率rate参数不在选项里",
            3312:"音频格式format参数不在选项里"
        }
        f = open(self.RECOGNITION_PATH,"rb")
        voice_data = f.read()
        f.close()

        speech_data = base64.b64encode(voice_data).decode("utf-8")
        speech_length = len(voice_data)
        post_data = {
            "format": "wav",
            "rate": 16000,
            "channel": 1,
            "cuid": self.CUID,
            "token": self.access_token,
            "speech": speech_data,
            "len": speech_length
        }

        json_data = json.dumps(post_data).encode("utf-8")
        json_length = len(json_data)

        req = urllib2.Request(self.RECOGNITION_URL, data=json_data)
        req.add_header("Content-Type", "application/json")
        req.add_header("Content-Length", json_length)

        resp = urllib2.urlopen(req)
        resp = resp.read()
        resp_data = json.loads(resp.decode("utf-8"))
        try:
            recognition_result = resp_data["result"][0]
            print recognition_result
            return recognition_result
        except:
            print erro_dict[resp_data["err_no"]]
            return False

    def voiceSynthesis(self,word): #语音合成
        token = self.access_token
        cuid = self.CUID
        word = urllib.quote(word.encode("utf8"))
        url = "http://tsn.baidu.com/text2audio?tex="+word+"&lan=zh&cuid="+cuid+"&ctp=1&tok="+token+"&per=4"
        urllib.urlretrieve(url,self.SYNTHESIS_PATH)

class TurLingAPI:
    def __init__(self):
        self.Tuling_API_KEY = "1872aeffd794498696772ce53c5c26ac"
        self.URL = "http://www.tuling123.com/openapi/api"

    def turlingReply(self,word): #图灵获取回复
        body = {"key": self.Tuling_API_KEY,
                "info": word.encode("utf-8")}
        res = requests.post(self.URL, data=body, verify=True)

        if res:
            date = json.loads(res.text)
            print date["text"]
            return date["text"]
        else:
            print "对不起,未获取到回复信息"
            return False