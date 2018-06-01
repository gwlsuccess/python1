from flask import Flask
from flask_script import Manager
app = Flask(__name__)
manager = Manager(app)
@app.route('/')
def index():
    return '2018/6/1 hello python'

@app.route('/news')
def news():
    return '内蒙古新闻资讯,请选择浏览'

if __name__ == '__main__':
    manager.run()

