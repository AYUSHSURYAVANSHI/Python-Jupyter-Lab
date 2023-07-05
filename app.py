from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/Hello_World2")
def hello_world1():
    return "<h1>Hello, World!</h1>"

@app.route("/Hello_World2")
def hello_world2():
    return "<h1>Hello, World!</h1>"

@app.route("/Hello_World3")
def hello_world4():
    return "<h1>Hello, World!</h1>"

@app.route("/Hello_World4")
def hello_world5():
    return "<h1>Hello, World!</h1>"

@app.route("/test2")
def test2():
    data = request.args.get('x')
    return '''this is a data return by my url'''.format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")
