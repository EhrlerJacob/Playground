from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return "Welcome!".title()

@app.route('/play')
def play():
    return render_template("index.html", num=3, color="blue")

@app.route('/play/<int:num>')
def playX(num):
    return render_template("index.html", num=num, color="blue")


@app.route('/play/<int:num>/<string:color>')
def playXL(num, color):
    return render_template("index.html", num=num, color=color)








if __name__ == "__main__":
    app.run(debug=True, port=5000)