from flask import Blueprint, request, redirect, url_for
import mysql.connector

transactions_bp = Blueprint('transactions_bp', __name__, url_prefix='/transactions')

db_config = {
    'user': 'root',
    'password': '0922',
    'host': 'localhost',
    'database': 'employeesystem'
}

@transactions_bp.route('/add', methods=['POST'])
def add_transaction():
    amount = request.form['amount']
    customer_id = request.form['customer_id']

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (amount, customer_id) VALUES (%s, %s)", (amount, customer_id))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('join_bp.show_transactions'))

