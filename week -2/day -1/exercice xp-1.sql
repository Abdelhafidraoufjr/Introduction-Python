CREATE TABLE IF NOT EXISTS public.items (
    item_id     SERIAL PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    price       NUMERIC(10,2) NOT NULL
);

INSERT INTO public.items (name, price) VALUES
('Petit bureau', 100),
('Grand bureau', 300),
('Ventilateur', 80);

CREATE TABLE IF NOT EXISTS public.customers (
    customer_id SERIAL PRIMARY KEY,
    first_name  VARCHAR(50) NOT NULL,
    last_name   VARCHAR(50) NOT NULL
);

INSERT INTO public.customers (first_name, last_name) VALUES
('Greg', 'Jones'),
('Sandra', 'Jones'),
('Scott', 'Scott'),
('Trevor', 'Vert'),
('Mélanie', 'Johnson');

SELECT * FROM public.items;

SELECT * FROM public.items
WHERE price > 80;

SELECT * FROM public.items
WHERE price <= 300;

SELECT * FROM public.customers
WHERE last_name = 'Smith';

SELECT * FROM public.customers
WHERE last_name = 'Jones';

SELECT * FROM public.customers
WHERE first_name <> 'Scott';
