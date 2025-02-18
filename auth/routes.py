from flask import Blueprint, render_template, request, url_for, redirect,sessions,session

auth = Blueprint('auth', __name__, template_folder='templates')
auth.secret_key  = "'SSD!@#L%!E'"

@auth.route('/login', methods=['POST','GET'])
def login():
    if 'username' in session:
        return render_template('login.html', name=session['username'])
    if request.method == "POST":
        data = request.form
        username = data['username']
        session['username'] = username
        password = data['password']
        print(data['username'])
        return render_template('login.html', name=username)
    return render_template('login.html')