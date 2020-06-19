from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort


app = Flask(__name__)

@app.route('/')
def home():
  return "hello"

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return "login sucessful"
    return render_template('login.html', error=error)


if __name__ == "__main__":
  app.run(port=2000)

