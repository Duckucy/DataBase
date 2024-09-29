from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# 連接 MySQL 資料庫
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # 根據你的 MySQL 設定調整
        password="0922",  # 根據你的 MySQL 設定調整
        database="employeesystem"
    )

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = connect_db()
    cursor = conn.cursor()

    if request.method == 'POST':
        # 獲取表單中的資料
        name = request.form['name']
        age = int(request.form['age'])
        country = request.form['country']
        position = request.form['position']
        wage = float(request.form['wage'])

        # 插入資料到資料庫
        query = "INSERT INTO employees (name, age, country, position, wage) VALUES (%s, %s, %s, %s, %s)"
        values = (name, age, country, position, wage)
        
        try:
            cursor.execute(query, values)
            conn.commit()
        except mysql.connector.Error as err:
            return f"Error: {err}"

    # 檢索所有員工資料
    cursor.execute("SELECT id, name, age, country, position, wage FROM employees")
    employees = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('index.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True)