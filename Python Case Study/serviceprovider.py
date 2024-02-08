import mysql.connector 
from datetime import datetime

class serviceprovider():
    
    def create_product(self, id,name, price,description,stockQuantity):
        con = mysql.connector.connect( user="root", password="root", database="ecommerce_application",port="3306",auth_plugin='mysql_native_password')
        product_id = id
        try: 
            query = f"INSERT INTO products (product_id ,name, price,description,stock_quantity) VALUES ('{product_id}','{name}', '{price}','{description}', '{stockQuantity}')"
            c = con.cursor()
            c.execute(query)
            con.commit()
            product_id = c.lastrowid
            print(f"\nProduct '{name}' added to the database \n")
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            con.close()

    def create_customer(self, id, name, email, password):
        con = mysql.connector.connect(user="root", password="root", database="ecommerce_application",port="3306",auth_plugin='mysql_native_password')
        customer_id = id
        try:
            query = f"INSERT INTO customers (customer_id, name, email, password) VALUES ('{customer_id}','{name}', '{email}', '{password}')"
            c = con.cursor()
            c.execute(query)
            con.commit()
            customer_id = c.lastrowid
            print(f"\nCustomer '{name}' added to the database \n")
            return customer_id
        except Exception as e:
            print(e)
            return None
        finally:
            pass 

    def customer_exists(self, name, password):
        con = mysql.connector.connect(user="root", password="root", database="ecommerce_application",port="3306",auth_plugin='mysql_native_password')
        try:
            
            query = f"SELECT COUNT(*) FROM customers WHERE name = '{name}' AND password = '{password}'"
            c = con.cursor()
            c.execute(query)
            con.commit()
            count = 1
            return count
        except Exception as e:
            print(e)
            return False
        finally:
            pass
        
    def delete_product(self,product_id):
        con = mysql.connector.connect(user="root", password="root", database="ecommerce_application",port="3306",auth_plugin='mysql_native_password')
        try:
            query = f"DELETE FROM products WHERE product_id = {product_id}"
            c = con.cursor()
            c.execute(query)
            con.commit()
            if c.rowcount > 0:
                print(f"Product with ID: {product_id} deleted successfully.")
            else:
                print(f"No product found with ID: {product_id}. Nothing was deleted.")
            return False
        except Exception as e:
            print(e)
            return None
        finally:
            pass
        
    def delete_customer(self, customer_id):
        con = mysql.connector.connect(user="root", password="root", database="ecommerce_application",port="3306",auth_plugin='mysql_native_password')
        try:
            query = f"DELETE FROM customers where customer_id = {customer_id}"
            c= con.cursor()
            c.execute(query)
            con.commit()
            if c.rowcount > 0:
                print(f"Customer with ID: {customer_id} deleted successfully.")
            else:
                print(f"No customer found with ID: {customer_id}. Nothing was deleted.")
            return False
        except Exception as e:
            print(e)
            return None
        finally:
            pass
        
    def addTocart(self,id, customer_id,product_id, quantity):
        con = mysql.connector.connect(user="root", password="root", database="ecommerce_application",port="3306",auth_plugin='mysql_native_password')
        cart_id = id
        # try:
        #     checking = f"select stockQuantity from products where product_id = {product_id}"
        
        #     query = f"INSERT INTO cart (cart_id ,customer_id, product_id, quantity) VALUES ('{cart_id}','{customer_id}', '{product_id}','{quantity}')"
        #     c= con.cursor()
        #     c.execute(query)
        #     con.commit()
        #     print(f"Product ID {product_id} added to the cart for Customer ID {customer_id}. Quantity: {quantity}")
        #     return True
        # except Exception as e:
        #     print(e)
        #     return False
        # finally:
        #     con.close()
        try:
            # Check if there is sufficient stock quantity
            checking_query = f"SELECT stock_quantity FROM products WHERE product_id = {product_id}"
            c = con.cursor()
            c.execute(checking_query)
            stock_quantity = c.fetchone()[0]
            print(int(stock_quantity))
            if int(stock_quantity) >= int(quantity):
                # Update the stock quantity and add to cart
                update_query = f"UPDATE products SET stock_quantity = stock_quantity - {quantity} WHERE product_id = {product_id}"
                c.execute(update_query)

                add_to_cart_query = f"INSERT INTO cart (cart_id, customer_id, product_id, quantity) VALUES ('{cart_id}', '{customer_id}', '{product_id}', '{quantity}')"
                c.execute(add_to_cart_query)

                con.commit()
                print(f"Product ID {product_id} added to the cart for Customer ID {customer_id}. Quantity: {quantity}")
                return True
            else:
                print(f"Insufficient stock for Product ID {product_id}. Available stock: {stock_quantity}, Requested quantity: {quantity}")
                return False
        except Exception as e:
            print(e)
            return False
        finally:
            con.close()
        
    def removefromcart(self,customer_id,product_id,):
        con = mysql.connector.connect(user="root", password="root", database="ecommerce_application",port="3306",auth_plugin='mysql_native_password')
        try:
            query = f"DELETE FROM cart WHERE customer_id ={customer_id} AND product_id = {product_id}"
            c= con.cursor()
            c.execute(query)
            con.commit()
            if c.rowcount > 0:
                print(f"Product ID {product_id} removed from the cart for Customer ID {customer_id}.")
            else:
                print(f"No product found in the cart for Customer ID {customer_id} with Product ID {product_id}. Nothing was removed.")
            return False
        except Exception as e:
            print(e)
            return None
        finally:
            pass
        
    def get_all_from_cart(self,customer_id):
        try:
            con = mysql.connector.connect(user="root", password="root", database="ecommerce_application",port="3306",auth_plugin='mysql_native_password')
        
            query = f"SELECT product_id, quantity FROM cart WHERE customer_id = {customer_id}"
            c = con.cursor()
            c.execute(query)
            rows = c.fetchall()
            return rows
        
        except mysql.connector.Error as e:
            print("Error:", e)
            return None
        finally:
            if 'con' in locals() and con.is_connected():
                c.close()
                con.close()
                
    def placeOrder(self, id, customer_id, shipping_address):
        order_id = id
        
        con = mysql.connector.connect(user="root", password="root", database="ecommerce_application",port="3306",auth_plugin='mysql_native_password')
        try: 
            cart_query = "SELECT p.product_id, p.price, c.quantity FROM cart c INNER JOIN products p ON c.product_id = p.product_id WHERE c.customer_id = %s"
            c = con.cursor()
            c.execute(cart_query, (customer_id,))
            cart_products = c.fetchall()

  
            total_price = sum(product[1] * product[2] for product in cart_products)
            for product in cart_products:
                print(product)
            order_date = datetime.now().strftime("%Y-%m-%d")
            order_query = "INSERT INTO orders (order_id ,customer_id, order_date, total_price, shipping_address) VALUES (%s,%s, %s, %s, %s)"
            order_values = (order_id, customer_id, order_date, total_price, shipping_address)
            c = con.cursor()
            c.execute(order_query, order_values)


            order_items_query = "INSERT INTO order_items (order_item_id, order_id, product_id, quantity) VALUES (%s, %s, %s, %s)"
            print(len(cart_products))
            for product in cart_products:
                order_item_id = int(input("Enter order Item id: "))
                # product_id = int(input("enter the product id: "))
                # quantity = int(input("enter the quantity: "))
                item_values = (order_item_id, order_id , product[0], product[2])
                c = con.cursor()
                c.execute(order_items_query, item_values)
                con.commit()

            
            # for product in cart_products:
            #     productid = product[0]
            #     quantity = product[2]

            #     change_product_stock = f"UPDATE products SET stockQuantity = stockQuantity - {quantity} WHERE product_id = {productid};"
            #     c= con.cursor()
            #     c.execute(change_product_stock)
            #     con.commit()


            
            clear_cart_query = "DELETE FROM cart WHERE customer_id = %s"
            c = con.cursor()
            c.execute(clear_cart_query, (customer_id,))



            con.commit()
            print(f"Total Price: {total_price}")
            return True
        except Exception as e:
            print(f"Error occurred: {e}")
            return False
        finally:
            c.close()
            
    def getordersbycustomers(self,customer_id):
        con = mysql.connector.connect(user="root", password="root", database="ecommerce_application",port="3306",auth_plugin='mysql_native_password')
        try:
            query = f"SELECT order_id,order_date,total_price, shipping_address quantity FROM orders WHERE customer_id = {customer_id}"
            c = con.cursor()
            c.execute(query)
            rows = c.fetchall()
            return rows
        
        except mysql.connector.Error as e:
            print("Error:", e)
            return None
        finally:
            if 'con' in locals() and con.is_connected():
                c.close()
                con.close()
        
        
        
    
                


        
    
        
    
        
            
            
        
                
                
    
                