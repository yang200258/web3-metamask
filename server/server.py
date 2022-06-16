from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.options import define, options

from peewee_async import Manager

from tornado.web import Application

# from server.web3_backend.settings import database, settings
# from server.web3_backend.urls import url_pattern
from web3_backend.settings import settings, database
from web3_backend.urls import url_pattern

define('port', default=9988, help="xxxxx", type=int)


def make_app():
    return Application(url_pattern, **settings)


def main():
    app = make_app()

    objects = Manager(database)
    database.set_allow_sync(False)
    app.objects = objects

    server = HTTPServer(app)
    server.bind(options.port)

    server.start(0)  # forks one process per cpu
    IOLoop.current().start()


if __name__ == "__main__":
    main()

