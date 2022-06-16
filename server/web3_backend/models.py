from datetime import datetime
from peewee import Model, DateTimeField
from web3_backend.settings import database


class BaseModel(Model):
    # add_time = DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        database = database
