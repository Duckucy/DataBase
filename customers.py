from flask import Blueprint, request, redirect, url_for
import mysql.connector

customers_bp = Blueprint('customers_bp', __name__, url_prefix='/customers')

db_config = {
    'user': 'root',
    'password': '0922',
    'host': 'localhost',
    'database': 'employeesystem'
}

@customers_bp.route('/add', methods=['POST'])
def add_customer():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO customers (first_name, last_name) VALUES (%s, %s)", (first_name, last_name))
    conn.commit()
    
    cursor.close()
    conn.close()
    
    return redirect(url_for('index'))


