from flask import Flask, redirect, url_for
from register import register_bp
from game_sessions import game_sessions_bp

app = Flask(__name__)

# 註冊模組 Blueprint
app.register_blueprint(register_bp)
app.register_blueprint(game_sessions_bp)

@app.route('/')
def index():
    # 預設導向到遊戲紀錄頁面
    return redirect(url_for('game_sessions_bp.get_game_sessions'))

if __name__ == '__main__':
    app.run(debug=True)
