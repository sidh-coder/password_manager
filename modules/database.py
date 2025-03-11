import mysql.connector
from config import db_config

def connect_db():
    return mysql.connector.connect(auth_plugin='mysql_native_password',**db_config)

def add_entry(site_name,username,encrypted_password):
    db = connect_db()
    cursor = db.cursor()
    query = "insert into passwords(site_name,username,password) values (%s,%s,%s)"
    cursor.execute(query,(site_name,username,encrypted_password))
    db.commit()
    cursor.close()
    db.close()

def create_table():
    db = connect_db()
    cursor = db.cursor()
    query = """create table if not exists passwords (
    id int auto_increment primary key,
    site_name varchar(100) not null,
    username varchar(50) not null,
    password blob not null,
    created_at timestamp default current_timestamp,
    last_used timestamp default current_timestamp on update current_timestamp
    )"""

    cursor.execute(query)
    db.commit()
    cursor.close()
    db.close()

def get_entry(site,username):
    db = connect_db()
    cursor = db.cursor(dictionary=True, buffered=True)
    query = "select * from passwords where site_name = %s AND username = %s"
    cursor.execute(query,(site,username,))
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return result

def list_entries():
    """List all password entries (only site name and username)."""
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    sql = "SELECT site_name, username FROM passwords"
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    db.close()
    return results

def delete_entry(site):
    """Delete a password entry by site name."""
    db = connect_db()
    cursor = db.cursor()
    sql = "DELETE FROM passwords WHERE site_name = %s"
    cursor.execute(sql, (site,))
    db.commit()
    cursor.close()
    db.close()

def create_user_table():
    db = connect_db()
    cursor = db.cursor()
    query = """CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    master_password blob NOT NULL,
    email VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);"""
    cursor.execute(query)
    db.commit()
    cursor.close()
    db.close()

def add_user(username,master_password,email_id):
    db = connect_db()
    cursor = db.cursor()
    query = "insert into users(username,master_password,email) values (%s,%s,%s)"
    cursor.execute(query,(username,master_password,email_id))
    db.commit()
    cursor.close()
    db.close()

def list_user_data(username):
    db = connect_db()
    cursor = db.cursor(dictionary=True)
    query = "SELECT username,master_password,email from users where username = %s"
    try:
        cursor.execute(query,(username,))
        results = cursor.fetchone()
        cursor.close()
        db.close()
        return results
    except:
        return False

def delete_user(username):
    db = connect_db()
    cursor = db.cursor()
    sql = "DELETE FROM passwords WHERE username = %s"
    cursor.execute(sql, (username,))
    sql2 = "DELETE FROM users WHERE username = %s"
    cursor.execute(sql2, (username,))
    db.commit()
    cursor.close()
    db.close()