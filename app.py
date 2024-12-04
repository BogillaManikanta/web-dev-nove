from flask import Flask
from flask import render_template,request

app = Flask(__name__) #To create an object of Flask

@app.route("/")
@app.route("/home")
def home():
    return "<h1>This is homepage</h1?>"
@app.route("/about")
def about():
    return render_template("about.html")
 
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello, {name}"
@app.route("/add",methods=["POST"])
def add_numbers():
    data = request.get_json()
    num1 = data.get('num1')
    num2 = data.get('num2')
    result = num1 + num2
    return jsonify({"result":result})
if __name__ =="__main__":
    app.run(debug = True)