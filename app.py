
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
# initialize the app with the extension
db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phno = db.Column(db.String)

@app.route("/niru", methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        users = User.query.all()
        return render_template('index.html', users = users)
    
    
    
    if request.method == "POST":
        usr = User(name=request.form["name"], phno = request.form["phno"])
        db.session.add(usr)
        db.session.commit()
        return redirect('/niru')
    
if __name__ == '__main__':
    app.run(debug=True)