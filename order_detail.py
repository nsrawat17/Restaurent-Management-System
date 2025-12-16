orders =[]

def add_order(item, price, quantity):
    orders.append((item ,price, quantity))

def get_orders():
    return orders