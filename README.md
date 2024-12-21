# Online-Restaurant-Food-Ordering-and-Management-System
Python OOPs and SQL | 2024
**Restaurant Management System** 🍴
A Python-based object-oriented program to manage restaurant operations, including menu management, customer handling, and order placement, with database integration using MySQL.

**Features** 🚀
1. Menu Management: Add and display menu items with price, category, and discount details.
2. Customer Management: Add new customers to the database or retrieve existing customer details.
3. Order Placement: Place orders for menu items and calculate the total cost based on discounts.
4. Database Integration: MySQL-based database to store restaurant, menu, and customer details.

**Usage** 📖
1. Start the program and provide the restaurant name.
2. Add menu items by specifying their name.
3. Enter customer details for placing orders.
4. Place orders by selecting menu items and quantities.
5. The system will calculate the total price based on the discounts and store the order in the database.

**Project Structure** 📂
restaurant-management-system/

├── main.py                # Entry point for the application

├── customer.py            # Customer class and related logic

├── menu.py                # Menu class for handling menu items

├── restaurant.py          # Restaurant class for managing operations

├── database.py            # Database connection and queries

├── setup_schema.sql              # SQL script for setting up the database

├── exceptions.py           # Custom exceptions for error handling

└── README.md              # Documentation file
