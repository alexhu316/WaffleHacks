from flask import Flask
app = Flask(__name__)



@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template("register.html", form = form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html", form = form)
