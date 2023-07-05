from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/Hello_World2")
def hello_world1():
    return "<h1>Hello, World!</h1>"

def math_operation():
    if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['nums1'])
        num1 = int(request.form['nums2'])
        if(ops == 'add'):
            r = num1 + num2
            result = 'the sum of  + str(nums1) + 'add' + str(nums2) + "is" + str

if __name__=="__main__":
    app.run(host="0.0.0.0")