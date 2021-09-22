from app import app
from flask import render_template
from models.orders_list import orders

@app.route('/orders')
def index():
    return render_template("index.html", title = "home", orders = orders)

@app.route('/orders/<index>[0]')
def orders():
    return render_template("orders.html", title = "order", orders = orders[0])


