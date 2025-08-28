#!/usr/bin/env bash

# Create database and run SQL
sqlite3 students.db - <<'SQL'
DROP TABLE IF EXISTS students;
CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, grade TEXT);
INSERT INTO students (name, age, grade) VALUES
('Alice',20,'A'),
('Bob',21,'B'),
('Charlie',22,'A'),
('Diana',20,'C');

SELECT grade, COUNT(*) FROM students GROUP BY grade;
SQL

# Run same query in Python via pandas
python - <<'PY'
import sqlite3, pandas as pd
conn = sqlite3.connect("students.db")
df = pd.read_sql_query("SELECT grade, COUNT(*) FROM students GROUP BY grade", conn)
print(df)
conn.close()
PY
