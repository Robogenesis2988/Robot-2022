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
        if self.timer.get() < 1:
            self.drive.drivePolar(.25,0,0) #drives foward for one second at 1/4 speed
        elif (self.timer.get() > 1) & (self.timer.get() < 4):
            self.solenoidDump.set(self.solenoidDump.Value.kForward) #from 1 - 4 seconds the solenoid extends 
        elif (self.timer.get() > 4) & (self.timer.get() < 6):
            self.solenoidDump.set(self.solenoidDump.Value.kReverse) #from 4-6 seconds the solenoid retracts
        elif (self.timer.get() > 6) & (self.timer.get() < 8):
            self.drive.drivePolar(0,0,.72) #The robot does a 180 turn in 2 seconds

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.drive.driveCartesian(self.stick.getY(), self.stick.getX())
        if self.stick.getRawButtonPressed(2): 
            self.solenoidDump.toggle()
            if self.solenoidDump.get() == self.solenoidDump.Value.kOff:
                self.solenoidDump.set(self.solenoidDump.Value.kForward)


if __name__ == "__main__":
    wpilib.run(MyRobot)