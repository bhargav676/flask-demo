from flask import Flask,request,render_template,url_for,redirect
from flask_pymongo import PyMongo
app=Flask(__name__)
app.config["MONGO_URI"]="mongodb+srv://bhargavk1290:951509290@cluster0.i5jvom9.mongodb.net/flask"
mongo=PyMongo(app)
register_collection=mongo.db.register
@app.route('/register',methods=["GET","POST"])
def register():
    if request.method=="POST":
        name=request.form.get('name')
        email=request.form.get('email')
        password=request.form.get('password')
        register_collection.insert_one({"name": name, "email": email, "password": password})
        return redirect(url_for('login'))
    return render_template('register.html')
@app.route('/login',methods=["GET","POST"])
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        enterpassword = request.form.get('password')
        user = register_collection.find_one({"email": email})
        if user["password"] == enterpassword:
            return redirect(url_for('dashboard',username=user["name"]))  
        else:
            return "Invalid email or password"
    return render_template('login.html')  
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/dashboard<username>')
def dashboard(username):
    return render_template('dashboard.html',username=username)

if __name__=="__main__":

    app.run(debug=True)
    