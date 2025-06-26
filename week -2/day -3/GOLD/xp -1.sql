SELECT *
FROM rental
WHERE return_date IS NULL;

SELECT c.customer_id, c.first_name, c.last_name, COUNT(*) AS unreturned_rentals
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
WHERE r.return_date IS NULL
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY unreturned_rentals DESC;

SELECT f.title
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE a.first_name = 'Joe' AND a.last_name = 'Swank'
  AND c.name = 'Action';

CREATE VIEW film_actor_category_view AS
SELECT f.film_id, f.title, a.first_name, a.last_name, c.name AS category
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id;

SELECT title
FROM film_actor_category_view
WHERE first_name = 'Joe' AND last_name = 'Swank'
  AND category = 'Action';
