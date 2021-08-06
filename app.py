from flask import Flask, render_template
import mysql.connector
from mysql.connector import Error


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    connection = None
    connection_result = ""
    query = "SELECT * FROM Employee"
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="test123",
            database="PythonDB2"
        )
        cursor = connection.cursor()
        cursor.execute(query)
        connection_result = str(cursor.fetchall())
    except Error as e:
        print(f"The error is '{e}' occurred")
        connection_result = "connection to db failed, please try again"
    return connection_result
