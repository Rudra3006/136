from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

@app.route("/")
def planet_date():
    return jsonify({
        'data':data,'success':'success'
    })

@app.route("/details")
def details():
    name=request.args.get('name')
    planetdata=next(i for i in data if i['name']==name)
    return jsonify({
        'data':planetdata,'success':'success'
    })
app.run()