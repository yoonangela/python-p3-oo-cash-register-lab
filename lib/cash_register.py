#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
      self.discount=discount
      self.total=0
      self.items=[]
      self.last_transaction=[]
    
    def add_item(self, title, price, quantity=1):
      self.total=self.total+price*quantity
      i=0
      while i<quantity:
        self.items.append(title)
        i=i+1
      self.last_transaction.append({"title":title, "price":price, "quantity":quantity})
    
    def apply_discount(self):  
      if self.discount==0:
        print("There is no discount to apply.")
      else:
        self.total=self.total*(100-self.discount)*0.01
        print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
      self.total=self.total-self.last_transaction[-1]["price"]*self.last_transaction[-1]["quantity"]
      if self.last_transaction==[]:
        return self.total


