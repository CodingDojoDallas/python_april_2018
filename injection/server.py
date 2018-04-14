from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'full_friends')

@app.route('/')
def index():
    query = 'SELECT * from friends'
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends = friends)

@app.route('/', methods=['POST'])
def add_friend():
    # injection = '2011-01-01"); DROP TABLE friends; --'
    # query = 'INSERT INTO friends (name, age, friend_since) VALUES ("'+ request.form['name'] + \
    #     '", "' + request.form['age'] + '", "' + request.form['friend_since'] + '");'
    query = 'INSERT INTO friends (name, age, friend_since) VALUES (:name, :age, :friend_since)'
    data = {
        'name': request.form['name'],
        'age': request.form['age'],
        'friend_since': request.form['friend_since']
    }
    result = mysql.query_db(query, data)
    return redirect('/')
app.run(debug=True)
