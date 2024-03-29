import mysql.connector
import sys
from Entity import customers
from Entity import *
from serviceprovider import serviceprovider

class Main():
           
    def main():
        r=serviceprovider()
        while True:
            print("\n----------Main Menu----------")
            print("Press-1 Create product")
            print("Press-2 Create customer")
            print("Press-3 Delete product")
            print("Press-4 Delete customer")
            print("Press-5 Add to Cart")
            print("Press-6 Remove from Cart")
            print("Press-7 Show Cart")
            print("Press-8 Place Order")
            print("Press-9 Show Order by customer")
            print("Press-10 exit") 
            i=int(input())
            if i==1:
                product_id= input("Enter Product Id:")
                product_name = input("Enter product name: ")
                description = input("Enter description: ")
                price = float(input("Enter price: "))
                quantity=int(input("Enter stock quantity: "))
                r.create_product(product_id ,product_name, price,description,quantity)
            elif i==2:
                customer_id=input("Enter Customer_id: ")
                name=input("Enter name: ")
                password=input("Enter password: ")
                email=input("Enter mail id: ")
                r.create_customer(customer_id, name, email, password)
            elif i==3:
                product_id=input("Enter product id: ")
                r.delete_product(product_id)
            
            elif i==4:
                customer_id=input("Enter customer id: ")
                r.delete_customer(customer_id)
                
            elif i==5:
                cart_id = input("Enter cart_id: ")
                customer_id=input("Enter customer id: ")
                product_id=input("Enter product id: ")
                quantity=input("Enter the product quantity: ")
                r.addTocart(cart_id, customer_id,product_id,quantity)
                
            elif i==6:
                customer_id=input("Enter customer id: ")
                product_id=input("Enter product id: ")
                r.removefromcart(customer_id,product_id)
                
            elif i==7:
                customer_id=input("Enter customer id: ")
                rows = r.get_all_from_cart(customer_id)
                print(rows)
            
            elif i == 8:
                order_id = int(input("Enter order id: " ))
                customer_id = int(input("Enter customer id: "))
                shipping_address = input("Enter shipping address: ")
                success = r.placeOrder(order_id, customer_id, shipping_address)
                if success:
                    print("Order placed successfully!")
                else:
                    print("Failed to place the order.")
                            
            elif i == 9:       
                customer_id=input("Enter customer id: ")
                rows = r.getordersbycustomers(customer_id)
                print(rows)
            
            elif i == 10:
                print("Exiting Ecommerce Application")

                             

                
if __name__ == "__main__":
    Main.main()