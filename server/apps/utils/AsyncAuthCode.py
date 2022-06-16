import json
from urllib.parse import urlencode

import requests
from tornado import httpclient
from tornado.httpclient import HTTPRequest, AsyncHTTPClient


class AsyncAuthCode:
    def __init__(self, apikey):
        self.apikey = apikey

    # 发送验证码（异步）
    async def send_single_sms(self, code, mobile):
        http_client = AsyncHTTPClient()
        # 海外服务器地址 us.yunpian.com
        url = "https://sms.yunpian.com/v2/sms/single_send.json"
        text = "【聂佳叶】您的验证码是{}，将用于注册信息，无需回复。".format(code)
        post_req = HTTPRequest(url=url, headers={
            "Accept": "application/json;charset=utf-8;",
            "Content-Type": "application/x-www-form-urlencoded;charset=utf-8;"
        }, method="POST", body=urlencode({
            "apikey": self.apikey,
            "mobile": mobile,
            "text": text,
        }))
        try:
            res = await http_client.fetch(post_req)
        except Exception as e:
            return json.loads(e.response.body.decode("utf8"));
        return json.loads(res.body.decode("utf8"))


if __name__ == "__main__":
    # import tornado
    # ioloop = tornado.ioloop.IOLoop.current()
    #
    # authcode = AsyncAuthCode("9c3496165c2af281c74233c8a27fe15e")
    #
    # # 组成带参数的新方法
    # from functools import partial
    # new_func = partial(authcode.send_single_sms, "1234", "18789601202")
    # ioloop.run_sync(new_func)

    apikey = "9c3496165c2af281c74233c8a27fe15e"
    url = "https://sms.yunpian.com/v2/sms/single_send.json"
    text = "【聂佳叶】您的验证码是{}，将用于注册信息，无需回复。".format(1234)
    res = requests.post(url=url, data={
        "apikey": apikey,
        "mobile": "18789601202",
        "text": text,
    }, headers={
        "Accept": "application/json;charset=utf-8;",
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8;"
    })
    print(json.loads(res.content))
