"""
This script for basic class constructor.
"""

class Laptop:
    """
    This is a test class
    """
    vat = 0.5


    def __init__(self, model, ram, price) -> None:
        self.model = model
        self.ram = ram
        self.price = price



    def calculate_vat(self) -> float:
        """
        This method Generate vat for instance.
        """
        return self.price + self.price* self.vat
    
    def __str__(self) -> str:
        return f'This is a {self.model} instance from Laptop class {self.calculate_vat()}'

print(Laptop('dell insprion 1433', 4, 15000))

