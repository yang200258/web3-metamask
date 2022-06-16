from peewee import MySQLDatabase

from apps.users.models import User

from server.settings import database

database = MySQLDatabase(
    'blog', host="127.0.0.1", port=3306, user="root", password="Yy141025"
)


def init():
    # 生成用户表
    database.create_tables([User])


if __name__ == "__main__":
    init()
