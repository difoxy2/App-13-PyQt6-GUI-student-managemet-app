import mysql.connector
import sqlite3


def DB_CONNECT():
    return sqlite3.connect('database.db')
    #return mysql.connector.connect(host="localhost", user="root",password="pythoncourse",database='app14')
