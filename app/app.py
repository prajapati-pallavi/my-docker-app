from flask import Flask
import mysql.connector
import time

app = Flask(__name__)

def connect_db():
    time.sleep(5)  # wait for MySQL to start
    return mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="testdb"
    )

@app.route('/')
def home():
    try:
        print("Attempting to connect to MySQL...")
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        result = cursor.fetchone()
        return f"Connected to MySQL: {result}"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)