from menu_item import conn, cursor, MenuItem


class MenuManager:

    @classmethod
    def get_by_name(cls, name):
        query = "SELECT item_name, item_price FROM Menu_Items WHERE item_name = %s;"
        cursor.execute(query, (name,))
        result = cursor.fetchone()
        if result:
            return MenuItem(result[0], result[1])
        return None

    @classmethod
    def all(cls):
        query = "SELECT item_name, item_price FROM Menu_Items;"
        cursor.execute(query)
        results = cursor.fetchall()
        return [MenuItem(name, price) for name, price in results]
