from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
# from flask_app.models import # other model file name here

class Order:
    def __init__(self, data):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.cookie = data['cookie']
        self.num_boxes = data['num_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# CREATE
    @classmethod
    def place_order(cls, data):
        query = "INSERT INTO cookie_orders (customer_name, cookie, num_boxes, created_at, updated_at) VALUES (%(customer_name)s, %(cookie)s, %(num_boxes)s, NOW(), NOW());"
        return connectToMySQL('cookie_orders').query_db(query, data)

# READ
    @classmethod
    def get_orders(cls):
        query = "SELECT * FROM cookie_orders;"
        results = connectToMySQL('cookie_orders').query_db(query)
        orders = []
        for order in results:
            orders.append(cls(order))
        return orders
    
    @classmethod
    def get_order_by_id(cls, data):
        query = "SELECT * FROM cookie_orders WHERE id = %(id)s;"
        result = connectToMySQL('cookie_orders').query_db(query, data)
        return cls(result[0])

# UPDATE
    @classmethod
    def update_order(cls, data):
        query = "UPDATE cookie_orders SET customer_name = %(customer_name)s, cookie = %(cookie)s, num_boxes = %(num_boxes)s WHERE id = %(id)s;"
        return connectToMySQL('cookie_orders').query_db(query, data)


# DELETE

# VALIDATION
    @staticmethod
    def validate(order):
        is_valid = True
        if len (order['customer_name']) < 2:
            flash("You must provide a name of at least two characters.")
            is_valid = False
        if len (order['cookie']) < 2:
            flash("Only cookies of two characters or more are valid. Please be more descriptive.")
            is_valid = False
        if int(order['num_boxes']) < 0:
            flash("You cannot select a negative number for your order...")
            is_valid = False
        return is_valid