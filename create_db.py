import sqlite3

# Створення або підключення до бази даних
conn = sqlite3.connect('hw_06_db.db')
cursor = conn.cursor()

# Таблиця студентів
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    fullname TEXT NOT NULL,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups (id)
);
''')

# Таблиця груп
cursor.execute('''
CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
''')

# Таблиця викладачів
cursor.execute('''
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY,
    fullname TEXT NOT NULL
);
''')

# Таблиця предметів
cursor.execute('''
CREATE TABLE IF NOT EXISTS disciplines (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers (id)
);
''')

# Таблиця оцінок
cursor.execute('''
CREATE TABLE IF NOT EXISTS grades (
  id INTEGER PRIMARY KEY,
  student_id INTEGER NOT NULL,  
  disciplines_id INTEGER NOT NULL, 
  grade INTEGER NOT NULL,       
  date_received DATE,
  FOREIGN KEY (student_id) REFERENCES students (id),
  FOREIGN KEY (disciplines_id) REFERENCES disciplines (id)
);
''')

# Збереження змін та закриття з'єднання
conn.commit()
conn.close()