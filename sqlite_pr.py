import sqlite3



def exec_query(query):
    conn = sqlite3.connect('./chinook.db')
    cursor = conn.cursor()
    cursor.execute(query)
    record = cursor.fetchall()
    return record


if __name__ == '__main__':
    q = 'SELECT * FROM customers;'
    print(exec_query(q))