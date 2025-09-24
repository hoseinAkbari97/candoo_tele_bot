import mysql.connector
# from datetime import datetime, timedelta
# from dotenv import load_dotenv
# import os

# load_dotenv()

master_conn_info = {
    "host": "192.168.248.12",
    "user": "root",
    "password": "DenZel00@",
    "database": "_smsengine"
}

sdp_tci_conn_info = {
    "host": "172.22.172.116",
    "user": "sdpuser",
    "password": "dO#dJn#240@",
    "database": "smsserver_p2"
}

# master_conn_info = {
#     "host": os.getenv("MASTER_HOST"),
#     "user": os.getenv("MASTER_USER"),
#     "password": os.getenv("MASTER_PASSWORD"),
#     "database": os.getenv("MASTER_DB")
# }

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
            
def send_test_message():
    try:
        conn = mysql.connector.connect(**sdp_tci_conn_info)
        cursor = conn.cursor()
        
        # Execute the INSERT query
        cursor.execute("""
            INSERT INTO messageout (MessageTo, MessageFrom, MessageText, Priority, UserId, ValidityPeriod, counter)
            VALUES (
                "9382997652",
                "982142750000",
                CONCAT(NOW(), " Test for TCI"),
                1, 14, 120, 1
            )
        """)
        
        # Commit the transaction
        conn.commit()
        
        # Return success message with the number of rows affected
        return f"Test message inserted successfully. Rows affected: {cursor.rowcount}"
        
    except Exception as e:
        # Rollback in case of error
        if conn:
            conn.rollback()
        return f"DB Error: {e}"
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
