from app import app
from flask import render_template, redirect, request, session, flash
from app.models.user_model import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

#renders index.html which will display both login and registration
@app.route('/')
def index():
    return render_template ("index.html")

#Post method for registering a new user
@app.route('/user/register', methods=['POST'])
def register_user():
    if not User.validate_user_registration(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "user_name":request.form['user_name'],
        "email":request.form['email'],
        "password":pw_hash
    }
    user_id = User.save(data)
    session['user_id'] = user_id
    return redirect('/dashboard')

#Post method for login in new user
@app.route('/user/login', methods=['POST'])
def login_user():
    user = User.get_by_email(request.form)
    if not user:
        flash("Invalid Email.","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard')

#loads a dashboard that can only be seen by the session user
@app.route('/menu')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    user = User.get_by_id(data)
    return render_template('menu.html', user = user)

@app.route('/view/user/<int:user_id>')
def view_user(user_id):
    data = {
        'id': user_id
    }
    user = User.get_by_id(data)
    return render_template('view_user.html', user = user)


#logs out current user session
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')