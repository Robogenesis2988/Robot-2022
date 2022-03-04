import wpilib
import wpilib.interfaces


class Winch:
    speed = 0.75

    def __init__(self, winchMotor: wpilib.interfaces.MotorController) -> None:
        self.winchMotor = winchMotor

    def winchExtend(self):
        self.winchMotor.set(-self.speed)

    def winchRetract(self):
        self.winchMotor.set(self.speed)

    def winchStop(self):
        self.winchMotor.set(0)


# class winch:
#     def __init__(self, winchMotor: wpilib.interfaces.MotorController) -> None:
#         self.winchMotor = winchMotor

#         self.timer = wpilib.Timer()
#         self.time = 5

#         """
#         State
#         0 - winch is not moving
#         1 - winch is extending
#         -1 - winch is retracting
#         """
#         self.State = 0

#     def restartTimer(self):
#         self.timer.reset()
#         self.timer.start()

#     def winchExtend(self):
#         self.winchMotor.set(.5)
#         self.State = 1

#     def winchRetract(self):
#         self.winchMotor.set(-.5)
#         self.State = -1

#     def winchStop(self):
#         self.winchMotor.set(0)
#         self.State = 0

#     def winchExtendTimed(self, time: int = 0):
#         """
#         Time - in seconds
#         """
#         if time != 0:
#             self.time = time

#         self.restartTimer()
#         self.winchExtend()

#     def winchUpdate(self):
#         if self.timer.hasElapsed(self.time) == True:
#             self.winchStop()

#     def winchRetractTimed(self, time: int):
#         """
#         Time - in seconds
#         """
#         if time != 0:
#             self.time = time

#         self.restartTimer()
#         self.winchRetract()
