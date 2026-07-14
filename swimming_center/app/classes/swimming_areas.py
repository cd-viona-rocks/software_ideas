import sys
import os

# Add the sibling folder's path to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')))
from config import Areas

class Area:
    """Represents one swimming-area definition for the swimming center.

    An Area object is always constructed through :meth:`Area.create`.
    The class intentionally blocks direct instantiation to keep the
    creation flow controlled.
    """

    def __init__(self): # composition code structure. 
        """Prevent direct construction of ``Area``.
        An area cannot exist without a swimming center.

        Raises:
            RuntimeError: Always, because direct creation is not allowed.
        """
        raise RuntimeError("cannot instantiate directly. Use Area.create() instead.")

    @classmethod
    def create(cls, name):
        """Create a valid Area instance from keyword arguments.

        Args:
            **kwargs: Must contain ``name`` and optionally ``description``.

        Returns:
            Area: A new Area instance with a validated enum code.

        Raises:
            ValueError: If the provided ``name`` is not one of the allowed
                Area enum members.
        """
        
        if name not in Areas.__members__:
            raise ValueError("Invalid area name. Must be one of: " + ", ".join([area.name for area in Areas]))

        obj = super().__new__(cls)
        obj.code = Areas[name].value[0]
        obj.description = Areas[name].value[1]
        return obj
    
    def __str__(self):
        """Return the area as a readable string representation."""
        return f"Area {self.code}: {self.description}"
    

if __name__ == "__main__":
    # Example usage
    areas = ["ENTRANCE", "CHILD", "SWIMMING", "WC", "SAUNA"]

    for name in areas:
        try:
            print(Area.create(name))
        except ValueError as e:
            print(f"Error: {e}")

    # WANTED OUTPUT
    # - - - - - - -
    # create three areas: entrance, child, swimming;
    # then raise error, because WC is not a valid area name.

    # Area 0: Entrance area, bistro, tickets, info point.
    # Area 1: A safe area for children to play.
    # Area 2: The main swimming area with different lanes.
    # Error: Invalid area name. Must be one of: ENTRANCE, CHILD, SWIMMING, SAUNA
    # Area 3: A relaxing sauna area.