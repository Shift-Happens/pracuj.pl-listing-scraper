import sqlite3
import json

def get_db_connection():
    connection = sqlite3.connect('job_offers.db')
    return connection

def create_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''s
        CREATE TABLE IF NOT EXISTS job_offers (
            id TEXT PRIMARY KEY,
            title TEXT,
            company TEXT,
            technologies TEXT,
            salary TEXT,
            work_modes TEXT,
            contract_types TEXT,
            workplace TEXT
        )
    ''')
    connection.commit()
    cursor.close()
    connection.close()

def add_or_update_offers(offers):
    connection = get_db_connection()
    cursor = connection.cursor()
    new_offers = []
    for offer in offers:
        cursor.execute("SELECT * FROM job_offers WHERE id=?", (offer['id'],))
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO job_offers (id, title, company, technologies, salary, work_modes, contract_types, workplace) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                           (offer['id'], offer['title'], offer['company'], json.dumps(offer['technologies']), offer['salary'], json.dumps(offer['work_modes']), json.dumps(offer['contract_types']), json.dumps(offer['workplace'])))
            new_offers.append(offer)
    connection.commit()
    cursor.close()
    connection.close()
    return new_offers