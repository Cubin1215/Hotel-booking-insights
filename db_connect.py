import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Debug: Print environment variables (excluding password for security)
print("Environment variables loaded:")
print(f"DB_NAME: {os.getenv('DB_NAME')}")
print(f"DB_USER: {os.getenv('DB_USER')}")
print(f"DB_HOST: {os.getenv('DB_HOST')}")
print(f"DB_PORT: {os.getenv('DB_PORT')}")
print(f"DB_PASSWORD exists: {'Yes' if os.getenv('DB_PASSWORD') else 'No'}")

try:
    connection = psycopg2.connect(
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )

    cursor = connection.cursor()
    print("\nConnected to the database!")

    # Optional: Check existing tables
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
    tables = cursor.fetchall()
    print("Tables:", tables)

    cursor.close()
    connection.close()

except Exception as error:
    print("\nError while connecting to PostgreSQL:", error)
    print("\nConnection details used:")
    print(f"Database: {os.getenv('DB_NAME')}")
    print(f"User: {os.getenv('DB_USER')}")
    print(f"Host: {os.getenv('DB_HOST')}")
    print(f"Port: {os.getenv('DB_PORT')}")
    print("Password: [hidden]")
