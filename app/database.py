import sqlite3

DB_NAME = "fitbuddy.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            gender TEXT,
            fitness_goal TEXT,
            experience_level TEXT,
            dietary_preference TEXT,
            workout_plan TEXT,
            diet_plan TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_user_plan(user_data, workout_plan, diet_plan):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (name, age, gender, fitness_goal, experience_level, dietary_preference, workout_plan, diet_plan)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        user_data.name, user_data.age, user_data.gender,
        user_data.fitness_goal, user_data.experience_level,
        user_data.dietary_preference, workout_plan, diet_plan
    ))
    user_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return user_id

def get_user_plan(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    return row

def get_all_users():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, fitness_goal, experience_level FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_user_goal_and_plan(user_id, new_goal, new_workout, new_diet):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE users 
        SET fitness_goal = ?, workout_plan = ?, diet_plan = ? 
        WHERE id = ?
    ''', (new_goal, new_workout, new_diet, user_id))
    conn.commit()
    conn.close()