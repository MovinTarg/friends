from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'full_friends')

@app.route('/')
def index():
    query = "SELECT first_name, last_name, age, DATE_FORMAT(created_at, '%M, %D') AS date, DATE_FORMAT(created_at, '%Y') AS year FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    query = "Insert INTO friends (first_name, last_name, age, created_at, updated_at) VALUES (:first_name, :last_name, :age, NOW(), NOW())"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)