# coding:utf-8

import logging
import time
import os.path

class Log():
    def __init__(self):
        self.level="DEBUG"
        # 日志器对象
        self.logger = logging.getLogger("大汇")
        self.logger.setLevel(self.level)

    def console_handle(self, level="DUBUG"):
        # 控制器处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(self.level)

        # 处理器添加格式器
        console_handler.setFormatter(self.get_formatter()[0])
        return console_handler

    def file_handle(self, level="DUBUG"):
        # 文件控制器
        file_handler = logging.FileHandler("../log/log.txt", mode="a", encoding="utf-8")
        file_handler.setLevel(self.level)
        # 处理器添加格式器
        file_handler.setFormatter(self.get_formatter()[1])
        return file_handler

    def get_formatter(self):
        '''格式器'''
        # 定义格式器
        console_fmt = logging.Formatter(fmt="%(name)s--->%(levelname)s--->%(asctime)s--->%(message)s")
        file_fmt = logging.Formatter(fmt="%(levelname)s--->%(asctime)s--->%(message)s")
        # 这里返回的是元组
        return console_fmt, file_fmt

    def get_log(self):
        # 日志器添加控制台处理器
        self.logger.addHandler(self.console_handle())
        # 日志器添加文件处理器
        self.logger.addHandler(self.file_handle())
        # 返回日志实例对象
        return self.logger

# if __name__ == '__main__':
#     log = Log()
#     logger = log.get_log()
#     logger.info("你是日志，你是丢丢~")
