from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# 資料庫連接設定
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0922",
    database="game_analysis"
)

@app.route('/')
def index():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM players")
    players = cursor.fetchall()
    
    join_query = """
        SELECT p.username, gs.score, gs.play_time, gs.level_reached, gs.session_date 
        FROM players p
        JOIN game_sessions gs ON p.player_id = gs.player_id
    """
    cursor.execute(join_query)
    game_sessions = cursor.fetchall()
    
    return render_template('index.html', players=players, game_sessions=game_sessions)

@app.route('/create_player', methods=['POST'])
def create_player():
    data = request.json
    cursor = db.cursor()
    cursor.execute("INSERT INTO players (username, email, password) VALUES (%s, %s, %s)",
                   (data['username'], data['email'], data['password']))
    db.commit()
    return jsonify({'message': 'Player created successfully'})

@app.route('/update_player/<int:player_id>', methods=['PUT'])
def update_player(player_id):
    data = request.json
    cursor = db.cursor()
    cursor.execute("UPDATE players SET username=%s, email=%s, password=%s WHERE player_id=%s",
                   (data['username'], data['email'], data['password'], player_id))
    db.commit()
    return jsonify({'message': 'Player updated successfully'})

@app.route('/delete_player/<int:player_id>', methods=['DELETE'])
def delete_player(player_id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM players WHERE player_id=%s", (player_id,))
    db.commit()
    return jsonify({'message': 'Player deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
