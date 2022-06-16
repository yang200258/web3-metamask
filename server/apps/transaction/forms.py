from wtforms import StringField
from wtforms_tornado import Form
from wtforms.validators import DataRequired, Regexp

mobile_regex = "^(13[0-9]|14[01456879]|15[0-3,5-9]|16[2567]|17[0-8]|18[0-9]|19[0-3,5-9])\d{8}$"


class SysForm(Form):
    mobile = StringField("手机号码",
                         validators=[DataRequired(message="请输入手机号码！"), Regexp(regex=mobile_regex, message="请输入合法的手机号码！")])
