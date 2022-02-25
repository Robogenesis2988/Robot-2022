import wpilib

class winch:
    def __init__(self) -> None:
        self.leftWinch = wpilib.Talon(4)
        self.rightWinch = wpilib.Talon(5)

        self.rightWinch.setInverted(True)

        self.timer = wpilib.Timer()
        self.time = 0 

    def winchExtendAdjustable(self):
        self.leftWinch.set(.5)
        self.rightWinch.set(.5)
    
    def winchRetractAdjustable(self):
        self.leftWinch.set(-.5)
        self.rightWinch.set(-.5)

    def winchExtendTimed(self):
        self.leftWinch.set(.5)
        self.rightWinch.set(.5)
        self.timer.hasElapsed(self.time)
        self.leftWinch.set(0)
        self.rightWinch.set(0)

    def winchRetractTimed(self):
        self.leftWinch.set(.5)
        self.rightWinch.set(.5)
        self.timer.hasElapsed(self.time)
        self.leftWinch.set(0)
        self.rightWinch.set(0)


