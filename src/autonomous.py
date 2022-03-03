# import wpilib
# import wpilib.drive

# from drivetrain import DriveTrain



# timer = wpilib.Timer

# #def autnomousInit():
# #    timer.reset()
# #    timer.start()

# #def autonomousPeriodic(drive: DriveTrain):
# #    if timer.get() < 2:
# #        drive.drivePolar(.25,0,0) #drives foward for one second at 1/4 speed
# #    elif (timer.get() > 2) & (timer.get() < 4):
# #        solenoidClimb1.set(solenoid1.Value.kForward) #from 1 - 4 seconds the solenoid extends 
# #        # if self.solenoid1.get() == self.solenoid1.Value.kOff:
#             #self.solenoid1.set(self.solenoid1.Value.kForward)
# #    elif (timer.get() > 4) & (timer.get() < 6):
# #        self.solenoid1.set(self.solenoid1.Value.kReverse)
# #    elif (timer.get() > 6) & (timer.get() < 8):
# #        drive.drivePolar(0,0,.72)

# # class TimedAutonomous():
# #     auto_actions = []

# #     class Action():
# #         class ActionType(Enum):
# #             SingleAction = auto()
# #             ContiniousAction = auto()

# #         def __init__(self, type: ActionType) -> None:
# #             type = type

# #     def __init__(self) -> None:
# #         timer = wpilib.Timer()

# #     def autonomousInit(self):
# #         timer.reset()
# #         timer.start()

# #     def autonomousPeriodic(self):
# #         pass

# #     def SingleAction(self, startTime: int, action: function):
# #         """
# #         startTime (in milliseconds)
# #         action - The function to run
# #         """
# #         auto_actions.append((startTime, action))
