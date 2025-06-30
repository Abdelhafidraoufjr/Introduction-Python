import psycopg2

conn = psycopg2.connect(
    dbname="database_day4",
    user="postgres",
    password="root",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()


class MenuItem:
    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price

    def save(self):
        query = "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s);"
        cursor.execute(query, (self.item_name, self.item_price))
        conn.commit()

    def delete(self):
        query = "DELETE FROM Menu_Items WHERE item_name = %s;"
        cursor.execute(query, (self.item_name,))
        conn.commit()

    def update(self, new_name, new_price):
        query = "UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s;"
        cursor.execute(query, (new_name, new_price, self.item_name))
        conn.commit()
        self.item_name = new_name
        self.item_price = new_price
