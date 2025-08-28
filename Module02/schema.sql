-- create table
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    grade TEXT
);

-- insert sample rows
INSERT INTO students (name, age, grade) VALUES
('Alice', 20, 'A'),
('Bob', 21, 'B'),
('Charlie', 22, 'A'),
('Diana', 20, 'C');