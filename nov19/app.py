from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html",title="Home Page")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/conditional")
def conditional():
    user = {"name":"John","logged_in":True}
    return render_template("conditional.html",user = user)
@app.route("/items")
def items():
    items = ['Apple','Banana','Carrot']
    return render_template("items.html",items = items)

if __name__=="__main__":
    app.run(debug = True)