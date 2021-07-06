# coding:utf-8
import json
import os
import sys
path = os.path.dirname(sys.path[0])
from business.common import CommonFun, BestApi
import requests

host = CommonFun.http_host()
Headers = CommonFun.http_header_token()

class Test_post():
    def create_post(self):
        # 创建岗位
        api = "/v1/post/"
        urls = host + api
        data = {
            "description": None,
            "name": "和谐星",
            "terminalType": 1
        }
        Data = json.dumps(data)
        # rps = requests.post(url=urls, headers=Headers, data=Data)
        rps = BestApi('post', urls, Headers, data=Data)
        rps = rps.interface()
        return rps
    def update_post(self, post_id):
        # 修改岗位
        api = "/v1/post/" + str(post_id)
        urls = host + api
        data = {
            "description": "更新岗位信息",
            "name": "和谐成号",
            "terminalType": 2
        }
        Data = json.dumps(data)
        rps = BestApi('put', urls, Headers, data=Data)
        rps = rps.interface()
        return rps
    def del_post(self, post_id):
        # 删除岗位
        api = "/v1/post/" + str(post_id)
        urls = host + api
        # rps = requests.delete(url=urls, headers=Headers)
        rps = BestApi('delete', urls, Headers)
        rps = rps.interface()
        return rps
    def search_post(self):
        # 查询所有岗位
        api = "/v1/post/all/"
        urls = host + api
        rp = BestApi('get', urls, Headers)
        rps = rp.interface()
        return rps
    def detail_post(self, post_id):
        # 岗位详情
        api = "/v1/post/" + str(post_id)
        urls = host + api
        rp = BestApi('get', urls, Headers)
        rps = rp.interface()
        return rps
    def get_postpage(self):
        # 分页查询岗位
        api = "/v1/post/page"
        urls = host + api
        data = {
            # "searchKey": "七月",
            "page": 1,
            "pageSize": 50
        }
        rp = BestApi('get', urls, Headers, params=data)
        rps = rp.interface()
        return rps
# if __name__ == '__main__':
#     TP = Test_post()
#     rp = TP.detail_post(21)
#     print(rp)
