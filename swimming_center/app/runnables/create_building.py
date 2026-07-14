import sys
import os

# Add the sibling folder's path to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')))
from config import WorkingHours

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'classes')))
from swimming_center import SwimmingCenter


def create_swimming_center():

    sw = SwimmingCenter({
        "name": "My Swimming Center",
        "description": "A great place to swim!",
        "address": "123 Main Street",
        "opening_hours": f"{WorkingHours.OPENING.value[0]}:00 AM - {WorkingHours.CLOSING.value[0]}:00 PM"
    })

    #  - - - areas - - -

    areas = ["ENTRANCE", "CHILD", "SWIMMING", "SAUNA"]
    for name in areas:
        try:
            sw.add_area(name)
        except ValueError as e:
            print(f"Error: {e}")

    # - - - automatics - - -
    automatics = [1001, 1002, 1003, 1004]
    for auto in automatics:
        try:
            sw.add_automatic(auto)
        except ValueError as e:
            print(f"Error: {e}. Automatic ID: {auto} couldn't be added.")

    # - - - employees - - -
    # TODO: Implement employee management logic here if needed.

    return sw