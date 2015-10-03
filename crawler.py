#-*- encoding:utf-8 -*-,
import requests
import json
import urllib
import sys
HEADERS = {
"Host":"www.freetranslation.com",
"Connection":" keep-alive",
"Content-Length":" 41",
"Origin":" http://www.freetranslation.com",
"Tracking":" applicationKey=dlWbNAC2iLJWujbcIHiNMQ%3D%3D applicationInstance=freetranslation",
"User-Agent":" Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
"Content-Type":" application/json",
"Accept":" application/json, text/javascript, */*; q=0.01",
"X-Requested-With":" XMLHttpRequest",
"Referer":" http://www.freetranslation.com/zh-tw/",
"Accept-Encoding":" gzip, deflate",
"Accept-Language":" en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
}

LANG={
#u"英文":"eng",
#u"中文 (繁體)":"cht",
u"中文 (簡體)":"chi",
u"丹麥文":"dan",
u"俄文":"rus",
u"保加利亞文":"bul",
u"匈牙利文":"hun",
u"印尼文":"ind",
u"印度文":"hin",
u"土耳其文":"tur",
u"塞爾維亞文":"srp",
u"孟加拉文":"ben",
u"希伯來文":"heb",
u"希臘文":"gre",
u"德文":"ger",
u"愛沙尼亞文":"est",
u"挪威文":"nor",
u"捷克文":"cze",
u"斯洛伐克文":"slo",
u"斯洛維尼亞文":"slv",
u"日文":"jpn",
u"普什圖文":"pus",
u"法文":"fra",
u"波斯文":"per",
u"波蘭文":"pol",
u"泰文":"tha",
u"烏克蘭文":"ukr",
u"烏都文":"urd",
u"瑞典文":"swe",
u"立陶宛文":"lit",
u"索馬利文":"som",
u"羅馬尼亞文":"rum",
u"義大利文":"ita",
u"芬蘭文":"fin",
u"荷蘭文":"dut",
u"葡萄牙文":"por",
u"西班牙文":"spa",
u"豪沙文":"hau",
u"越南文":"vie",
u"達里文":"fad",
u"阿拉伯文":"ara",
u"韓文":"kor",
u"馬來文":"may",
}

def translate_word(word, fr, to):
  #data_cht = json.dumps(json_obj_cht) 
  data_in = '{"text":"%s","from":"%s","to":"%s"}'%(urllib.quote(word,safe=''),fr,to) 
  r = requests.post("http://www.freetranslation.com/gw-mt-proxy-service-web/mt-translation", data=data_in, headers=HEADERS )
  #print r.text
  out_obj = json.loads( r.text)
  #print out_obj
  out_word = out_obj["translation"]
  return out_word

def gen_words(word_in):
  result = {}
  word_eng =  translate_word(word_in,"cht","eng")
  result.update({u"英文": word_eng})
  print "%s: %s"%(u"英文",word_eng)
  for w in LANG:
    word_lang =  translate_word(word_eng,"eng",LANG[w])
    result.update({w:word_lang})
    print "%s: %s"%(w,word_lang)
  return result

def main():
  result = gen_words(sys.argv[1])
  #for w in result:
  #  print "%s: %s"%(w,result[w])

def test():
  word_in = u"投票".encode('utf-8')
  result = gen_words(word_in)
  #for w in result:
  #  print "%s: %s"%(w,result[w])

if __name__ == "__main__":
  #main()
  test()
