from flask import Flask, render_template , url_for, flash, redirect
from forms import RegistrationsForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '2b8aacd0b5d9784f84c470941d87e5e9'

app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.colum(db.Integer, primary_key=True ),
    username = db.colum(db.String()),
    password = db.colum(db.String())

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title = 'about it')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationsForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('register.html', title='Login', form=form)






if __name__ == "__main__":
    app.run(debug=True)
