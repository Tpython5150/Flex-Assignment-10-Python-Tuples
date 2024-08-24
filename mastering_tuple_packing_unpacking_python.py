'''

3. Mastering tuple Packing and Umpacking in Python

Objective: The goal of the assignment is to deepen your understanding of tuple packing and unpacking in Python,

Task 1: Customer Order Processing Refine you skills in tuple unpacking by managing customer orders.
 
Problem Statement:
You are given a list of tuples, each representing a customer's order. Each tuple contains the customer's name, the product orderd, and the quantity. Your task to to unpack each tuple and print the order details in a user friendly format.

Sameple Order Data:

orders = [
  ("Alice", "Laptop", 1),
  ("Bob", "Camera", 2 )
]

- Write a function to iterate over the list of orders. 
- Unpack each tuple in the list and format the details for display.

'''

orders = [
  ("Alice", "Laptop", 1),
  ("Bob", "Camera", 2 )
]

def processed_orders(orders):
  for order in orders:
    customer_name, product, quantity = order
    print(f"Customer: {customer_name}, Product: {product}, Quantity: {quantity}")
    
processed_orders(orders)    