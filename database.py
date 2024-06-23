import sqlite3
import os

def init_db():
    conn = sqlite3.connect('settings.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    ''')
    if not load_setting('current_language'):
        c.execute('INSERT INTO settings (key, value) VALUES (?, ?)', ('current_language', 'English'))
    if not load_setting('save_folder'):
        c.execute('INSERT INTO settings (key, value) VALUES (?, ?)',
                  ('save_folder', os.path.join(os.getcwd(), 'screenshots')))
    conn.commit()
    conn.close()


def save_setting(key, value):
    conn = sqlite3.connect('settings.db')
    c = conn.cursor()
    c.execute('''
        INSERT OR REPLACE INTO settings (key, value)
        VALUES (?, ?)
    ''', (key, value))
    conn.commit()
    conn.close()


def load_setting(key, default=None):
    conn = sqlite3.connect('settings.db')
    c = conn.cursor()
    c.execute('''
        SELECT value FROM settings WHERE key = ?
    ''', (key,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else default