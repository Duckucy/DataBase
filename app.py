from flask import Flask, render_template, redirect, url_for
from join import join_bp
from employees import employees_bp
from customers import customers_bp
from transactions import transactions_bp

app = Flask(__name__)

app.register_blueprint(join_bp)
app.register_blueprint(employees_bp)
app.register_blueprint(customers_bp)
app.register_blueprint(transactions_bp)

@app.route('/')
def index():
    return redirect(url_for('join_bp.show_transactions'))

if __name__ == '__main__':
    app.run(debug=True)
