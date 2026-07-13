from __future__ import annotations

# TODO check this file. continue here ! ! ! 
# TODO check this file. continue here ! ! ! 
# TODO check this file. continue here ! ! ! 
# TODO check this file. continue here ! ! ! 
# TODO check this file. continue here ! ! ! 


class Automatic:
    """Represents a ticket vending machine for the swimming center.

    The object is created through :meth:`Automatic.create` and stores its
    machine number and the list of supported ticket options as plain strings.
    """

    def __init__(self):
        """Block direct construction of the class.

        Raises:
            RuntimeError: Always, because this class must be created through
                the factory method.
        """
        raise RuntimeError("cannot instantiate directly. Use Automatic.create() instead.")

    @classmethod
    def create(cls, number: int | None = None, **kwargs) -> "Automatic":
        """Create an Automatic instance from keyword arguments.

        Args:
            number: The machine number.
            **kwargs: Optional ``buy_options`` list and other metadata.

        Returns:
            Automatic: A configured automatic ticket machine object.

        Raises:
            ValueError: If the machine number is missing or invalid.
        """
        if number is None:
            number = kwargs.get("number")

        if not isinstance(number, int):
            raise ValueError("Automatic number must be an integer.")

        buy_options = kwargs.get("buy_options", [])
        if not isinstance(buy_options, list):
            raise ValueError("buy_options must be a list of strings.")

        obj = super().__new__(cls)
        obj.number = number
        obj.buy_options = buy_options
        return obj

    def sell(self, option: str, money: int, price: int = 0) -> str:
        """Simulate a ticket sale for one supported area option.

        Args:
            option: The requested area or ticket option.
            money: The amount inserted by the client.
            price: The ticket price.

        Returns:
            str: Status message for the transaction.
        """
        if option not in self.buy_options:
            return f"Invalid option: {option}"

        if money < price:
            return "Please insert more money."

        return f"Ticket created for {option}."

    def __str__(self) -> str:
        """Return a readable representation of the automatic."""
        options = ", ".join(self.buy_options) if self.buy_options else "none"
        return f"Automatic {self.number}: buy_options=[{options}]"


if __name__ == "__main__":
    automatic = Automatic.create(
        number=7,
        buy_options=["ENTRANCE", "CHILD", "SWIMMING", "SAUNA"],
    )

    print(automatic)
    print(automatic.sell("SWIMMING", 10, 10))
    print(automatic.sell("WC", 10, 10))