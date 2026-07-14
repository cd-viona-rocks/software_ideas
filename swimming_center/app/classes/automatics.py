
from datetime import datetime

import sys
import os

# Add the sibling folder's path to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')))
from config import WorkingHours, TicketOptions

from ticket import Ticket

# TODO check this file. continue here ! ! ! 

class Automatic:
    """Represents a ticket vending machine for the swimming center.

    This class models aggregation: the machine can exist independently of a
    swimming center and may be attached or removed without owning the center's
    lifecycle.
    """
    Serial = []

    def __init__(self, number: int):
        """Create an Automatic instance.

        Args:
            number: The machine number.

        Raises:
            ValueError: If the machine number already exists or is not an integer.
        """
        if not isinstance(number, int):
            raise ValueError("Automatic number must be an integer.")

        if number in Automatic.Serial:
            raise ValueError(f"Automatic number {number} already exists.")

        self.number = number
        Automatic.Serial.append(number)

    
    def sell(self, 
            option: TicketOptions, 
            money: int, 
            hasSubscription: bool = False, 
            create_at: int = 0,
            allowSauna: bool = False
        ) -> Ticket:
        """Simulate a ticket sale for one supported area option."""
        if option not in TicketOptions:
            return f"Invalid option: {option}"

        if money < option.value[1]:
            return "Please insert more money. The operation will be canceled."

        # Free ticket for subscription holders
        if hasSubscription:
            ticket = Ticket(option.DAY_PASS, create_at, allowSauna)
        else:
            ticket = Ticket(option, create_at, allowSauna)        

        return ticket

    def __str__(self) -> str:
        """Return a readable representation of the automatic."""
        return f"Automatic(number={self.number})"
    