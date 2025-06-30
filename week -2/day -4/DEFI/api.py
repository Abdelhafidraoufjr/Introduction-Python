import psycopg2
import requests
import random

conn = psycopg2.connect(
    dbname="database_day4",  
    user="postgres",
    password="root",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

url = "https://restcountries.com/v3.1/all"
response = requests.get(url)
countries = response.json()

random_countries = random.sample(countries, 10)

for country in random_countries:
    try:
        name = country.get('name', {}).get('common', 'N/A')
        capital = country.get('capital', ['N/A'])[0]
        flag = country.get('flags', {}).get('png', 'N/A')
        subregion = country.get('subregion', 'N/A')
        population = country.get('population', 0)

        cursor.execute("""
            INSERT INTO countries (name, capital, flag, subregion, population)
            VALUES (%s, %s, %s, %s, %s)
        """, (name, capital, flag, subregion, population))
    except Exception as e:
        print(f"Erreur pour {name}: {e}")
        conn.rollback()
    else:
        conn.commit()

print("✅ 10 pays insérés dans la base de données avec succès.")
cursor.close()
conn.close()
