import sqlite3
import pandas as pd

def import_csv_to_sql():
    # Connect to (or create) SQLite database file
    conn = sqlite3.connect('amex_churn.db')

    # Load your CSV file
    df = pd.read_csv('unzipped/amex_data.csv')

    # Import data into SQL table named 'customer_data'
    df.to_sql('customer_data', conn, if_exists='replace', index=False)

    print("Data imported into SQLite database successfully!")

    # Close connection
    conn.close()

if __name__ == "__main__":
    import_csv_to_sql()
