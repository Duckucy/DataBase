from flask import Blueprint, render_template, redirect, url_for
import mysql.connector

join_bp = Blueprint('join_bp', __name__)

db_config = {
    'user': 'root',
    'password': '0922',
    'host': 'localhost',
    'database': 'employeesystem'
}

@join_bp.route('/transactions')
def show_transactions():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    
    # 查詢員工
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    
    # 查詢顧客
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    
    # 查詢 JOIN 結果
    join_query = """
    SELECT customers.customer_id, customers.first_name, customers.last_name, 
           transactions.transaction_id, transactions.amount
    FROM customers
    JOIN transactions ON customers.customer_id = transactions.customer_id
    """
    cursor.execute(join_query)
    transactions = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return render_template('index.html', employees=employees, customers=customers, transactions=transactions)
