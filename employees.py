from flask import Blueprint, request, redirect, url_for
import mysql.connector

employees_bp = Blueprint('employees_bp', __name__, url_prefix='/employees')

db_config = {
    'user': 'root',
    'password': '0922',
    'host': 'localhost',
    'database': 'employeesystem'
}

@employees_bp.route('/add', methods=['POST'])
def add_employee():
    name = request.form['name']
    age = request.form['age']
    country = request.form['country']
    position = request.form['position']
    wage = request.form['wage']

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO employees (name, age, country, position, wage)
        VALUES (%s, %s, %s, %s, %s)
    """, (name, age, country, position, wage))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('join_bp.show_transactions'))

@employees_bp.route('/update/<int:employee_id>', methods=['POST'])
def update_employee(employee_id):
    name = request.form['name']
    age = request.form['age']
    country = request.form['country']
    position = request.form['position']
    wage = request.form['wage']

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE employees SET name=%s, age=%s, country=%s, position=%s, wage=%s
        WHERE id=%s
    """, (name, age, country, position, wage, employee_id))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('join_bp.show_transactions'))

@employees_bp.route('/delete/<int:employee_id>', methods=['POST'])
def delete_employee(employee_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE id=%s", (employee_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('join_bp.show_transactions'))
