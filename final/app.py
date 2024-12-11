from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
CORS(app)

# 資料庫配置
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'game_analysis'
}

# 玩家註冊
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    email = data['email']
    password = data['password']

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

# 玩家遊戲紀錄
@app.route('/game_sessions', methods=['GET'])
def get_game_sessions():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        query = "SELECT * FROM game_sessions"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        connection.close()

        # 格式化資料輸出
        columns = ['session_id', 'player_id', 'score', 'play_time', 'level_reached', 'session_date']
        game_sessions = [dict(zip(columns, row)) for row in results]
        return jsonify(game_sessions), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500

# 啟動伺服器
if __name__ == '__main__':
    app.run(debug=True, port=5000)
