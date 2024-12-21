class MenuItemNotFoundException(Exception):
    def __init__(self, message="Menu Item Not Found"):
        self.message = message
        super().__init__(self.message)

class OrderProcessingError(Exception):
    def __init__(self, message="Error Processing Order"):
        self.message = message
        super().__init__(self.message)

class DatabaseConnectionError(Exception):
    def __init__(self, message="Database Connection Error"):
        self.message = message
        super().__init__(self.message)
