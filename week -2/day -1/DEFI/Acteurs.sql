CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
)

INSERT INTO actors (first_name, last_name, age, number_oscars) VALUES
('Meryl',      'Streep',      '1949-06-22', 3),  -- 3 Oscars
('Daniel',     'Day-Lewis',   '1957-04-29', 3),  -- 3 Oscars
('Denzel',     'Washington',  '1954-12-28', 2),  -- 2 Oscars
('Frances',    'McDormand',   '1957-06-23', 4),  -- 4 Oscars (dont 1 productrice)
('Leonardo',   'DiCaprio',    '1974-11-11', 1),  -- 1 Oscar
('Cate',       'Blanchett',   '1969-05-14', 2),  -- 2 Oscars
('Mahershala', 'Ali',         '1974-02-16', 2),  -- 2 Oscars
('Tom',        'Hanks',       '1956-07-09', 2),  -- 2 Oscars
('Natalie',    'Portman',     '1981-06-09', 1),  -- 1 Oscar
('Joaquin',    'Phoenix',     '1974-10-28', 1);  -- 1 Oscar

SELECT COUNT(*) FROM actors

INSERT INTO actors (first_name, last_name, age, number_oscars) VALUES
('',      '',      '', ), ------> Erreur deja les valeur sont Not NULL 