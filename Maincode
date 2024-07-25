
# LOAD products list from products.txt
# LOAD couriers list from couriers.txt
#this function load the text file and displays the content
# def Load_txt_file(text_file):
#    with open(text_file,'r') as load_file:
#    content = load_file.read()
#    return content
#print(Load_txt_file('products.txt'))
# add_products = open('products.txt','a')
# add_couriers = open('couriers.txt','a')
#when you use the (*) for an import - it imports everything from the other file

import csv

from helper_functions import *
# ////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////
  


# CREATE order status list
order_status = ['Preparing','On route','Delivered','Out of Stock']

#loading the csv for each
products = load_csv('products.csv')
couriers = load_csv('couriers.csv')
orders = load_csv('orders.csv')


# PRINT main menu options
# GET user input for main menu option

while True :
  response = int(input('Select an option:\n 0 for Exit App\n 1 for Products Menu\n 2 for Couriers Menu\n 3 for Orders Menu \nOption selected:')) 
  if response == 0:
    
    exit()

  elif response == 1:
    while True :
      product_option = int(input('0 - Exit to Main Menu\n 1 - Products List\n 2 - New Product\n 3 - Update Product\n 4 - Delete Product\n \nOption selected:'))
      #if 0 exit to main menu , 
      if product_option == 0:
        #return you back to the beginning of the code
        break #takes you out of a while loop
      #if 1 print product list, 
      elif product_option == 1:
        print()
        print('Here are the items sold in the store:')
        print()
        #read_csv('products.csv')
        
          #print
        
        print_product(products)
        # exit()
      
      # if 2 create new product
      # APPEND product name to products list
      elif product_option == 2:
        new_product = product_info()#store into a variable the input
        products.append(new_product)
        append_product('products.csv',new_product)
      #if 3 update existing
      elif product_option == 3:
        # PRINT product names with its index value
        #i want to open a txt file that has my products
        update_product('products.csv',products)
        #user_product_name.append(load_list('product.txt'))

      ## if 4 delete product
      elif product_option == 4:
      ##GET user input for product index value & product name & then delet the product from a list and uplad a new list
        delete_product('products.csv')
        
  elif response == 2:
    while True :
      courier_option = int(input('0 - Exit to Main Menu\n 1 - Couriers List\n 2 - New Courier\n 3 - Update Existing Courier\n 4 - Delete Courier \nOption selected:'))
      #if 0 exit to main menu , 
      if courier_option == 0:
        #return you back to the beginning of the code
          break #takes you out of a while loop

      #if 1 print product list, 
      elif courier_option == 1:
        print()
        print('Here are the list of couriers:')
        print()
        
        print_courier(couriers)
          #use a method to capitalise
          
        print()
        # exit()
      
      # if 2 create new product
      # GET user input for product name
      # APPEND product name to products list
      elif courier_option == 2:
        #get input for new product name & 
        new_courier = courier_info()#store into a variable the input
        couriers.append(new_courier)
        courier_append('couriers.csv',new_courier)
       
        break
      #if 3 update existing
      elif courier_option == 3:
          # PRINT product names with its index value
          #i want to open a txt file that has my products
          #update_courier = courier_info()
          
          courier_update('couriers.csv',couriers)
                
          break     
                #user_product_name.append(load_list('product.txt'))
      # #if 4 delete product
      elif courier_option == 4:
        courier_delete('couriers.csv')
        break
    #  DELETE product at index in products list
      # access the product from the list
      ######################################################################
      ######################################################################
      ######################################################################
      ##################################################################
      ##ORDERS################################################################

  elif response == 3: 
    while True :  
      order_option = int(input('0 - Exit to Main Menu\n 1 - Print orders \n 2 - Create orders\n 3 - update order status\n 4 - Update existing order\n 5 - delete order \nOption selected:'))
      if order_option == 0:
        #return you back to the beginning of the code
        break
      if order_option == 1:
        #  The outer loop iterates through each dictionary (order) in the orders list.
        orders_print(orders)
              
      if order_option == 2:
        
        add_order = orders_info()
        orders.append(add_order)
        orders_append('orders.csv',add_order)

        print("Order added successfully!")
          # APPEND order to orders list
        break
      #UPDATE THE ORDER STATUS 
      if order_option == 3:

        orders_update_status('orders.csv',orders)
        
      #UPDATE THE ORDER STATUS
      if order_option == 4:
        orders_update_order('orders.csv',orders)
      
      elif order_option == 5:
        orders_delete('orders.csv')
        break
