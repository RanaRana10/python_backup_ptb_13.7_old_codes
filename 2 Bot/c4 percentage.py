import sqlite3
import random
from datetime import datetime, timedelta

# Function to generate a random name with the first letter of each word capitalized
def generate_random_name():
    name = ' '.join(''.join(random.choice('abcdefghijklmnopqrstuvwxyz').capitalize() for _ in range(random.randint(15, 30))) for _ in range(3))
    return name

# Function to display a progress bar
def print_progress_bar(iteration, total, bar_length=50):
    progress = iteration / total
    arrow = '=' * int(round(bar_length * progress))
    spaces = ' ' * (bar_length - len(arrow))
    print(f'[{arrow}{spaces}] {int(progress * 100)}%')

# Create a SQLite database named 'xyz.db' or connect to an existing one
conn = sqlite3.connect('xyz.db')
cursor = conn.cursor()

# Create a table to store the data with referrer_name and referred_user_name
cursor.execute('''
    CREATE TABLE IF NOT EXISTS referrals (
        id INTEGER PRIMARY KEY,
        referrer_id INTEGER,
        referrer_name TEXT,
        referred_user_id INTEGER,
        referred_user_name TEXT,
        time TEXT
    )
''')

# Create a list to hold the data
data = []

# Insert 100 rows with referrer_id as 6690362261 and the name "Rana Universe"
specific_referrer_id = 6690362261
specific_referrer_name = "Rana Universe"
for i in range(5950):
    referred_user_id = random.randint(10**8, 10**9 - 1)  # Generate random 8-9 digit values
    referred_user_name = generate_random_name()
    random_time = datetime.now() - timedelta(days=random.randint(1, 365))
    time = random_time.strftime('%Y-%m-%d %H:%M:%S')
    data.append((specific_referrer_id, specific_referrer_name, referred_user_id, referred_user_name, time))
    print_progress_bar(i + 1, 100)

# Insert 900 rows with random values for referrer_id and names
total_random_rows = 2577500
for i in range(total_random_rows):
    referrer_id = random.randint(10**8, 10**9 - 1)  # Generate random 8-9 digit values
    referrer_name = generate_random_name()
    referred_user_id = random.randint(10**8, 10**9 - 1)
    referred_user_name = generate_random_name()
    random_time = datetime.now() - timedelta(days=random.randint(1, 365))
    time = random_time.strftime('%Y-%m-%d %H:%M:%S')
    data.append((referrer_id, referrer_name, referred_user_id, referred_user_name, time))
    print_progress_bar(i + 1, total_random_rows)

# Shuffle the data to mix the rows
random.shuffle(data)

# Insert the shuffled data into the database
cursor.executemany('INSERT INTO referrals (referrer_id, referrer_name, referred_user_id, referred_user_name, time) VALUES (?, ?, ?, ?, ?)', data)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database 'xyz.db' created and populated with 1000 rows of random data, including 100 with specific referrer_id and name, with the rows mixed.")
