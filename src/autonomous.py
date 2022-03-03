import wpilib
import wpilib.drive


class autonomous:

    def __init__(self):
        self.timer = wpilib.Timer

    def autnomousInit(self):
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        if self.timer.get() < 1:
            self.drive.drivePolar(.25,0,0) #drives foward for one second at 1/4 speed
        elif (self.timer.get() > 1) & (self.timer.get() < 4):
            self.solenoid1.set(self.solenoid1.Value.kForward) #from 1 - 4 seconds the solenoid extends 
           # if self.solenoid1.get() == self.solenoid1.Value.kOff:
                #self.solenoid1.set(self.solenoid1.Value.kForward)
        elif (self.timer.get() > 4) & (self.timer.get() < 6):
            self.solenoid1.set(self.solenoid1.Value.kReverse)
        elif (self.timer.get() > 6) & (self.timer.get() < 8):
            self.drive.drivePolar(0,0,.72)
=======
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
=======
>>>>>>> f89df4a156cf2a94f7df8d6ae64d7d53dd175672
>>>>>>> Stashed changes
