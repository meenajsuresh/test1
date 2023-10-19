from flask import Flask, render_template, request, redirect, url_for
# import json
from flask_mysqldb import MySQL

app = Flask(_name_)

# Database connection settings
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'p@ssw0rd'
app.config['MYSQL_DB'] = 'EmployeeDB'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM employees")
    employees = cur.fetchall()
    cur.close()
    return render_template('index.html', employees=employees)
    print(employees)
    return json.dumps(employees)