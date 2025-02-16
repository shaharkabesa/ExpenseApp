from flask import Flask, request, render_template, url_for, redirect,sessions,session
from auth.routes import auth



app = Flask(__name__)
app.register_blueprint(auth, url_prefix='/auth')
app.secret_key  = "'SSD!@#L%!E'"
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['POST','GET'])
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
@app.route('/logout')
def logout():   
  session.clear()
  return redirect(url_for('login'))


@app.route('/register', methods=["GET","POST"])
def register():
    return render_template('register.html')
if __name__ == "__main__":
    app.run(debug=True)