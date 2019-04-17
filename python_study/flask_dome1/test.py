# -*- coding=utf-8 -*-
# @Time     :2019/4/15 16:47
# @Author   :ZhouChuqi
from flask import Flask
app = Flask(__name__)
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
