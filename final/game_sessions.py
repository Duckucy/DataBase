from flask import Blueprint, render_template, jsonify
import mysql.connector
from mysql.connector import Error

# 創建 Blueprint
game_sessions_bp = Blueprint('game_sessions_bp', __name__, template_folder='templates')

# 資料庫配置
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '0922',
    'database': 'game_analysis'
}

@game_sessions_bp.route('/game_sessions', methods=['GET'])
def get_game_sessions():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM game_sessions"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        return render_template('records.html', game_sessions=results)
    except Error as e:
        return jsonify({'error': str(e)}), 500
