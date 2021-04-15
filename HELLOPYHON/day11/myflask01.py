from flask import Flask,render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Flask"

@app.route("/param", methods=['GET','POST'])
def param():
    if request.method == "POST":
        name = request.form.get('name', "kimchulsu")
    if request.method == "GET":
        name = request.args.get('name', "kimchulsu")  
    return "param="+name

@app.route("/forward.do")
def forward():
    title = "Good Morning"
    return render_template('forward.html',title=title)

@app.route("/db.do")
def db():
#     s_code db select -> 화면에 뿌려주시
    return render_template('db.html',title="good",list=[1,2,3])



if __name__ == "__main__":
    app.run()