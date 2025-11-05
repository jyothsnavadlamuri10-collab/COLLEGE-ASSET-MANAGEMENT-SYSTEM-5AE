A simple Flask-based College Asset Management System (demo project) with features:

List all college assets

Add new assets (name, category, quantity, etc.)

Update or delete existing assets (simple POST actions)

Data stored in assets_data.json (flat-file for demo)

🔧 Run locally

Create virtualenv:

python -m venv venv && source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate                             # (Windows)


Install requirements:

pip install -r requirements.txt


Run:

python app.py


Open:
http://127.0.0.1:5000

🗒️ Notes

This is a simple educational demo project.

For production, use a proper database (like SQLite/MySQL), add authentication for admin/staff users, and improve UI/UX.
