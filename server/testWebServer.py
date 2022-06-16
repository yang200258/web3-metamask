import tornado.ioloop
import tornado.web
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop as ioloop


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")


class MainHandler(BaseHandler):
    # def initialize(self, database):
    #     self.database = database

    # def get(self):
    #     if not self.current_user:
    #         self.redirect("/login")
    #         return
    #     name = tornado.escape.xhtml_escape(self.current_user)
    #     self.write("Hello, " + name)
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        self.write("Hello, " + name)

    # async def get(self):
    #     http = AsyncHTTPClient()
    #     response = await http.fetch("http://www.baidu.com")
    #     json = tornado.escape.json_decode(response.body)
    #     self.render(response.body)

    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_body_argument("message"))


class LoginHandler(BaseHandler):
    def get(self):
        self.write('<html><body><form action="/login" method="post">'
                   'Name: <input type="text" name="name">'
                   '<input type="submit" value="Sign in">'
                   '</form></body></html>')

    def post(self):
        self.set_secure_cookie("user", self.get_argument("name"))
        self.redirect("/")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/login", LoginHandler),
        # (r"/myform", MainHandler, dict(database=database)),
    ], cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__")


def main():
    app = make_app()
    server = HTTPServer(app)
    server.bind(8888)
    server.start(0)  # forks one process per cpu
    ioloop.current().start()


if __name__ == "__main__":
    main()
