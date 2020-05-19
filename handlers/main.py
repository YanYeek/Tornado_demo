#!C:\Users\Administrator\Code F:\Anaconda\python.exe 3.6.4
# author: YanYeek  encoding: utf-8
# file: main.py  time: 2020/5/19 13:26
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    """
    首页 用户上传图片的展示
    """
    def get(self):
        return self.write("首页")

class ExploreHandler(tornado.web.RequestHandler):
    """
    最近上传的页面
    """
    def get(self):
        return self.write("发现或最近上传的图片页面")
    
class PostHandler(tornado.web.RequestHandler):
    """
    单个图片的详情页
    """
    def get(self,post_id):
        return self.write("详情页")