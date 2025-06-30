CREATE TABLE users (
     user_id SERIAL PRIMARY KEY,
     username VARCHAR(50) NOT NULL UNIQUE,
     email VARCHAR(100) NOT NULL UNIQUE,
     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
 );

 CREATE TABLE product_orders (
     order_id SERIAL PRIMARY KEY,
     user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
     order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
     status VARCHAR(20) DEFAULT 'pending'
 );

 CREATE TABLE items (
     item_id SERIAL PRIMARY KEY,
     order_id INTEGER REFERENCES product_orders(order_id) ON DELETE CASCADE,
     product_name VARCHAR(100) NOT NULL,
     price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
     quantity INTEGER NOT NULL CHECK (quantity > 0)
 );
 CREATE OR REPLACE FUNCTION get_order_total(order_id_param INTEGER) RETURNS DECIMAL(10, 2) AS $$
 DECLARE total DECIMAL(10, 2);
 BEGIN
 SELECT SUM(price * quantity) INTO total
 FROM items
 WHERE order_id = order_id_param;
 RETURN COALESCE(total, 0);
 END;