import wpilib
import wpilib.drive

from drivetrain import DriveTrain


timer = wpilib.Timer()


def autonomousInit():
    """This function is run once each time the robot enters autonomous mode."""
    timer.reset()
    timer.start()


def autonomousPeriodic(driveTrain: DriveTrain) -> None:
    if timer.get() < 2:
        driveTrain.moveRobot(1, 90, 0)
    else:
        driveTrain.moveRobot(0, 0, 0)

# class TimedAutonomous():
#     auto_actions = []

#     class Action():
#         class ActionType(Enum):
#             SingleAction = auto()
#             ContiniousAction = auto()

#         def __init__(self, type: ActionType) -> None:
#             type = type

#     def __init__(self) -> None:
#         timer = wpilib.Timer()

#     def autonomousInit(self):
#         timer.reset()
#         timer.start()

#     def autonomousPeriodic(self):
#         pass

#     def SingleAction(self, startTime: int, action: function):
#         """
#         startTime (in milliseconds)
#         action - The function to run
#         """
#         auto_actions.append((startTime, action))
