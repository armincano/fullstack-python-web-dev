"""
Challenge: Shopping Cart Implementation
Instructions
1. Create a Base Class Product:
1.1 It should have private attributes __name, __price, and __stock_quantity.
1.2 It should have properties name, price, and stock_quantity to get and set the values of these attributes.
1.3 The price property should ensure that the price is not negative.
1.4 The stock_quantity property should ensure that the stock quantity is not negative.

2. Create a Class VirtualCart:
2.1 It should have a private attribute __products which is a dictionary where the key is the product name and the value is an instance of Product.
2.2 It should have a method add_product(product, quantity) that adds a product to the cart.
    - If the requested quantity exceeds the stock quantity, it should raise a custom exception InsufficientStockError.
2.3 It should have a method remove_product(product_name) that removes a product from the cart.
2.4 It should have a method calculate_total() that calculates and returns the total cost of the products in the cart.
2.5 It should have a method show_cart() that prints the products in the cart with their quantities and prices.

3. Testing and Verification:
3.1 Create several products, add them to the cart, handle exceptions if you try to add more than what is in stock, calculate the total of the cart, and remove a product."""
from product import Product
from db import db
from utils.customexceptions import StockInsufficientError, ProductNotFound
from utils.integertolocalechile import format_currency

class VirtualCart:
    def __init__(self, products={}):
        self.__products = products
        
    @property
    def products(self):
        return self.__products

    def add_product(self, raw_product_name: str, quantity: int):      
        product_name = raw_product_name.lower()
        try:
            if quantity <= 0:
                raise ValueError
            if product_name not in db:
                raise ProductNotFound
            if db[product_name].stock < quantity:
                raise StockInsufficientError
            
            if product_name in self.__products:
                self.__products[product_name].stock += quantity
            else:
                product_to_add = {product_name: Product(db[product_name].name, db[product_name].price, quantity)}
                self.__products.update(product_to_add)
        except ValueError:
            print(f"Invalid quantity '{quantity}' for '{product_name}'.")
        except ProductNotFound as e:
            print(f"'{product_name}' {e}")
        except StockInsufficientError as e:
            print(f"{e} '{product_name}'.")
    
    def delete_product(self, raw_product_name: str):
        product_name = raw_product_name.lower()
        if product_name in self.__products:
            self.__products.pop(product_name)
            print("🗑 Product was deleted from your cart.")
        else:
            print("There is no product to delete")
    
    def calculate_total(self):
        total = 0
        for product in self.__products.values():
            total += product.price * product.stock
        return f"The total of your cart is {format_currency(total)}"
    
    def show_cart(self):
        divider_1 = ">>>--->>----------------------------------------"
        divider_2 = "----------------------------------------<<---<<<"
        if self.__products:
            for product in self.__products.values():
                print(f"{divider_1}\nName: {product.name}\nPrice: {format_currency(product.price)}\nQuantity: {product.stock}\n{divider_2}")
        else:
            print("There are no products in your cart")