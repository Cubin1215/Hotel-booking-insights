import psycopg2
from tabulate import tabulate
import pandas as pd
import sys
import re
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def get_query_number():
    if len(sys.argv) > 1:
        try:
            return int(sys.argv[1])
        except ValueError:
            print("Please provide a valid query number")
            sys.exit(1)
    else:
        print("Please provide a query number as argument")
        print("Example: py run_query.py 1")
        sys.exit(1)

def extract_queries(sql_content):
    # Split the content by section markers (looking for Question X: pattern)
    sections = re.split(r'-- =+.*?Question \d+:.*?=+\s*', sql_content)
    queries = []
    
    for section in sections:
        if section.strip():
            # Find all SQL statements in the section
            sql_statements = re.findall(r'SELECT.*?;', section, re.DOTALL | re.IGNORECASE)
            if sql_statements:  # Only add if we found a SELECT statement
                queries.extend(sql_statements)
    
    return queries

# Use environment variables for database connection
connection = psycopg2.connect(
    database=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT')
)

cursor = connection.cursor()

# Read the SQL file
with open('exploration.sql', 'r') as sql_file:
    sql_content = sql_file.read()
    queries = extract_queries(sql_content)

# Get the query number from command line
query_number = get_query_number()

# Check if the query number is valid
if query_number < 1 or query_number > len(queries):
    print(f"Invalid query number. Please choose between 1 and {len(queries)}")
    print("\nAvailable queries:")
    for i, query in enumerate(queries, 1):
        # Extract the query description from the SQL file
        query_desc = ""
        with open('exploration.sql', 'r') as f:
            content = f.read()
            # Find the section header for this query
            matches = re.findall(r'-- =+.*?Question ' + str(i) + r':(.*?)=+\s*', content, re.DOTALL)
            if matches:
                query_desc = matches[0].strip()
        
        print(f"\nQuery {i}: {query_desc}")
        print("-" * 80)
        print(query.strip())
    sys.exit(1)

# Execute the selected query
selected_query = queries[query_number - 1]
print(f"\nExecuting Query {query_number}:")
print("=" * 80)
print(selected_query.strip())
print("=" * 80)

try:
    cursor.execute(selected_query)
    
    # Get column names
    column_names = [desc[0] for desc in cursor.description]
    
    # Fetch results
    results = cursor.fetchall()
    
    # Convert to pandas DataFrame for better formatting
    df = pd.DataFrame(results, columns=column_names)
    
    # Print results in a nice tabular format
    print("\nQuery Results:")
    print("=" * 80)
    print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
    print("=" * 80)
    print(f"\nTotal rows: {len(df)}")

except Exception as e:
    print(f"Error executing query: {e}")

cursor.close()
connection.close() 