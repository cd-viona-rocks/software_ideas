from datetime import datetime, timedelta
import sys
import os

# Add the sibling folder's path to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')))
from config import WorkingHours, TicketOptions
from database import TICKETS

# TODO: review documentation for this module


class Ticket:
    """Represents a ticket for the swimming center.

    This class models aggregation: the ticket can exist independently of a
    swimming center and may be attached or removed without owning the center's
    lifecycle.
    """

    def __init__(self, ticket_type: TicketOptions = None, created_at: int = 0, allows_sauna: bool = False):
        """Create a Ticket instance.

        Args:
            ticket_type: The type of the ticket (e.g., "ENTRANCE", "CHILD").
            price: The price of the ticket.
            dealine: The deadline for the ticket in unix timestamp (optional).
        """
        self.ticket_number = id(self)  # Unique identifier for the ticket
        self.ticket_type = ticket_type.name
        self.ticket_code = ticket_type.value[0]
        self.description = ticket_type.value[3]
        self.price = ticket_type.value[1]
        self.sauna = False
        self.created_at = created_at
        self.deadline = None
        
        self.set_deadline()
        if allows_sauna: self.include_sauna()

    def set_deadline(self):
        """Set the creation time for the ticket. sets automatically deadline."""

        created_dt = datetime.fromtimestamp(self.created_at)
        closing_dt = created_dt.replace(
                hour=WorkingHours.CLOSING.value[0],
                minute=WorkingHours.CLOSING.value[1],
                second=WorkingHours.CLOSING.value[2],
                microsecond=0,
            )
        
        # DAY_PASS: deadline is the closing time on the same day
        if self.ticket_type == "DAY_PASS":            
            self.deadline = int(closing_dt.timestamp())
        # SHORT_TERM / LONG_TERM: period ends after a duration (hours) defined
        elif self.ticket_type in ("SHORT_TERM", "LONG_TERM"):
            hours = TicketOptions[self.ticket_type].value[2]
            period_ends = created_dt + timedelta(hours=hours)
            if period_ends > closing_dt:
                period_ends = closing_dt
            self.deadline = int(period_ends.timestamp())
        else:
            raise ValueError(f"Invalid ticket type. Must be one {[o.name for o in TicketOptions]}")

    def include_sauna(self):
        self.price += 1.5
        self.sauna = True

    def log_ticket(self):
        """Log the ticket information to the database."""
        TICKETS[self.ticket_number] = self

    def __str__(self):
        return f"Ticket(type={self.ticket_type}, number={self.ticket_number}, sauna={self.sauna}, price={self.price}, deadline={self.deadline})"
    


if __name__ == "__main__":

    def ts_to_dt(ts:int) -> str:
        dt = datetime.fromtimestamp(ts)
        formatted = dt.strftime("%Y-%m-%d %H:%M:%S")
        return formatted
    
    def dt_to_ts(dt: datetime) -> int:
        return int(dt.timestamp())
    
    def print_it(ticket: Ticket) -> None:
        print(ticket)
        print(f"created_at: {ts_to_dt(ticket.created_at)}, deadline at: {ts_to_dt(ticket.deadline)}")

    # Example usage: create a ticket and set a concrete creation datetime
    # set a specific creation datetime e.g. Monday july 13th, 2026 on 06:32:45 AM
    ticket = Ticket(ticket_type=TicketOptions.SHORT_TERM, created_at=dt_to_ts(datetime(2026, 7, 13, 6, 32, 45)))
    print_it(ticket)

    # and close before closing
    ticket = Ticket(ticket_type=TicketOptions.SHORT_TERM, created_at=dt_to_ts(datetime(2026, 7, 13, 20, 32, 45)))
    print_it(ticket)

    # what if the gast wants some hours sauna
    ticket = Ticket(ticket_type=TicketOptions.SHORT_TERM, created_at=dt_to_ts(datetime(2026, 7, 13, 20, 32, 45)), allows_sauna=True)
    print_it(ticket)