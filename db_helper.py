import sqlite3
import pandas as pd

def hello_db():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses(
            ID INTEGER PRIMARY KEY,
            DATE TEXT NOT NULL,
            CATEGORY TEXT NOT NULL,
            AMOUNT INT NOT NULL,
            NOTES TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_expense(date, category, amount, notes):
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO expenses(DATE, CATEGORY, AMOUNT, NOTES)
        VALUES(?,?,?,?)
    ''', (date, category, amount, notes))
    conn.commit()
    conn.close()

def view_all_expenses():
    conn = sqlite3.connect('finance.db')
    df = pd.read_sql_query("SELECT * FROM expenses", conn)
    conn.close()
    return df
