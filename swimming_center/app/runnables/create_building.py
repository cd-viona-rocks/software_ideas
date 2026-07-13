from app.classes.swimming_center import SwimmingCenter


def create_swimming_center():

    sw = SwimmingCenter({
        "name": "My Swimming Center",
        "description": "A great place to swim!",
        "address": "123 Main Street",
        "opening_hours": "6:00 AM - 22:00 PM"
    })

    areas = ["ENTRANCE", "CHILD", "SWIMMING", "SAUNA"]
    for name in areas:
        try:
            sw.add_area(name)
        except ValueError as e:
            print(f"Error: {e}")

    return sw