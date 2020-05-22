#!C:\Users\Administrator\Code F:\Anaconda\python.exe 3.6.4
# author: YanYeek  encoding: utf-8
# file: users.py  time: 2020/5/19 13:47
import tornado.web
from utils.account import pas_encryption
from models.auth import User
from handlers.main import BaseHandler
class RegisterHandler(tornado.web.RequestHandler):
    """
    注册
    """
    def get(self):
        return self.render("register.html")
    
    def post(self):
        # 获取前端参数
        username = self.get_argument("username", "").strip()
        password = self.get_argument("password", "").strip()
        repeat_password = self.get_argument("repeat_password", "").strip()
        # 一 校验参数
        # 判断非空
        if not all([username, password, repeat_password]):
            return self.write("参数错误")
        # 判断格式
        if not (len(username) >=6 and len(password) >=6 and password==repeat_password):
            return self.write("格式错误")
        
        if User.check_username(username):
            return self.write("用户名已存在")
        # 加密 保留在实现
        passwd = pas_encryption(password)
        # 入库
        User.add_user(username, passwd) # 存入user数据库
        # 返回数据
        
        return self.redirect("/login")
    

class LoginHandler(BaseHandler):
    """
    登录
    """
    def get(self):
        return self.render("login.html")
    
    def post(self):
        # 获取用户名与密码
        username = self.get_argument("username", "").strip()
        password = self.get_argument("password", "").strip()
        # 验证 一般不需要
        
        #  将输入的明文密码与密文密码进行加密，是否等于密文密码。
        if username and password:
            # 数据对比
            user = User.check_username(username)  # 获取用户的实例
            pas = user.password if user else ""
            # 用传入的密码加存储的密码作为盐解密 然后对比数据库的加密密码
            if pas_encryption(password, pas, False) == pas.encode("utf8"):
                self.session.set("user", username)
                next = self.get_argument("next","/")
                return self.redirect(next) # 路由跳转
            else:
                return self.write("用户名和密码错误")
                
                
        # 设置会话
        else:
            return self.write("参数错误")
        
        