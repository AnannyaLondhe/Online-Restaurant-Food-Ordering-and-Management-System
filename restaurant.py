from database import Database
from menu import RegularMenuItem, SpecialMenuItem

class Restaurant:
    def __init__(self, name, db):
        self.name = name
        self.menu = []
        self.restaurant_id = None  # This will be set when restaurant is saved
        self.db = db  # Database instance
    @staticmethod
    def display_restaurant(instance):
        print("choose your favorite restaurant")
        query="Select name from restaurant"
        restaurant_names=instance.db.fetch_all(query)
        if restaurant_names:
            print(f"{'name':<20}")
            print("-" * 60)
            for names in restaurant_names:
                name = names['name']
                print(f"{name:<20}")


    def display_menu(self):
        print(f"Welcome to {self.name}!")
        
        if not self.restaurant_id:
            print("Restaurant ID is not available.")
            return
        
        # Fetch the menu items for this restaurant_id from the database
        query = "SELECT name, price, category, special_discount FROM menu WHERE restaurant_id = %s"
        menu_items = self.db.fetch_all(query, (self.restaurant_id,))

        if menu_items:
            print("Menu:")
            # Print the header of the table
            print(f"{'Name':<20}{'Price':<10}{'Category':<15}{'Discount (%)':<15}")
            print("-" * 60)
            # Print the menu items in table format
            for item in menu_items:
                name = item['name']
                price = item['price']
                category = item['category']
                special_discount = item['special_discount'] if item['special_discount'] else 0
                print(f"{name:<20}{price:<10}{category:<15}{special_discount:<15}")
        else:
            print("No menu items available.")

    def add_menu_item(self, item):
        """
        Add a menu item to the restaurant's menu and save it to the database.
        """
        self.menu.append(item)
        #item.save_to_db(self.db)  # Save the item to the database after adding

    def remove_menu_item(self, item):
        """
        Remove a menu item from the restaurant's menu.
        """
        if item in self.menu:
            self.menu.remove(item)
            item.remove_from_db(self.db)  # Remove from the database as well

    def save_to_db(self):
        """Save restaurant to the database and fetch its ID."""
        query = "INSERT INTO restaurant (name) VALUES (%s) ON DUPLICATE KEY UPDATE name=%s"
        self.db.execute_query(query, (self.name, self.name))

        # Fetch the restaurant_id after saving
        query = "SELECT id FROM restaurant WHERE name = %s"
        result = self.db.fetch_one(query, (self.name,))
        if result:
            self.restaurant_id = result['id']

    def get_restaurant_id(self):
        """
        Fetch the restaurant ID based on the restaurant name.
        """
        query = "SELECT id FROM restaurant WHERE name = %s"
        result = self.db.fetch_one(query, (self.name,))
        if result:
            return result['id']
        else:
            raise Exception(f"Restaurant '{self.name}' not found in the database.")
