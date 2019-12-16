import sqlite3
import os


def exec_query(query):
    db_path = os.path.join(os.getcwd(), 'chinook.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(query)
    record = cursor.fetchall()
    return parse_response(record)


def parse_response(resp) -> str:
    text = ""
    for row in resp:
        text += str(row)[1:-1] + "<br>"
    return text


if __name__ == '__main__':
    q = 'SELECT COUNT(DISTINCT FirstName) FROM customers;'
    exec_query(q)
