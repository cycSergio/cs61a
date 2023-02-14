.read lab12.sql

-- Q5
CREATE TABLE greatstudents AS
  SELECT a.date, a.color, a.pet, a.number, b.number FROM students as a, fa17students as b
  WHERE a.date = b.date and a.color = b.color and a.pet = b.pet;

-- Q6
CREATE TABLE sevens AS
  SELECT b.seven from students as b, checkboxes as a WHERE b.number = 7 AND a.'7' = 'True' AND b.time = a.time;

-- Q7
CREATE TABLE fa17favnum AS
  SELECT max(number), count(*) FROM fa17students GROUP BY number ORDER BY count(*) DESC LIMIT 1;


CREATE TABLE fa17favpets AS
  SELECT pet, count(*) FROM fa17students GROUP BY pet ORDER BY count(*) DESC, pet LIMIT 10;


CREATE TABLE sp18favpets AS
  SELECT pet, count(*) FROM students GROUP BY pet ORDER BY count(*) DESC, pet LIMIT 10;


CREATE TABLE sp18dog AS
  SELECT pet, count(*) FROM students WHERE pet = 'dog';


CREATE TABLE sp18alldogs AS
  SELECT pet, count(*) FROM students WHERE pet LIKE '%dog%';


CREATE TABLE obedienceimages AS
  SELECT seven, denero, count(*) FROM students WHERE seven = '7' GROUP BY denero;

-- Q8
CREATE TABLE smallest_int_count AS
  SELECT smallest, count(*) FROM students GROUP BY smallest ORDER BY smallest;
