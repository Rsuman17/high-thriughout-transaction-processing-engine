import psycopg2
def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="transaction_engine",
        user="postgres",
        password="2410",
        port="5432"
    )