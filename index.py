from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '2018/6/1 hello python'

@app.route('/news')
def news():
    return '内蒙古新闻资讯'

if __name__ == '__main__':
    app.run()

