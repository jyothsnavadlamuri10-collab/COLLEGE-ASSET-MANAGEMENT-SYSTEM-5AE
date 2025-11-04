from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# ---------------------- DATABASE ----------------------
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS assets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    category TEXT,
                    location TEXT,
                    purchase_date TEXT,
                    condition TEXT
                )''')
    conn.commit()
    conn.close()

init_db()

# ---------------------- ROUTES ----------------------

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_asset():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        location = request.form['location']
        purchase_date = request.form['purchase_date']
        condition = request.form['condition']

        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO assets (name, category, location, purchase_date, condition) VALUES (?, ?, ?, ?, ?)",
                  (name, category, location, purchase_date, condition))
        conn.commit()
        conn.close()

        return redirect(url_for('view_assets'))

    return render_template('add_asset.html')

@app.route('/view')
def view_assets():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM assets")
    data = c.fetchall()
    conn.close()
    return render_template('view_assets.html', assets=data)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_asset(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM assets WHERE id=?", (id,))
    asset = c.fetchone()
    conn.close()

    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        location = request.form['location']
        purchase_date = request.form['purchase_date']
        condition = request.form['condition']

        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('''UPDATE assets SET name=?, category=?, location=?, purchase_date=?, condition=? WHERE id=?''',
                  (name, category, location, purchase_date, condition, id))
        conn.commit()
        conn.close()
        return redirect(url_for('view_assets'))

    return render_template('edit_asset.html', asset=asset)

@app.route('/delete/<int:id>')
def delete_asset(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("DELETE FROM assets WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('view_assets'))

if __name__ == '__main__':
    app.run(debug=True)
