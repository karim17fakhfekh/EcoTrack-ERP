from flask import Flask, request, send_from_directory
import sqlite3

app = Flask(__name__)

# 1. Route to serve your index.html homepage
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/add_client', methods=['POST'])
def add_client():
    # 1. Extract form text along with the security role selection
    user_role = request.form.get('user_role')
    name = request.form.get('client_name')
    email = request.form.get('client_email')
    
    # 2. SECURITY GATE: Only allow 'HR' or 'Manager'
    allowed_roles = ['HR', 'Manager']
    if user_role not in allowed_roles:
        return f"""
        <div style="font-family: Arial, sans-serif; margin: 80px auto; max-width: 500px; text-align: center; padding: 30px; border: 2px solid #e74c3c; border-radius: 8px; background-color: #fdf2f2;">
            <h1 style="color: #c0392b; margin-top: 0;">🚫 Access Denied</h1>
            <p style="color: #7f8c8d; font-size: 16px;">Your simulated role (<strong>{user_role}</strong>) does not possess permission to modify the database.</p>
            <p style="font-size: 14px; color: #95a5a6;">Only <strong>HR</strong> and <strong>Manager</strong> credentials can execute insertions.</p>
            <br>
            <a href="javascript:history.back()" style="color: #3498db; text-decoration: none; font-weight: bold;">← Go Back & Change Role</a>
        </div>
        """, 403  # HTTP 403 Forbidden

    # 3. If check passes, interact with database
    conn = sqlite3.connect('company_erp.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Clients (client_name, contact_email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()
    
    # 4. Success Response
    return f"""
    <div style="font-family: Arial, sans-serif; margin: 80px auto; max-width: 500px; text-align: center; padding: 30px; border: 2px solid #2ecc71; border-radius: 8px; background-color: #f4fbf7;">
        <h1 style="color: #27ae60; margin-top: 0;">Success! 🎉</h1>
        <p style="font-size: 16px; color: #2c3e50;">Database Authorization Verified via <strong>{user_role}</strong> profile.</p>
        <p style="color: #7f8c8d;"><strong>{name}</strong> has been written to the client directory.</p>
        <br>
        <a href="javascript:history.back()" style="color: #3498db; text-decoration: none; font-weight: bold;">← Return to Dashboard</a>
    </div>
    """

if __name__ == '__main__':
    app.run(debug=True, port=8080)
