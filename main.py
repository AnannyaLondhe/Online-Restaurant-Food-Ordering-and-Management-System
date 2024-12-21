from restaurant import Restaurant
from customer import Customer
from menu import RegularMenuItem, SpecialMenuItem
from database import Database

class Prog:
    def create_menu_item(self):
        #Create a menu item by fetching details from the database.
        menu_name = input("Enter the menu item name: ").strip()
    
        # Query the database to fetch price, category, and discount based on the menu name
        query = "SELECT price, category, special_discount FROM menu WHERE name = %s"
        menu_details = self.db.fetch_one(query, (menu_name,))
    
        if menu_details:
            price = menu_details['price']
            category = menu_details['category']
            special_discount = menu_details.get('special_discount', 0)  # Default to 0 if None
        
            # Ask if it's a special menu item
            is_special = input("Is this a special menu item? (yes/no): ").strip().lower()
        
            if is_special == 'yes':
                # If special, use the discount fetched from the database
                print(f"Special Discount for {menu_name}: {special_discount}%")
                return SpecialMenuItem(None, menu_name, price, category, special_discount)
            else:
                # If not special, create a regular menu item
                return RegularMenuItem(None, menu_name, price, category)
        else:
            print(f"No menu item found with the name '{menu_name}' in the database.")
            return None


    def create_customer(self):
        print("Enter customer details:")
        name = input("Customer name: ")
        contact = input("Customer contact: ")
        return Customer(name, contact, self.restaurant_name, self.db)

    def main(self):
        # Initialize database connection
        self.db = Database(host='localhost', user='root', password='Anannya@06', database='restaurant_db')
        
        # Initialize the restaurant
        Restaurant.display_restaurant(prog)
        self.restaurant_name = input("Enter the name of the restaurant: ")
        self.restaurant = Restaurant(self.restaurant_name, self.db)
        self.restaurant.save_to_db()
        self.restaurant.display_menu()

        # Ask user for the number of menu items
        menu_items_count = int(input("Enter the number of menu items: "))
        for _ in range(menu_items_count):
            item = self.create_menu_item()  # Call method using self
            self.restaurant.add_menu_item(item)
            item.save_to_db(self.db)  # Save the menu item to the database

        # Ask user for customer details and save
        customer = self.create_customer()  # Call method using self
        #customer.save_to_db()  # Save customer to the database

        # Display menu and place an order
        #self.restaurant.display_menu()
        menu_items = []
        for item in self.restaurant.menu:
            quantity = int(input(f"How many {item.name}s would you like to order? "))
            menu_items.append((item, quantity))
        customer.place_order(self.restaurant, menu_items)

# Entry point
if __name__ == "__main__":
    prog = Prog()  # Create an instance of Prog
    prog.main()    # Call the main method
