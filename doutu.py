
import requests
import re
import pymysql

db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='doutu',
    charset='utf8'
)
cursor = db.cursor()


def getImagesList(page=1):
    res = requests.get('http://www.doutula.com/photo/list/?page={}'.format(page))
    html = res.text
    reg = r'data-original="(.*?)".*?alt="(.*?)"'
    reg = re.compile(reg, re.S)
    imagesList = re.findall(reg, html)
    for i in imagesList:
        # print(i)
        cursor.execute("insert into images(`name`,`imageUrl`) VALUES ('{}','{}')".format(i[1], i[0]))
        db.commit()

for i in range(1,1084):
    print("正在爬取第{}页".format(i))
    getImagesList(i)
db.close()
