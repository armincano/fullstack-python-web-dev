from virtualcart import VirtualCart
from db import db

def main():
    cart = VirtualCart()
    cart.add_product("FOR HiiiM", 1)
    cart.add_product("FOR HiM", 101)
    cart.add_product("for him", -1)
    # print(db["for him"].stock)
    print("\nadd a 'for him' to the cart with quantity of 1 ↓")
    cart.add_product("for him", 1)
    print("show the products from the cart ↓")
    cart.show_cart()
    # print(db["for him"].stock)
    print("\nadd a 'for him' to the cart with quantity of 1 ↓")
    cart.add_product("for him", 1)
    print("add a 'for him red edition' to the cart with quantity of 1 ↓")
    cart.add_product("for him red edition", 1)
    print("show the products from the cart ↓")
    cart.show_cart()
    print("\ncalculate total of the cart ↓")
    print(cart.calculate_total())
    print("\ndelete 'for him red edition' from the cart ↓")
    cart.delete_product("for him red edition")
    print("show the products from the cart ↓")
    cart.show_cart()
    print("\ncalculate total of the cart ↓")
    print(cart.calculate_total())
    
if __name__ == "__main__":
    main()