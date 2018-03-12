# -*- coding:utf-8 -*-
import flask
import json
from flask import request
from flask import jsonify
import operations
import urllib

APP = flask.Flask(__name__)


@APP.route('/')
def index():
    return flask.render_template('index.html')


@APP.route('/hello/<name>/<what>')
def hello(name, what):
    return flask.render_template('hello.html', name=name, what=what)


@APP.route('/select/<sheet>', methods=['POST', 'GET'])
def select(sheet):
    if request.method == "POST":
        # 接收前端发来的数据,转化为Json格式,我个人理解就是Python里面的字典格式
        # print(request.get_json(force=True))
        # a.decode("utf-8")
        data = request.get_data().decode("utf-8")
        data = urllib.parse.unquote(data)
        filter = {}
        for i in data.split():
            filter[i.split('=')[0]] = i.split('=')[1]
        # # print(type(data['sheetname']))
        # # data1 = {u'age': 23, u'name': u'Peng Shuang', u'location': u'China'}
        # # data = jsonify(data1)
        # # 然后在本地对数据进行处理,再返回给前端
        # print(data)
        # sheetname = data
        # print(data)
        print(filter)
        data = operations.search(sheet, **filter)

        # Output: {u'age': 23, u'name': u'Peng Shuang', u'location': u'China'}
        # print data
        # print(data)
        print(data)
        return jsonify(data)
    else:
        return flask.render_template('select.html', sheet=sheet)
    # pass


@APP.route('/insert/<sheet>', methods=['POST', 'GET'])
def insert(sheet):
    if request.method == "POST":
        data = request.get_data().decode('utf-8')
        data = urllib.parse.unquote(data)
        data = data.replace('&', ' ')
        print(data)
        print(sheet)
        insertvalue = {}
        for i in data.split():
            insertvalue[i.split('=')[0]] = i.split('=')[1]
        print(insertvalue)
        operations.insert(sheet, **insertvalue)
        return jsonify(insertvalue)

    else:
        pass


# @APP.route("/sendjson", methods=['POST','GET'])
# def sendjson():
# 	if request.method == "POST":
# 		#接受前端发来的数据
# 		data = json.loads(request.form.get('data'))
# 		# decoded_data = data.decode('utf-8');
# 		# json_data = json.loads(decoded_data)
# 		# dat = models.search("*","Doctorinfo")
# 		# data = dat[0]

# 		lesson: "Operation System"
# 		score: 100
# 		lesson = data["lesson"]
# 		score = data["score"]

# 		info = dict()
# 		info['name'] = "pengshuang"
# 		info['lesson'] = lesson
# 		info['score'] = score
# 		# return flask.render_template('sendjson.html')
# 		# return jsonify(info)
# 		return data
# 	else:
# 		return flask.render_template('sendjson.html')

if __name__ == '__main__':
    APP.debut = True
    APP.debug = False
    APP.run(host="0.0.0.0", port=5000)
