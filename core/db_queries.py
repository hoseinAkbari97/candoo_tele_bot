import mysql.connector
from datetime import datetime, timedelta

master_conn_info = {
    "host": "192.168.248.12",
    "user": "root",
    "password": "DenZel00@",
    "database": "_smsengine"
}

def get_outbound_count():
    try:
        conn = mysql.connector.connect(**master_conn_info)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM _outbound_messages")
        result = cursor.fetchone()
        return result[0] if result else 0
    except Exception as e:
        return f"DB Error: {e}"
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
