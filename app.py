from flask import Flask
from flask import request,render_template,jsonify

print('Changes in derived branch')
app = Flask(__name__)

@app.route("/home", methods=['GET','POST'])
def main_page():
    return render_template('index.html')

@app.route('/math',methods=['POST'])
def operation():
    if request.method=='POST':
        ops=request.form['operation']
        a=int(request.form['num1'])
        b=int(request.form['num2'])
        if ops=='add':
            results=a+b
            return render_template('results.html',result=results)

@app.route('/postman',methods=['POST'])
def post_data():
    if request.method=='POST':
        ops=request.json['operation']
        a=int(request.json['num1'])
        b=int(request.json['num2'])
        if ops=='add':
            results=a+b
            return jsonify(results)


if __name__=="__main__":
    app.run(host="0.0.0.0")
