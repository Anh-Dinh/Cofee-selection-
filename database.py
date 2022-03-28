import sqlite3

CREAT_BEANS_TABLE="CREATE TABLE IF NOT EXISTS beans(id INTERGER PRIMARY KEY, name TEXT,method TEXT, rating INTEGER);"
INSERT_BEANS='INSERT INTO beans (name,method,rating) VALUES(?,?,?);'

GET_ALL_BEANS='SELECT * FROM beans;'
GET_BEANS_BY_NAME='SELECT * FROM beans WHERE name=?;'
GET_BEST_PREPARATION_FOR_BEAN="""
SELECT * FROM beans
WHERE name = ?
ORDER BY rating DESC
LIMIT 1;"""
REMOVE_BEANS_BY_NAME="DELETE FROM beans WHERE name=?;"

def connect():
    return sqlite3.connect("data")

def create_table(connection):
    with connection:
        connection.execute(CREAT_BEANS_TABLE)
        
def add_bean(connection,name,method,rating):
    with connection:
        connection.execute(INSERT_BEANS,(name,method,rating))

def get_all_beans(connection):
    with connection:
        return connection.execute(GET_ALL_BEANS).fetchall()# fetch all give a list of rows that were returned by database  

def get_beans_by_name(connection,name):
    with connection:
        return connection.execute(GET_BEANS_BY_NAME,(name,)).fetchall() # NAME IS TUPLE 

def get_best_preparation_for_bean(connection,name):
    with connection:
        return connection.execute(GET_BEST_PREPARATION_FOR_BEAN,(name,)).fetchone() # bc return only 1 row
    
def remove_beans_by_name(connection,name):
    with connection:
        return connection.execute(REMOVE_BEANS_BY_NAME,(name,)).fetchall()