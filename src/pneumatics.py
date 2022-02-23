from enum import Enum, auto
import wpilib


class DoubleSolenoid():
    """
    Double Solenoid object - Assumes type CTRE

    """

    def __init__(self, openChannel: int, closeChannel: int):
        self.solenoid = wpilib.DoubleSolenoid(
            wpilib.PneumaticsModuleType.CTREPCM, openChannel, closeChannel)

    def open(self):
        """
        Opens the solenoid
        """
        self.solenoid.set(wpilib.DoubleSolenoid.Value.kForward)

    def close(self):
        """
        Closes the solenoid
        """
        self.solenoid.set(wpilib.DoubleSolenoid.Value.kReverse)

    def disable(self):
        """
        Turns off the solenoid
        """
        self.solenoid.set(wpilib.DoubleSolenoid.Value.kOff)

    def getState(self) -> bool:
        """
        Returns the state of the solenoid

        False - closed
        True - open
        """
        return self.solenoid.get() == wpilib.DoubleSolenoid.Value.kForward

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

    def toggle(self):
        """
        Toggles the state of the solenoid
        """
        if not self.getState():
            self.open()
        else:
            self.close()
