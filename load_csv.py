import pandas as pd
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Load the CSV
df = pd.read_csv("hotel_bookings.csv")

# Clean NaNs (optional)
df = df.fillna(value='')

# Connect to PostgreSQL
conn = psycopg2.connect(
    database=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT')
)

cur = conn.cursor()

# Create table (match exact structure of hotel_bookings.csv)
cur.execute("""
    DROP TABLE IF EXISTS hotel_bookings;
    CREATE TABLE hotel_bookings (
        hotel TEXT,
        is_canceled INTEGER,
        lead_time INTEGER,
        arrival_date_year INTEGER,
        arrival_date_month TEXT,
        arrival_date_week_number INTEGER,
        arrival_date_day_of_month INTEGER,
        stays_in_weekend_nights INTEGER,
        stays_in_week_nights INTEGER,
        adults INTEGER,
        children TEXT,
        babies INTEGER,
        meal TEXT,
        country TEXT,
        market_segment TEXT,
        distribution_channel TEXT,
        is_repeated_guest INTEGER,
        previous_cancellations INTEGER,
        previous_bookings_not_canceled INTEGER,
        reserved_room_type TEXT,
        assigned_room_type TEXT,
        booking_changes INTEGER,
        deposit_type TEXT,
        agent TEXT,
        company TEXT,
        days_in_waiting_list INTEGER,
        customer_type TEXT,
        adr NUMERIC,
        required_car_parking_spaces INTEGER,
        total_of_special_requests INTEGER,
        reservation_status TEXT,
        reservation_status_date DATE
    );
""")
conn.commit()

# Insert data
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO hotel_bookings VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        )
    """, tuple(row))

conn.commit()
cur.close()
conn.close()

print("✅ hotel_bookings.csv successfully loaded into PostgreSQL!")
