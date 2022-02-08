import os

from flask import  Flask, render_template, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))
from flask import request

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/register", methods=["POST"])
def register():
    userid=request.form.get("userid")
    username=request.form.get("username")
    password=request.form.get("password")
    db.execute("INSERT INTO users (userid, username, password) VALUES (userid:, :username, :password)", {"userid": userid, "username":username, "passwrd":password})
    db.commit()
    return render_template("registersuccess.html")

@app.route("/loginsuccess")
def loginsuccess():
    return render_template('loginsuccess.html')

@app.route("/login", methods=["POST"])
def login():
    #  userid=request.form.get("userid")
    username=request.form.get("username")
    password=request.form.get("password")
    user=db.execute("SELECT * FROM users WHERE username=:username AND password=:password" , {"username":username, "password":password})
    session["userid"]=user["userid"]
    session["logged_in"]=True

    return render_template("homepage.html", )


    






