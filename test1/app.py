from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",title="Home Page")
@app.route("/hello/<name>")
def hello(name):
    return render_template("hello.html",name= name,title="Hello Page")
@app.route("/add",methods=["GET","POST"])
def add():
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            result = num1+num2
            return render_template("add.html",result = result, title = "Addition")
        except ValueError:
             return render_template("add.html",error = "Please enter valid number", title = "Addition")
    return render_template("add.html",title="Enter the values")
@app.route("/subtract",methods=["GET","POST"])
def subtract():
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            result = num1-num2
            return render_template("subtract.html",result = result, title = "Subtraction")
        except ValueError:
             return render_template("subtract.html",error = "Please enter valid number", title = "Addition")
    return render_template("subtract.html",title="Enter the values")
@app.route("/multiply",methods=["GET","POST"])
def multiply():
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            result = num1*num2
            return render_template("multiply.html",result = result, title = "Multiplication")
        except ValueError:
             return render_template("multiply.html",error = "Please enter valid number", title = "Addition")
    return render_template("multiply.html",title="Enter the values")
@app.route("/divide",methods=["GET","POST"])
def divide():
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            result = num1/num2
            return render_template("divide.html",result = result, title = "Division")
        except ValueError:
             return render_template("divide.html",error = "Please enter valid number", title = "Addition")
    return render_template("divide.html",title="Enter the values")
@app.route("/modulus",methods=["GET","POST"])
def modulus():
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            result = num1%num2
            return render_template("modulus.html",result = result, title = "Division")
        except ValueError:
             return render_template("modulus.html",error = "Please enter valid number", title = "Addition")
    return render_template("modulus.html",title="Enter the values")


if __name__=="__main__":
    app.run(debug = True)