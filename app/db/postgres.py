import os
import psycopg2

def get_conn():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "localhost"),
        dbname=os.getenv("POSTGRES_DB", "appdb"),
        user=os.getenv("POSTGRES_USER", "appuser"),
        password=os.getenv("POSTGRES_PASSWORD", "apppass"),
        port=5432 if os.getenv("POSTGRES_HOST") != "pgbouncer" else 6432,
    )