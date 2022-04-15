from flask import Flask,redirect,url_for, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/user/<name>')
def getname(name):
    return render_template('getname.html',names = name)



if __name__ == "__main__":
    app.run(debug=True)