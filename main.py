from flask import Flask, render_template
from numpy import number
app = Flask(__name__)


@app.route('/')
def redirect():
    return "click here to PLAY!!!"


@app.route('/play')
def play():
    return render_template("index.html",number=3)


@app.route('/play/<num>')
def playwithnum(num):
    return render_template("index.html", number=int(num))


@app.route('/play/<num>/<color>')
def playwitnclr(num, color):
    return render_template("index.html", number=int(num), clr=color)


if __name__ == "__main__":
    app.run(debug=True)
