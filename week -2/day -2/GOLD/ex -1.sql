SELECT rating,
    COUNT(*) AS number_of_films
FROM film
GROUP BY rating
ORDER BY number_of_films DESC;
SELECT title,
    rating,
    length,
    rental_rate
FROM film
WHERE rating IN ('G', 'PG-13')
    AND length < 120
    AND rental_rate < 3.00
ORDER BY title ASC;
UPDATE customer
SET first_name = 'YourFirstName',
    last_name = 'YourLastName',
    email = 'your.email@example.com'
WHERE customer_id = 1;

SELECT *
FROM customer
WHERE customer_id = 1;
SELECT address_id
FROM customer
WHERE customer_id = 1;
UPDATE address
SET address = '123 Your Street',
    address2 = 'Apt 4B',
    district = 'Your District',
    postal_code = '12345',
    phone = '555-123-4567'
WHERE address_id = (
        SELECT address_id
        FROM customer
        WHERE customer_id = 1
    );
SELECT a.*
FROM address a
    JOIN customer c ON a.address_id = c.address_id
WHERE c.customer_id = 1;