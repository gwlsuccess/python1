from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '2018/6/1 hello python'

if __name__ == '__main__':
    app.run()

