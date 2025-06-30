# auth_db.py
import psycopg2
import bcrypt

conn = psycopg2.connect(
    dbname="database_day4",  
    user="postgres",
    password="root",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

def register_user(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed))
        conn.commit()
        print("✅ Utilisateur enregistré avec succès.")
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        print("❌ Ce nom d'utilisateur est déjà pris.")

def login_user(username, password):
    cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    if result and bcrypt.checkpw(password.encode(), result[0].encode()):
        return True
    return False


