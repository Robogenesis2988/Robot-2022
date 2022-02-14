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
        
        self.leftFront = wpilib.Talon(0)
        self.leftRear = wpilib.Talon(1)
        self.rightFront = wpilib.Talon(2)
        self.rightRear = wpilib.Talon(3)

        self.rightFront.setInverted(True)
        self.rightRear.setInverted(True)

        self.drive = wpilib.drive.MecanumDrive(self.leftFront, self.leftRear, self.rightFront, self.rightRear)
        
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
        self.drive.drivePolar(self.stick.getMagnitude(), self.stick.getDirectionDegrees(), self.stick.getTwist())
        # print(self.stick.getMagnitude())
        
        # self.drive.driveCartesian(self.stick.getY(),self.stick.getX(),self.stick.getZ(),0)

if __name__ == "__main__":
    wpilib.run(MyRobot)