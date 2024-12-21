class Customer:
    def __init__(self, name, contact,restaurant_name,db):
        self.name = name
        self.contact = contact
        self.restaurant_name=restaurant_name
        self.db=db
        
        

    def save_to_db(self):
        query = "INSERT INTO customers (name, contact) VALUES (%s, %s)"
        self.db.execute_query(query, (self.name, self.contact))

    def get_customer_id(self):
        """
        Fetch the customer ID from the database using the name and contact.
        """
        query = "SELECT id FROM customers WHERE name = %s AND contact = %s"
        print(f"Debug: Executing query: {query}")
        print(f"Debug: Parameters: ({self.name}, {self.contact})")
        params = (self.name, self.contact)
        result = self.db.fetch_one(query, params)
        print(f"Debug: Query result: {result}")
        if result:
            return result['id']  # Assuming fetch_one returns a dictionary
        else:
            insert_query = "INSERT INTO customers (name, contact) VALUES (%s, %s)"
            self.db.execute_query(insert_query, params)
            # Retrieve the last inserted ID
            last_id_query = "SELECT LAST_INSERT_ID() AS id"
            result = self.db.fetch_one(last_id_query)
            return result["id"]

        
    def place_order(self, restaurant, menu_items):
        order_total = 0
        order_details = []

        for item, quantity in menu_items:
            order_total += item.price * quantity
            order_details.append((item.name, quantity, item.price * quantity))

        # Save the order to the database with restaurant_id
        query = "INSERT INTO orders (restaurant_id, customer_id, total_price,quantity) VALUES (%s, %s, %s,%s)"
        customer_id = self.get_customer_id()
        restaurant_id = restaurant.get_restaurant_id()  # Method to fetch restaurant ID
        self.db.execute_query(query, (restaurant_id, customer_id, order_total,quantity))

        print(f"Order placed successfully! Total: ${order_total:.2f}")
        return order_details

