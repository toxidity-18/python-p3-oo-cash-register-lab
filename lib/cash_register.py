#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = (None, 0, 0)  # (item_name, item_price, item_quantity)
    
    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction = (title, price, quantity)
    
    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")
    
    def void_last_transaction(self):
        item_name, item_price, item_quantity = self.last_transaction
        if item_name:
            self.total -= item_price * item_quantity
            for _ in range(item_quantity):
                self.items.remove(item_name)
            self.last_transaction = (None, 0, 0)
  