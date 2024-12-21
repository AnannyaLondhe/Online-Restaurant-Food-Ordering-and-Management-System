from abc import ABC, abstractmethod

class MenuItem(ABC):
    def __init__(self, item_id, name, price, category):
        self.item_id = item_id
        self.name = name
        self._price = price  # Private attribute
        self._category = category

    @abstractmethod
    def display_item(self):
        pass

    @property
    def price(self):
        """
        Property to get the price of the item.
        """
        return self._price

    @property
    def category(self):
        """
        Property to get the category of the item.
        """
        return self._category

    def save_to_db(self, db):
        """
        Save the menu item to the database.
        """
        query = "INSERT INTO menu (name, price, category, restaurant_id) VALUES (%s, %s, %s, %s)"
        restaurant_id = self.get_restaurant_id()
        db.execute_query(query, (self.name, self.price, self.category, restaurant_id))

    def remove_from_db(self, db):
        """
        Remove the menu item from the database.
        """
        query = "DELETE FROM menu WHERE id = %s"
        db.execute_query(query, (self.item_id,))

    def get_restaurant_id(self):
        """
        Fetch the restaurant ID.
        This method assumes the restaurant is already linked and fetched using `self`.
        """
        return 1  # Assuming restaurant ID will be available, replace this with actual logic


class RegularMenuItem(MenuItem):
    def __init__(self, item_id, name, price, category):
        super().__init__(item_id, name, price, category)

    def display_item(self):
        """
        Display information about the regular menu item.
        """
        return f"Regular Item: {self.name} | Price: ${self.price:.2f} | Category: {self.category}"


class SpecialMenuItem(MenuItem):
    def __init__(self, item_id, name, price, category, discount_percentage):
        super().__init__(item_id, name, price, category)
        self.discount_percentage = discount_percentage

    def display_item(self):
        """
        Display information about the special menu item, including the discount.
        """
        discounted_price = self.price - (self.price * self.discount_percentage / 100)
        return f"Special Item: {self.name} | Original Price: ${self.price:.2f} | Discounted Price: ${discounted_price:.2f} | Category: {self.category}"

    @property
    def discount(self):
        """
        Property to get the discount percentage.
        """
        return self.discount_percentage
