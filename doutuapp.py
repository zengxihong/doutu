from flask import Flask
import pymysql
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def search():
    kw = request.args.get('kw')  # 获取用户 get 请求的参数
    count = request.args.get('count')  # 获取用户 get 请求的参数
    cursor.execute("select * from images where `name` like '%{}%'".format(kw))
    data = cursor.fetchmany(int(count))
    return render_template('index.html', images=data)


if __name__ == '__main__':
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='123456',
        db='doutu',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor,
    )
    cursor = conn.cursor()

    app.run(debug=True)