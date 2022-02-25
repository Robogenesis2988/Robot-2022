import wpilib

class winch:
    def __init__(self) -> None:
        self.leftWinch = wpilib.Talon(4)
        self.rightWinch = wpilib.Talon(5)

        self.rightWinch.setInverted(True)

        self.timer = wpilib.Timer()
        self.time = 0 

    def winchExtend(self):
        self.leftWinch.set(.5)
        self.rightWinch.set(.5)
    
    def winchRetract(self):
        self.leftWinch.set(-.5)
        self.rightWinch.set(-.5)
    def winchStop(self):
        self.leftWinch.set(0)
        self.rightWinch.set(0)

    def winchExtendTimed(self):
        self.winchExtend()
        self.timer.hasElapsed(self.time)
        self.winchRetract()

    def winchRetractTimed(self):
        self.leftWinch.set(.5)
        self.rightWinch.set(.5)
        self.timer.hasElapsed(self.time)
        self.leftWinch.set(0)
        self.rightWinch.set(0)


