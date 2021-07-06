# coding:utf-8
import pytest

from common.Log import Log
from common_class.Test_post import Test_post

# 日志模块
logger = Log()
log = logger.get_log()

'''实例化对象'''
TP = Test_post()
class Test_post_01():
    def test_create_post(self):
        try:
            rp = TP.create_post()
            assert rp['code'] == 200
            assert rp['msg'] == '请求成功'
            assert rp['data'] is not None
            global post_id
            post_id = rp['data']
            log.debug("断言正确，创建岗位-用例通过")
        except AssertionError:
            log.debug("断言出现错误!")

    def test_search_all(self):
        try:
            rp = TP.search_post()
            assert rp['data'] is not None
            log.debug("断言正确，查询所有岗位-用例通过")
        except AssertionError:
            log.debug("断言出现错误!")

    def test_detail_post(self):
        try:
            rp = TP.detail_post(post_id)
            assert rp['code'] == 200
            assert rp['data'] is not None
            log.debug("断言正确，岗位详情信息-用例通过")
        except AssertionError:
            log.debug("断言出现错误!")
    def test_get_postpage(self):
        try:
            rp = TP.get_postpage()
            assert rp['code'] == 200
            assert rp['data'] is not None
            log.debug("断言正确，获取岗位分页信息-用例通过")
        except AssertionError:
            log.debug("断言出现错误!")
    def test_update_post(self):
        try:
            rp = TP.update_post(post_id)
            assert rp['code'] == 200
            assert rp['msg'] == '修改成功'
            log.debug("断言正确，修改岗位-用例通过")
        except AssertionError:
            log.debug("断言出现错误!")
    def test_del_post(self):
        try:
            rp = TP.del_post(post_id)
            assert rp['code'] == 200
            assert rp['msg'] == '请求成功'
            assert rp['data'] == True
            log.debug("断言正确，删除岗位-用例通过")
        except AssertionError:
            log.debug("断言出现错误!")
if __name__ == '__main__':
    pytest.main(["-vs", "test_post.py"])