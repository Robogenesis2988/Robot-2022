#!/usr/bin/env python3
"""
    This is a good foundation to build your robot code on
"""

import wpilib
import wpilib.drive


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """

        self.left_motor = wpilib.Talon(0)
        self.right_motor = wpilib.Talon(1)
        self.solenoidDump = wpilib.DoubleSolenoid(wpilib.PneumaticsModuleType.CTREPCM, 1,0)
        self.solenoid2 = wpilib.DoubleSolenoid(wpilib.PneumaticsModuleType.CTREPCM, 3,2)
        self.solenoid3 = wpilib.DoubleSolenoid(wpilib.PneumaticsModuleType.CTREPCM, 5,4)

        self.drive = wpilib.drive.MecanumDrive(self.left_motor, self.right_motor)
        
        self.stick = wpilib.Joystick(0)
        
        self.timer = wpilib.Timer()
        

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        # Drive for two seconds
        if self.timer.get() < 2.0:
            self.drive.arcadeDrive(-0.5, 0)  # Drive forwards at half speed
        else:
            self.drive.arcadeDrive(0, 0)  # Stop robot

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.drive.driveCartesian(self.stick.getY(), self.stick.getX())
        if self.stick.getRawButtonPressed(2): 
            self.solenoidDump.toggle()
            if self.solenoidDump.get() == self.solenoidDump.Value.kOff:
                self.solenoidDump.set(self.solenoidDump.Value.kForward)


if __name__ == "__main__":
    wpilib.run(MyRobot)