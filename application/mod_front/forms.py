from wtforms import Form
from flask_wtf.file import FileField


class Front(Form):
    xlsx_file = FileField()