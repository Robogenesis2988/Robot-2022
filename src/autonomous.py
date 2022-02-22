from enum import Enum, auto
# from magicbot import AutonomousStateMachine
import wpilib
import wpilib.drive


class TimedAutonomous():
    auto_actions = []

    class Action():
        class ActionType(Enum):
            SingleAction = auto()
            ContiniousAction = auto()

        def __init__(self, type: ActionType) -> None:
            self.type = type

    def __init__(self) -> None:
        self.timer = wpilib.Timer()

    def autonomousInit(self):
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        pass

    def SingleAction(self, startTime: int, action: function):
        """
        startTime (in milliseconds)
        action - The function to run
        """
        self.auto_actions.append((startTime, action))
