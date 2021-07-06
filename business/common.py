# coding:utf-8

import requests
import json

class CommonFun():
    @classmethod
    def http_host(self):
        # my_host = "http://zah.dev.dhwork.cn"  # 开发环境的host
        my_host = "http://zah.test.dhwork.cn"   # 测试环境的host
        # my_host = "http://192.168.10.109:8002"  #

        return my_host

    @classmethod
    def get_token(self):
        api = "/v1/auth/login"
        urls = CommonFun.http_host() + api
        data = {
            "username": "18382223307",  # 开发环境和测试环境都可以用，amd yes
            "password": "12345678"  # 开发环境和测试环境都可以用，amd yes
        }
        QHeaders = CommonFun.http_header()
        data = json.dumps(data)
        rp = requests.post(url=urls, headers=QHeaders, data=data)
        ztoken = rp.json()['data']['accessToken']
        my_token = "Bearer " + ztoken
        # print("第一次拿到的token", my_token)
        pre_pid = rp.json()['data']['preProject']['id']
        return my_token, pre_pid

    @classmethod
    def http_header_token(self):
        data = CommonFun.get_token()
        token_id = data[0]
        projenct_id = str(data[1])
        head_data = {
            "Content-Type": "application/json",
            "Authorization": token_id,
            "PROJECT-HEADER": projenct_id
        }
        # print("头部token：", head_data['Authorization'])
        # print(head_data['PROJECT-HEADER'])
        return head_data

    @classmethod
    def http_header(self):
        head_data = {
            "Content-Type": "application/json",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
        }
        return head_data

    @classmethod
    def get_reflash(self, user, pwd):
        api = "/v1/auth/login"
        urls = CommonFun.http_host() + api
        data = {
            "username": user,
            "password": pwd
        }
        Headers = CommonFun.http_header()
        data = json.dumps(data)
        rp = requests.post(url=urls, headers=Headers, data=data)
        my_reflash = rp.json()['data']['refreshToken']
        my_reflash = "Bearer " + my_reflash
        return my_reflash

    @classmethod
    def search_pro(self):
        api = "/v1/project/search"
        urls = CommonFun.http_host() + api
        data = {
            "ownerName": "双江口业主",
            "page": 1,
            "pageSize": 100,
            "projectName": "双江口水电站大坝"
        }
        Headers = CommonFun.http_header_token()
        # rp = requests.get(url=urls, headers=Headers, params=data)
        rps = BestApi('get', urls, Headers, params=data)
        rps = rps.interface()
        # rps = rp.json()['data']
        # pro_id = rps['data'][0]['id'] # 0是最早生成的结果，-1是最新生成的结果
        return rps

class BestApi():
    def __init__(self, method, url, headers, data=None, params=None, json=None, file=None):
        self.method = method
        self.url = url
        self.headers = headers
        self.data = data
        self.params = params
        self.json = json
        self.file = file
    def interface(self):
        rp = requests.request(method=self.method, url=self.url, headers=self.headers, data=self.data, params=self.params, json=self.json, files=self.file)
        return rp.json()

if __name__ == '__main__':
    # rp = CommonFun.http_login("18382223307", "12345678")
    rp = CommonFun.search_pro()
    # rp = CommonFun.get_token()
    print(type(rp))
    print(rp)