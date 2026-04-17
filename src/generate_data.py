import os
import sqlite3
import random
from datetime import datetime, timedelta

print("START: running generate_data.py")
random.seed(42)

DB_PATH = os.path.abspath("data/raw/funnel.db")
print("DB_PATH =", DB_PATH)
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

COUNTRIES = ["UK", "DE", "FR", "NL", "ES", "IT"]
CHANNELS = ["organic", "paid_search", "social", "email", "referral"]
DEVICES = ["desktop", "mobile", "tablet"]

def rand_date(start, end):
    delta = end - start
    return start + timedelta(seconds=random.randint(0, int(delta.total_seconds())))

def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.executescript("""
    DROP TABLE IF EXISTS users;
    DROP TABLE IF EXISTS sessions;
    DROP TABLE IF EXISTS events;
    DROP TABLE IF EXISTS transactions;

    CREATE TABLE users (
        user_id INTEGER PRIMARY KEY,
        signup_ts TEXT,
        country TEXT,
        acquisition_channel TEXT
    );

    CREATE TABLE sessions (
        session_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        session_ts TEXT,
        device TEXT
    );

    CREATE TABLE events (
        event_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        event_ts TEXT,
        event_type TEXT,
        session_id INTEGER
    );

    CREATE TABLE transactions (
        transaction_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        purchase_ts TEXT,
        revenue_gbp REAL
    );
    """)

    n_users = 2000
    start = datetime(2025, 10, 1)
    end = datetime(2025, 12, 31)

    users = []
    for user_id in range(1, n_users + 1):
        signup_ts = rand_date(start, end)
        users.append((user_id, signup_ts.isoformat(),
                      random.choice(COUNTRIES),
                      random.choices(CHANNELS, weights=[40,25,15,10,10])[0]))

    cur.executemany("INSERT INTO users VALUES (?, ?, ?, ?);", users)

    session_id = 1
    event_id = 1
    transaction_id = 1

    for user_id, signup_ts, *_ in users:
        signup_dt = datetime.fromisoformat(signup_ts)
        for _ in range(random.randint(1, 5)):
            s_ts = signup_dt + timedelta(days=random.randint(0, 20))
            cur.execute("INSERT INTO sessions VALUES (?, ?, ?, ?);",
                        (session_id, user_id, s_ts.isoformat(), random.choice(DEVICES)))

            cur.execute("INSERT INTO events VALUES (?, ?, ?, ?, ?);",
                        (event_id, user_id, s_ts.isoformat(), "visit", session_id))
            event_id += 1

            if random.random() < 0.7:
                cur.execute("INSERT INTO events VALUES (?, ?, ?, ?, ?);",
                            (event_id, user_id, s_ts.isoformat(), "signup", session_id))
                event_id += 1

                if random.random() < 0.4:
                    cur.execute("INSERT INTO events VALUES (?, ?, ?, ?, ?);",
                                (event_id, user_id, s_ts.isoformat(), "add_to_cart", session_id))
                    event_id += 1

                    if random.random() < 0.35:
                        revenue = random.choice([19.99, 29.99, 49.99, 79.99, 99.99])
                        cur.execute("INSERT INTO transactions VALUES (?, ?, ?, ?);",
                                    (transaction_id, user_id, s_ts.isoformat(), revenue))
                        transaction_id += 1

            session_id += 1

    conn.commit()
    conn.close()
    print("✅ funnel.db created successfully")

if __name__ == "__main__":
    main()
