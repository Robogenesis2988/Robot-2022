from enum import Enum, auto
import wpilib


class DoubleSolenoid():
    """
    Double Solenoid object - Assumes type CTRE

    """

    class InputMode(Enum):
        Toggle = auto()
        Hold = auto()

    def __init__(self, openChannel: int, closeChannel: int):
        """

        """
        pass

    def open(self):
        """
        Opens the solenoid
        """
        pass

    def close(self):
        """
        Closes the solenoid
        """
        pass

    def getState(self) -> bool:
        """
        Returns the state of the solenoid

        False - closed
        True - open
        """

    def setState(self, state: bool):
        """
        Sets the state of the solenoid

        False - closed
        True - open
        """
        if state:
            self.open()
        else:
            self.close()
