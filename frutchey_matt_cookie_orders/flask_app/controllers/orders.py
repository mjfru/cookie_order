from flask_app import app
from flask import render_template, session, redirect, request, flash

from flask_app.models.order import Order

# App Routes Go Below:

# Home Page
@app.route("/")
@app.route("/cookies")
def all_orders():
    orders = Order.get_orders()
    return render_template("/index.html", orders = orders)

@app.route("/order_page")
def order_page():
    return render_template("/new_order.html")

# Create 
@app.route("/order/place", methods = ["POST", "GET"])
def place_new_order():
    if request.method == "POST":
        if not Order.validate(request.form):
            return render_template("new_order.html")
    data = {
        "customer_name": request.form["customer_name"],
        "cookie": request.form["cookie"],
        "num_boxes": request.form["num_boxes"]
    }
    Order.place_order(data)
    return redirect("/cookies")

# Read
@app.route("/cookies/edit/<int:id>")
def edit_page(id):
    order = Order.get_order_by_id({'id': id})
    return render_template("edit_order.html", order = order)

# Update
@app.route("/update/order", methods = ["POST"])
def change_order():
    order_id = request.form['id']
    if not Order.validate(request.form):
        return redirect(f"/cookies/edit/{order_id}")
    data = {
        "id": request.form['id'],
        "customer_name": request.form["customer_name"],
        "cookie": request.form["cookie"],
        "num_boxes": request.form["num_boxes"]
    }
    # print(data)
    Order.update_order(data)
    return redirect("/cookies")

# Delete