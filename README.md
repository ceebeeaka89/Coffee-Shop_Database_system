# Project Background
The project was to create a drink shop application, that store orders by customers, couriers delivering the product and products sold in the drinks shop.This project provides a simple command-line interface to manage products, couriers, and orders for a store. It allows users to perform CRUD (Create, Read, Update, Delete) operations on these entities using CSV files.

# Client requirements
The client requirements was to build an application that could a variety of things fro three main areas of their business; Products, Couriers & Orders information.
The client would like to do the following: 
1. Perform CRUD (Create, Read, Update, Delete).
2. A storage system for the data: Products, Couriers & Orders.
3. The code should have a testing framework to ensure that it works as intended.
   

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Main Menu](#main-menu)
  - [Products Menu](#products-menu)
  - [Couriers Menu](#couriers-menu)
  - [Orders Menu](#orders-menu)
- [Helper Functions](#helper-functions)
- [File Structure](#file-structure)

## Features
- Load products and couriers from text and CSV files.
- Display lists of products, couriers, and orders.
- Add new products, couriers, and orders.
- Update existing products, couriers, and orders.
- Delete products, couriers, and orders.
- Save changes back to CSV files.

## Prerequisites
- Python 3.x
- CSV files named `products.csv`, `couriers.csv`, and `orders.csv` in the project directory.

## Installation
1. Clone the repository or download the project files.
2. Ensure you have Python 3.x installed.
3. Install any required packages (if any).

## Usage
Run the main script to start the application:

## Main Menu
Upon running the script, you will be presented with the main menu:

Select an option:
 0 for Exit App
 1 for Products Menu
 2 for Couriers Menu
 3 for Orders Menu
 
Option selected:

## Products Menu
- **0**: Exit to Main Menu
- **1**: Display Products List
- **2**: Add New Product
- **3**: Update Existing Product
- **4**: Delete Product

## Couriers Menu
- **0**: Exit to Main Menu
- **1**: Display Couriers List
- **2**: Add New Courier
- **3**: Update Existing Courier
- **4**: Delete Courier

## Orders Menu
- **0**: Exit to Main Menu
- **1**: Display Orders List
- **2**: Add New Order
- **3**: Update Order Status
- **4**: Update Existing Order
- **5**: Delete Order


## Helper Functions

The functionality is broken down into several helper functions located in `helper_functions.py`:

- `load_csv(filename)`: Load data from a CSV file.
- `print_product(products)`: Print the list of products.
- `print_courier(couriers)`: Print the list of couriers.
- `orders_print(orders)`: Print the list of orders.
- `product_info()`: Get new product information from the user.
- `courier_info()`: Get new courier information from the user.
- `orders_info()`: Get new order information from the user.
- `append_product(filename, product)`: Append a new product to the CSV file.
- `courier_append(filename, courier)`: Append a new courier to the CSV file.
- `orders_append(filename, order)`: Append a new order to the CSV file.
- `update_product(filename, products)`: Update an existing product in the CSV file.
- `courier_update(filename, couriers)`: Update an existing courier in the CSV file.
- `orders_update_order(filename, orders)`: Update an existing order in the CSV file.
- `orders_update_status(filename, orders)`: Update the status of an order in the CSV file.
- `delete_product(filename)`: Delete a product from the CSV file.
- `courier_delete(filename)`: Delete a courier from the CSV file.
- `orders_delete(filename)`: Delete an order from the CSV file.


## File Structure

The project files should be organized as follows:
.
- main.py
- helper_functions.py
- products.csv
- couriers.csv
- orders.csv
- README.md

'minor change again'
