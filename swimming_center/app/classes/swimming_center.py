
from swimming_center.app.data.config import Areas
from .automatics import Automatic

class SwimmingCenter:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.description = kwargs.get('description')
        self.address = kwargs.get('address')
        self.opening_hours = kwargs.get('opening_hours')
        self.areas = []
        self.automatics = []
        self.employees = []

    # Methods to manage areas

    def add_area(self, name):
        area = Area.create(name)
        self.areas.append(area)

    def remove_area(self, name):
        area = Area.create(name)
        if area in self.areas:
            self.areas.remove(area)

    # Methods to manage automatics
    
    def add_automatic(self, number):
        automatic = Automatic(number)
        self.automatics.append(automatic)

    def remove_automatic(self, number):
        automatic = Automatic(number)
        if automatic in self.automatics:
            self.automatics.remove(automatic)
        else:
            raise ValueError(f"Automatic with number {number} not found.")
        
    # mehtods to manage employees

    def add_employee(self, number):
        self.employees.append(number)

    def remove_employee(self, number):
        if number in self.employees:
            self.employees.remove(number)
        else:
            raise ValueError(f"Employee with number {number} not found.")

    # Additional methods for managing the swimming center can be added here.
    # please note that in a real swimming center, it is not so easy, to update the address, because it is a building.

    def rename(self, new_name):
        self.name = new_name

    def update_description(self, new_description):
        self.description = new_description

    def update_opening_hours(self, new_opening_hours):
        self.opening_hours = new_opening_hours

    def __str__(self):
        return f"Swimming Center: {self.name}, Description: {self.description}, Address: {self.address}, Opening Hours: {self.opening_hours}"