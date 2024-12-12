from flask import Blueprint, render_template, request, jsonify
import mysql.connector
from mysql.connector import Error

# 創建 Blueprint
register_bp = Blueprint('register_bp', __name__, template_folder='templates')

# 資料庫配置
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '0922',
    'database': 'game_analysis'
}

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 從表單或 JSON 獲取資料
        username = request.form.get('username') or request.json.get('username')
        email = request.form.get('email') or request.json.get('email')
        password = request.form.get('password') or request.json.get('password')

        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            query = "INSERT INTO players (username, email, password) VALUES (%s, %s, %s)"
            cursor.execute(query, (username, email, password))
            connection.commit()
            cursor.close()
            connection.close()
            return jsonify({'message': 'Player registered successfully'}), 201
        except Error as e:
            return jsonify({'error': str(e)}), 500
    return render_template('register.html')
