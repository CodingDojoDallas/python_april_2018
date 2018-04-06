from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'shhhhhhhh'

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    print request.form

    print 'andy is AWEEEEESOMMMMMEEEE'

    if request.form['whattodo'] == 'login':
        session['uname'] = request.form['username']
        session['pword'] = request.form['password']
        return redirect('/welcome')
    else:
        return redirect('/')

@app.route('/welcome')
def welcome():
    print session
    session['count'] += 1
    return render_template('welcome.html', name=session['uname'], count=session['count'])

app.run(debug=True)
