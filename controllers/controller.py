from app import app
from flask import render_template
from models.orders_list import orders

@app.route('/orders')
def index():
    return render_template("index.html", title = "home", orders = orders)

@app.route('/orders/<index>')
def show_order(index):
    order = orders[int(index)]
    return render_template("order.html", order = order)


