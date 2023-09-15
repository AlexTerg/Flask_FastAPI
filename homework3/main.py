from flask import Flask, render_template, request
from form import LoginForm
from model import db, User
import hashlib
from flask_wtf.csrf import CSRFProtect



app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)
csrf = CSRFProtect(app)

@app.cli.command('init-db')
def init_db():
    db.create_all()
    

@app.route('/', methods=['GET', 'POST'])
def register():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.mail.data
        password = form.password.data
        pswd_hash = hashlib.sha256(password.encode()).digest()
        user = User(
            firstname=firstname,
            lastname=lastname,
            mail=email,
            pswd=pswd_hash 
        )
        db.session.add(user)
        db.session.commit()
    return render_template('register.html', form=form)