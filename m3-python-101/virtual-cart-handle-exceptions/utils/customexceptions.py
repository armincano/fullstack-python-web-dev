class StockInsufficientError(Exception):
    def __init__(self, message="There is no enough stock of"):
        self.message = message
        super().__init__(message)

class ProductNotFound(Exception):
    def __init__(self, message="was not found in the DB."):
        self.message = message
        super().__init__(message)