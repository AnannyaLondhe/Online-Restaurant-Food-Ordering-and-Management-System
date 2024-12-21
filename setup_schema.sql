-- CREATE DATABASE restaurant_db;

USE restaurant_db;

-- CREATE TABLE menu_items (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(255),
--     price DECIMAL(10, 2),
--     category VARCHAR(50),
--     item_type VARCHAR(50)
-- );

-- CREATE TABLE customers (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(255),
--     contact VARCHAR(50)
-- );

-- -- Modify the orders table to add restaurant_id instead of restaurant_name
-- CREATE TABLE orders (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     customer_id INT,
--     restaurant_id INT,   -- New field for restaurant association
--     total_price DECIMAL(10, 2),
--     status VARCHAR(50),
--     FOREIGN KEY (customer_id) REFERENCES customers(id),
--     FOREIGN KEY (restaurant_id) REFERENCES restaurant(id)
-- );

-- CREATE TABLE restaurant (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(255) 
-- );

-- SET FOREIGN_KEY_CHECKS = 0;
-- truncate table restaurant;
-- SET FOREIGN_KEY_CHECKS = 1;

-- ALTER TABLE restaurant MODIFY COLUMN name VARCHAR(255) Unique NOT NULL;
--describe restaurant;
-- select * from restaurant;
-- show tables;
-- ALTER TABLE orders ADD COLUMN restaurant_id INT NOT NULL;
-- ALTER TABLE orders ADD CONSTRAINT fk_restaurant_id
-- FOREIGN KEY (restaurant_id) REFERENCES restaurant(restaurant_id);
-- describe orders; 

-- DELETE FROM customers WHERE contact = '123-456-7890' LIMIT 1; 
-- SET FOREIGN_KEY_CHECKS = 0;
-- truncate table customers;
-- SET FOREIGN_KEY_CHECKS = 1;

-- Alter table customers modify column contact varchar(50) unique not null;
-- describe customers;
-- ALTER TABLE orders
-- DROP COLUMN name,
-- DROP COLUMN item_id;
-- ALTER TABLE menu
-- ADD COLUMN special_discount DECIMAL(5,2) DEFAULT 0.00;
-- describe menu;
-- ALTER TABLE orders
-- DROP COLUMN special_discount;
-- describe orders;
INSERT INTO menu (restaurant_id, name, price, category, special_discount)
VALUES
    -- Restaurant 1: food mood
    (1, 'Margherita Pizza', 9.99, 'Main Course', 10.00),
    (1, 'Cheeseburger', 7.49, 'Main Course', 5.00),
    (1, 'Spaghetti Bolognese', 12.99, 'Main Course', 8.00),
    (1, 'Garlic Bread', 4.99, 'Appetizer', 2.50),
    (1, 'Tiramisu', 6.99, 'Dessert', 0.00),
    (1, 'Chocolate Lava Cake', 8.49, 'Dessert', 5.00),
    (1, 'Lemonade', 3.99, 'Beverage', 0.00),
    (1, 'Cappuccino', 4.99, 'Beverage', 1.00),

    -- Restaurant 2: Vegan Delights
    (2, 'Grilled Tofu Salad', 10.99, 'Main Course', 12.00),
    (2, 'Vegan Burger', 8.99, 'Main Course', 7.00),
    (2, 'Quinoa Bowl', 11.49, 'Main Course', 10.00),
    (2, 'Hummus & Pita', 5.99, 'Appetizer', 3.00),
    (2, 'Falafel Wrap', 7.99, 'Appetizer', 0.00),
    (2, 'Vegan Brownie', 6.49, 'Dessert', 5.00),
    (2, 'Herbal Tea', 2.99, 'Beverage', 0.00),
    (2, 'Almond Milk Latte', 4.49, 'Beverage', 1.50),

    -- Restaurant 3: The Steakhouse
    (3, 'Sirloin Steak', 18.99, 'Main Course', 15.00),
    (3, 'BBQ Ribs', 21.49, 'Main Course', 10.00),
    (3, 'Grilled Salmon', 19.99, 'Main Course', 12.00),
    (3, 'Caesar Salad', 7.99, 'Appetizer', 0.00),
    (3, 'Shrimp Cocktail', 9.49, 'Appetizer', 5.00),
    (3, 'Apple Pie', 5.99, 'Dessert', 2.00),
    (3, 'Molten Chocolate Cake', 7.49, 'Dessert', 0.00),
    (3, 'Classic Mojito', 6.99, 'Beverage', 0.00),

    -- Restaurant 4: Asian Fusion
    (4, 'Sushi Platter', 24.99, 'Main Course', 20.00),
    (4, 'Kung Pao Chicken', 13.99, 'Main Course', 8.00),
    (4, 'Vegetable Stir-Fry', 10.99, 'Main Course', 5.00),
    (4, 'Spring Rolls', 6.99, 'Appetizer', 3.00),
    (4, 'Pork Dumplings', 7.99, 'Appetizer', 4.00),
    (4, 'Mango Sticky Rice', 6.49, 'Dessert', 0.00),
    (4, 'Green Tea Ice Cream', 4.99, 'Dessert', 2.00),
    (4, 'Jasmine Tea', 2.99, 'Beverage', 0.00),

    -- Restaurant 5: Coastal Cafe
    (5, 'Lobster Roll', 15.99, 'Main Course', 10.00),
    (5, 'Fish Tacos', 12.49, 'Main Course', 7.00),
    (5, 'Clam Chowder', 9.99, 'Main Course', 5.00),
    (5, 'Fried Calamari', 7.49, 'Appetizer', 2.00),
    (5, 'Crab Cakes', 10.49, 'Appetizer', 4.00),
    (5, 'Key Lime Pie', 6.99, 'Dessert', 3.00),
    (5, 'Banana Split', 5.99, 'Dessert', 0.00),
    (5, 'Iced Coffee', 3.99, 'Beverage', 0.00);
