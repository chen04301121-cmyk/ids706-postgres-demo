import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()


def main():
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        sslmode=os.getenv("DB_SSLMODE", "prefer"),
    )

    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT name, rating
                FROM restaurants
                ORDER BY rating DESC, name ASC
                LIMIT 3;
            """)

            print("top three restaurant with high ranking:")
            for name, rating in cur.fetchall():
                print(f"{name}: {rating}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()