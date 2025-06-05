from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/sendlink')
def sendlink():
    return render_template('sendlink.html')

@app.route('/finishSignIn')
def finish_signin():
    return render_template('finishSignIn.html')

if __name__ == '__main__':
    app.run(debug=True)
