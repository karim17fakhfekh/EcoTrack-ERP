# Read the template files and stitch together the complete app.py and index.html scripts cleanly.
import os

app_py_content = '''import os
import sqlite3
from functools import wraps
from flask import (
    Flask, render_template, request, redirect, 
    url_for, session, flash, jsonify
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Security: Best practice to read secret keys from environment variables
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
DATABASE = os.environ.get('DATABASE_PATH', 'company_erp.db')
HR_MASTER_KEY_HASH = generate_password_hash(os.environ.get('HR_MASTER_KEY', '19100576'))

# --- Database Helper ---
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db_connection() as conn:
        conn.execute(\'\'\'
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                sector TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        \'\'\')
        conn.commit()

# --- Decorators for Role-Based Access Control (RBAC) ---
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Please log in to access this page.", "warning")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def roles_required(*roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_role' not in session or session['user_role'] not in roles:
                flash("Unauthorized access: You do not have permission for this action.", "danger")
                return render_template('access_denied.html'), 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# --- Authentication Routes ---
@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_type = request.form.get('login_type')  # 'staff' or 'hr'
        
        if login_type == 'hr':
            master_code = request.form.get('hr_code', '')
            if check_password_hash(HR_MASTER_KEY_HASH, master_code):
                session['user_id'] = 'hr_admin'
                session['user_name'] = 'HR Master Admin'
                session['user_role'] = 'Admin'
                flash("Authenticated as HR Master Administrator.", "success")
                return redirect(url_for('dashboard'))
            else:
                flash("Handshake rejected. Master code invalid.", "danger")
                
        elif login_type == 'staff':
            username = request.form.get('name')
            role = request.form.get('role', 'Read')  # Assign default low-privilege role
            
            # In a full setup, look up user from DB and check password hash here
            session['user_id'] = username
            session['user_name'] = username
            session['user_role'] = role
            return redirect(url_for('dashboard'))

    return render_template('index.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("Successfully logged out.", "info")
    return redirect(url_for('login'))

# --- Main Application Routes ---
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template(
        'index.html', 
        user_name=session.get('user_name'),
        user_role=session.get('user_role')
    )

@app.route('/add_client', methods=['POST'])
@login_required
@roles_required('Admin', 'Write')
def add_client():
    name = request.form.get('name')
    email = request.form.get('email')
    sector = request.form.get('sector', 'Private')

    if not name or not email:
        flash("Name and email are required fields.", "warning")
        return redirect(url_for('dashboard'))

    try:
        with get_db_connection() as conn:
            conn.execute(
                "INSERT INTO clients (name, email, sector) VALUES (?, ?, ?)",
                (name, email, sector)
            )
            conn.commit()
        flash("Client registered successfully.", "success")
    except sqlite3.IntegrityError:
        flash("An account with this email already exists.", "danger")

    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
'''

with open("app.py", "w") as f:
    f.write(app_py_content)

print("app.py saved successfully.")
