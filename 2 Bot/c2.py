import sqlite3
import random
from datetime import datetime, timedelta

# Create a SQLite database named '1krow.db' or connect to an existing one
conn = sqlite3.connect('1krow.db')
cursor = conn.cursor()

# Create a table to store the data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS referrals (
        id INTEGER PRIMARY KEY,
        referrer_id INTEGER,
        referred_user_id INTEGER,
        time TEXT
    )
''')

# Insert 500 rows with referrer_id as 6690362261
specific_referrer_id = 6690362261
for _ in range(500):
    referred_user_id = random.randint(10**8, 10**9 - 1)  # Generate random 8-9 digit values
    random_time = datetime.now() - timedelta(days=random.randint(1, 365))
    time = random_time.strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('INSERT INTO referrals (referrer_id, referred_user_id, time) VALUES (?, ?, ?)', (specific_referrer_id, referred_user_id, time))

# Insert 500 rows with random values for referrer_id
for _ in range(500):
    referrer_id = random.randint(10**8, 10**9 - 1)  # Generate random 8-9 digit values
    referred_user_id = random.randint(10**8, 10**9 - 1)
    random_time = datetime.now() - timedelta(days=random.randint(1, 365))
    time = random_time.strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('INSERT INTO referrals (referrer_id, referred_user_id, time) VALUES (?, ?, ?)', (referrer_id, referred_user_id, time))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database '1krow.db' created and populated with 1000 rows of random data, including 500 with specific referrer_id.")
