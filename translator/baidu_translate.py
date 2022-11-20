#百度通用翻译API，具体帮助文档参考网站：http://api.fanyi.baidu.com/doc/21
# coding=utf-8
 
import http.client
import hashlib
import urllib
import random
import json

def baiduTranslate(q): 
    # 百度appid和密钥需要通过注册百度【翻译开放平台】账号后获得
    appid = '20221120001461841'        # appid
    secretKey = 'IDXzb31d80qcQJ2ZWuXS'    # 密钥
    
    httpClient = None
    myurl = '/api/trans/vip/translate'  # 通用翻译API HTTP地址
    
    fromLang = 'auto'       # 原文语种
    toLang = 'zh'           # 译文语种

    salt = random.randint(32768, 65536)
    # 手动录入翻译内容，q存放
    # q = raw_input("please input the word you want to translate:")  
    sign = appid + q + str(salt) + secretKey   # 字符串1
    sign = hashlib.md5(sign.encode()).hexdigest()  # 对字符串1做 MD5 ，得到 32 位小写的 sign
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + \
            '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
    
    # 建立会话，返回结果 返回的结果是json格式
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('POST', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
        dst_str = result['trans_result'][0]['dst']
    
        # print (dst_str)
    
    except Exception as e:
        print (e)
    finally:
        if httpClient:
            httpClient.close()
    # dst_str = 'www'
    return dst_str

if __name__ == '__main__':
    print(baiduTranslate('i love you.'))