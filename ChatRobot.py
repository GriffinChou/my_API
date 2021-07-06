# -*- coding:utf-8 -*-
'''
调用百度的对话接口，生成一个在线聊天AI机器人
'''

import json
import random
import requests
client_id = "Pd6Q4F6xKnjMi7jwqPx55TTy"
client_secret = "Ep5WykCokSdzzHKZBqrwrTfHjVyYcOhz"

def unit_chat(chat_input,user_id="8888"):
    '''
    功能：进行聊天
    :param chat_input:用户输入的聊天语句
    :param user_id:该用户的id
    :return:返回百度unit机器人的回复语句
    '''
    #默认回复
    chat_reply = "不好意思，我正在学习中"
    #得到访问的access_token
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s"% (client_id,client_secret)
    # print(url)

    res = requests.get(url)
    # print(res.text)
    access_token = eval(res.text)["access_token"]

    #利用刚得到的access_token访问聊天url
    unit_chatbot_url = "https://aip.baidubce.com/rpc/2.0/unit/service/chat?access_token=" + access_token

    #构建访问数据
    post_data = {
        "log_id": str(random.random()),
        "request": {"query": chat_input,
                   "user_id": user_id
                   },
        "session_id": "",
        "service_id": "s52044",
        "version": "2.0"
    }

    #访问第二个url，得到百度机器人的回复
    res = requests.post(url=unit_chatbot_url,json=post_data)

    #得到res中有一个content，里面放着真正的返回信息
    unit_chat_obj = json.loads(res.content)
    # print("返回信息",unit_chat_obj)

    #判断聊天接口的返回是否正常，依据error_code判断，不为0时访问错误
    if unit_chat_obj["error_code"] != 0:
        return chat_reply

    #解析数据
    unit_chat_obj_result = unit_chat_obj["result"]
    unit_chat_response_list = unit_chat_obj_result["response_list"]

    #随机选择一个意图置信度大于0的回复作为机器人的回复语句
    unit_chat_response_obj = random.choice([unit_chat_response for unit_chat_response in unit_chat_response_list
                                            if unit_chat_response["schema"]["intent_confidence"]>0.0])

    #进一步提取数据
    unit_chat_response_action_list = unit_chat_response_obj["action_list"]
    # print("aaaaaaa",unit_chat_response_action_list)
    unit_chat_response_obj = random.choice(unit_chat_response_action_list)
    unit_chat_response_say = unit_chat_response_obj['say']
    return unit_chat_response_say

if __name__ == '__main__':
    print("您好，我是小周，现在我来陪你聊天解闷！")
    while True:
        chat_input = input()
        chat_reply = unit_chat(chat_input)
        print("你：",chat_input)
        print("小周:", chat_reply)
        if chat_input == 'q' or chat_input == 'Q':
            break

