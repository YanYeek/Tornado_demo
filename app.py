#!C:\Users\Administrator\Code F:\Anaconda\python.exe 3.6.4
# author: YanYeek  encoding: utf-8
# file: app.py  time: 2020/5/19 13:01
import tornado.ioloop
import tornado.web  # web 应用api
import tornado.options
from  tornado.options import define, options
from handlers.main import IndexHandler, ExploreHandler, PostHandler,UpdateHandler
from handlers.users import RegisterHandler,LoginHandler



define("port", default="8888", help="Listening port", type=int)



class Application(tornado.web.Application):
    def __init__(self):
        handlers = [ # 配置路由
            (r"/", IndexHandler),
            (r"/explore", ExploreHandler),
            (r"/post/(?P<post_id>[0-9]+)", PostHandler),
            (r"/register", RegisterHandler),
            (r"/login", LoginHandler),
            (r"/update", UpdateHandler),
        ]
        settings = dict(
            debug = True,  # 开启测试模式
            template_path = "templates", # 配置模板路径
            cookie_secret="YanYeek",
            xsrf_cookies=True,  # 跨站点请求伪造保护开启
            pycket={  # Redis配置
                'engine': 'redis',
                'storage': {
                    'host': '127.0.0.1',  # 虚拟机IP
                    'port': 6379,
                    'db_sessions': 7,
                    'max_connections': 2 ** 31,
                },
                'cookies': {
                    # 设置过期时间
                    'expires_days': 2,
                    # 'expires':None, #秒
                },
            },
            login_url="/login",  # 设置的是当你没有权限访问时所跳转的页面路由
            static_path="statics",  # 配置静态文件路径
        )
        super().__init__(handlers, **settings)
    


if __name__ == "__main__":  # 只有在当前文件运行是才会执行
    tornado.options.parse_command_line() # 命令行
    application = Application()          # 实例化
    application.listen(options.port)     # 设置监听端口
    tornado.ioloop.IOLoop.current().start()  # 开启tornodo服务