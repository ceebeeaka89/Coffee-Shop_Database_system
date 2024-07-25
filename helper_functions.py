#MAIN MENU FUNCTION
# ////////////////////////////////////////////////////////////////////////
import csv

def Main_menu():
   int(input('Select an option:\n 0 for Exit App\n 1 for Products Menu\n 2 for Couriers Menu\n 3 for Orders Menu')) 

# //////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////
def load_csv(the_csv):
  list = []
  with open(the_csv, 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      list.append(row)
  return list
# //////////////////////////////////////////////////////////////
def append_product(the_csv,item):
   with open(the_csv, mode='a', newline = '') as csvfile:
      writer = csv.DictWriter(csvfile, fieldnames=item.keys()) 
      writer.writerow(item) 
# //////////////////////////////////////////////////////////////
def print_product(products):
   for n,product in enumerate(products):
      print(f"{n} Product Name: {product["name"]}, Price: £{product['price']}")

def update_product(filename, field_type):
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    for i, row in enumerate(data, start=1):
        print(f"{i}: {row}")

    row_to_update = int(input(f"\nEnter the row number (starting from 1) to update: ")) - 1

    if not (0 <= row_to_update < len(data)):
        print("Invalid row number!")
        return False

    updated_data = {key: input(f"Enter the new {key} (current value: '{value}'): ") for key, value in data[row_to_update].items()}

    data[row_to_update] = updated_data

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=updated_data.keys())
        writer.writeheader()
        writer.writerows(data)

    print(f"{field_type} row {row_to_update + 1} updated successfully!")
    return True

# //////////////////////////////////////////////////////////////
def update_csv_orders(filename):

  fields = ["customer_name", "customer_address", "customer_phone", "courier", "status", "items"]

  with open(filename, 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    # Check for empty CSV
    if not reader:
      print(f"Error: '{filename}' is empty.")
      return False

    # Show available rows with index
    print("Available rows:")
    for idx, row in enumerate(reader, start=1):
      print(f"  - Index: {idx} & The order: {row}")

  while True:
    try:
      row_to_update = int(input("Enter the index of the row to update (or 0 to exit): "))

      if 0 <= row_to_update <= 0:  # Check for exit or invalid index
        if row_to_update == 0:
          print("Exiting update process.")
          return True
        else:
          print(f"Error: Invalid index. Please enter 0 to exit or a valid row number.")
          continue  # Go back to the loop
      # Get user input for specific fields to update
      updated_data = {}
      for field in fields:
        value_to_display = row.get(field, "")  # Use get() with default ""

        print(f"Key: {field}, Value: {value_to_display} (or leave blank to keep existing): ")
        new_value = input("> ")
        if new_value:  # Update only if user provides a new value
          updated_data[field] = new_value


      # Update logic (assuming you have update functionality here)
      # ... (update the chosen row based on row_to_update)
      print(f"Order row {row_to_update} updated successfully!")
      return True

    except ValueError:
      print("Error: Please enter a valid number.")

  # This return statement is unreachable due to the loop's return statements
  # return False  # Unreachable code

def product_info():
    name = input('Enter the new product name:')
    price = input("Enter product price:")
    return {"name":name ,"price":price}
#delete the list
def delete_product(filename):
    # Open the products.txt file in read mode
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    # Get user input for product name (assuming valid input handling)
    for i, row in enumerate(data, start=1):
        print(f"{i}: {row}")
    
    row_to_delete = int(input(f"\nEnter the row number (starting from 1) to delete: ")) - 1

    del data[row_to_delete] 

    # Write the updated data back to the CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    print(f"Row {row_to_delete + 1} deleted successfully!")
    return True
    
# //////////////////////////////////////////////////////////////
#UPDATE
################
def courier_append(the_csv,item):
   with open(the_csv, mode='a', newline = '') as csvfile:
      writer = csv.DictWriter(csvfile, fieldnames=item.keys()) 
      writer.writerow(item)    
def print_courier(couriers):
   for n,courier in enumerate(couriers):
            print(f"{n} Courier Name: {courier["name"]}: Phone Number: {courier['phone']}")
def courier_update(filename,field_type):
  with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

  for i, row in enumerate(data, start=1):
        print(f"{i}: {row}")
  row_to_update = int(input(f"\nEnter the row number (starting from 1) to update: ")) - 1

  if not (0 <= row_to_update < len(data)):
        print("Invalid row number!")
        return False

  updated_data = {key: input(f"Enter the new {key} (current value: '{value}'): ") for key, value in data[row_to_update].items()}

  data[row_to_update] = updated_data

  with open(filename, 'w', newline='') as csvfile:
      writer = csv.DictWriter(csvfile, fieldnames=updated_data.keys())
      writer.writeheader()
      writer.writerows(data)

  print(f"{field_type} row {row_to_update + 1} updated successfully!")
  return True
def courier_info():
    
    name = input('Enter the new courier name:')
    phone_num = input("Enter courier phone number:")
    return {"name":name ,"phone":phone_num} 
def courier_delete(filename):
   # Open the products.txt file in read mode
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    # Get user input for product name (assuming valid input handling)
    for i, row in enumerate(data, start=1):
        print(f"{i}: {row}")
    
    row_to_delete = int(input(f"\nEnter the row number (starting from 1) to delete: ")) - 1

    if not (0 <= row_to_delete < len(data)):
        print("Invalid row number!")
        return False
    
    del data[row_to_delete] 

    # Write the updated data back to the CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    print(f"Row {row_to_delete + 1} deleted successfully!")
    return True
def read_courier_csv(the_csv):

  with open(the_csv, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"Name: {row['name']}: Phone Number: {row['phone']}")

################
################

def orders_print(orders):
   for n,order in enumerate(orders):
            print(f"{n} Customer Name: {order["customer name"]}: customer Address: {order["customer address"]} Customer phone number: {order["customer phone"]}: Courier Number: {order["courier"]} Status: {order["status"]} Items: {order["items"]} ")

def orders_info():
    
    customer_name = input("Enter customer name: ")
    customer_address = input("Enter customer address: ")
    customer_phone_number = input("Please enter your phone no: ")
    courier = int(input("choose the courier index: "))
    status = input("What is the order status?: ")
    items = input('Please input the item number?: ')
    return {'customer name':customer_name ,'customer address':customer_address,'customer phone number':customer_phone_number ,'courier':courier,'status':status, 'items' : items}
    #create an empty list
              
def orders_append(the_csv,item):
    with open(the_csv, mode='a', newline = '') as csvfile:
      writer = csv.DictWriter(csvfile, fieldnames=item.keys())
      writer.writerow(item)  
def orders_update_status(filename,field_csv):
  with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

  for i, row in enumerate(data, start=1):
        print(f"{i}: {row}")
  row_to_update = int(input(f"\nEnter the row number (starting from 1) to update: ")) - 1

  if not (0 <= row_to_update < len(data)):
        print("Invalid row number!")
        return False

  new_status = input(f"Enter the new {"status"} (current value: '{data[row_to_update]['status']}'): ")


  data[row_to_update]['status'] = new_status 

  with open(filename, 'w', newline='') as csvfile:
      writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
      writer.writeheader()
      writer.writerows(data)

  print( f"\n{field_csv} field in row {row_to_update + 1} updated successfully!")
  return True
def orders_delete(filename):
  # Open the products.txt file in read mode
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    # Get user input for product name (assuming valid input handling)
    for i, row in enumerate(data, start=1):
        print(f"{i}: {row}")
    
    row_to_delete = int(input(f"\nEnter the row number (starting from 1) to delete: ")) - 1

    if not (0 <= row_to_delete < len(data)):
        print("Invalid row number!")
        return False
    
    del data[row_to_delete] 

    # Write the updated data back to the CSV file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    print(f"Row {row_to_delete + 1} deleted successfully!")
    return True
def orders_update_order(filename,field_csv):
  with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

  for i, row in enumerate(data, start=1):
        print(f"{i}: {row}")
  row_to_update = int(input(f"\nEnter the row number (starting from 1) to update: ")) - 1

  if not (0 <= row_to_update < len(data)):
        print("Invalid row number!")
        return False

  new_order = input(f"Enter the new {"items"} (current value: '{data[row_to_update]['items']}'): ")


  data[row_to_update]['items'] = new_order 

  with open(filename, 'w', newline='') as csvfile:
      writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
      writer.writeheader()
      writer.writerows(data)

  print(f"\n{field_csv} field in row {row_to_update + 1} updated successfully!")
  return True
