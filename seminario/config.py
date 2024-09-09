import mysql.connector

def connect_db():
    conn = mysql.connector.connect(
        user='lara',
        password='LaraVictoria123_@;',
        host='127.0.0.1',
        database='login'
    )
    return conn

def create_users_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(50) NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
    except mysql.connector.IntegrityError:
        print(f"Usuário '{username}' já existe.")
    conn.close()

def get_user_by_username(username):
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def user_exists(username):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s limit 1", (username,))
    exists = cursor.fetchone() is not None
    conn.close()
    
    return exists
