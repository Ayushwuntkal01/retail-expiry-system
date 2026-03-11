import mysql.connector
from config import MYSQL_CONFIG

def get_connection():
    try:
        print("DEBUG: Trying MySQL connection...")
        conn = mysql.connector.connect(**MYSQL_CONFIG)
        print("DEBUG: Connection successful.")
        return conn
    except Exception as e:
        print("ERROR: Could not connect to MySQL:", e)
        return None


def fetch_one(query, params=None):
    try:
        conn = get_connection()
        if conn is None:
            return None

        cur = conn.cursor(dictionary=True)
        print("DEBUG: Running SELECT (fetch_one):", query)
        cur.execute(query, params or ())
        row = cur.fetchone()

        cur.close()
        conn.close()
        return row
    except Exception as e:
        print("ERROR in fetch_one:", e)
        return None


def fetch_all(query, params=None):
    try:
        conn = get_connection()
        if conn is None:
            return None

        cur = conn.cursor(dictionary=True)
        print("DEBUG: Running SELECT (fetch_all):", query)
        cur.execute(query, params or ())
        rows = cur.fetchall()

        cur.close()
        conn.close()
        return rows
    except Exception as e:
        print("ERROR in fetch_all:", e)
        return None


def execute(query, params=None):
    try:
        conn = get_connection()
        if conn is None:
            return None

        cur = conn.cursor()
        print("DEBUG: Running SQL (execute):", query)
        cur.execute(query, params or ())
        conn.commit()

        cur.close()
        conn.close()
        return True
    except Exception as e:
        print("ERROR in execute:", e)
        return False
    
