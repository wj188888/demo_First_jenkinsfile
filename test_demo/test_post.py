# coding:utf-8
import pytest

from common_class.Test_post import Test_post
'''实例化对象'''
TP = Test_post()
class Test_post_01():
    def test_create_post(self):
        rp = TP.create_post()
        assert rp['code'] == 200
        assert rp['msg'] == '请求成功'
        assert rp['data'] is not None
        global post_id
        post_id = rp['data']

    def test_search_all(self):
        rp = TP.search_post()
        assert rp['data'] is not None

    def test_detail_post(self):
        rp = TP.detail_post(post_id)
        assert rp['code'] == 200
        assert rp['data'] is not None

    def test_get_postpage(self):
        rp = TP.get_postpage()
        assert rp['code'] == 200
        assert rp['data'] is not None

    def test_update_post(self):
        rp = TP.update_post(post_id)
        assert rp['code'] == 200
        assert rp['msg'] == '修改成功'

    def test_del_post(self):
        rp = TP.del_post(post_id)
        assert rp['code'] == 200
        assert rp['msg'] == '请求成功'
        assert rp['data'] == True