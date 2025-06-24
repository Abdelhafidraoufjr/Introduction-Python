CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
)

INSERT INTO actors (first_name, last_name, age, number_oscars) VALUES
('Meryl',      'Streep',      '1949-06-22', 3),  
('Daniel',     'Day-Lewis',   '1957-04-29', 3), 
('Denzel',     'Washington',  '1954-12-28', 2), 
('Frances',    'McDormand',   '1957-06-23', 4), 
('Leonardo',   'DiCaprio',    '1974-11-11', 1),  
('Cate',       'Blanchett',   '1969-05-14', 2),  
('Mahershala', 'Ali',         '1974-02-16', 2),  
('Tom',        'Hanks',       '1956-07-09', 2),  
('Natalie',    'Portman',     '1981-06-09', 1), 
('Joaquin',    'Phoenix',     '1974-10-28', 1);  

SELECT COUNT(*) FROM actors

INSERT INTO actors (first_name, last_name, age, number_oscars) VALUES
('',      '',      '', ), ------> Erreur deja les valeur sont Not NULL 