#!/usr/bin/env python3
"""
    This is a good foundation to build your robot code on
"""

import wpilib
import wpilib.drive

import drivetrain as drivetrain


class Robot(wpilib.TimedRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """

        self.solenoidDump = wpilib.DoubleSolenoid(
            wpilib.PneumaticsModuleType.CTREPCM, 1, 0)
        self.solenoid2 = wpilib.DoubleSolenoid(
            wpilib.PneumaticsModuleType.CTREPCM, 3, 2)
        self.solenoid3 = wpilib.DoubleSolenoid(
            wpilib.PneumaticsModuleType.CTREPCM, 5, 4)

        self.leftFront = wpilib.Talon(0)
        self.leftRear = wpilib.Talon(1)
        self.rightFront = wpilib.Talon(2)
        self.rightRear = wpilib.Talon(3)

        # self.drive = wpilib.drive.MecanumDrive(self.leftFront, self.leftRear, self.rightFront, self.rightRear)

        self.drivetrain = drivetrain.MecanumDrive(
            self.leftFront, self.leftRear, self.rightFront, self.rightRear)
        self.drivetrain.rightInverted(True)
        self.drivetrain.setDeadzone(0.2, 0.2)

        # self.rightFront.setInverted(True)
        # self.rightRear.setInverted(True)

        self.stick = wpilib.Joystick(0)

        self.timer = wpilib.Timer()

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        # Drive for two seconds
        if self.timer.get() < 1.0:
            # Drive forwards at half speed
            self.drivetrain.moveRobot(1, 90, 0)
        else:
            self.drivetrain.moveRobot(0, 0, 0)

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.drive.driveCartesian(self.stick.getY(), self.stick.getX())

        # Toggle pistons on button 3
        if self.stick.getRawButtonPressed(3):
            self.solenoidDump.toggle()
            if self.solenoidDump.get() == self.solenoidDump.Value.kOff:
                self.solenoidDump.set(self.solenoidDump.Value.kForward)

        # Toggel speed multiplier on button 2
        if self.stick.getRawButtonPressed(2):
            if self.drivetrain.speedMultiplier == 1:
                self.drivetrain.speedMultiplier = 0.5
            else:
                self.drivetrain.speedMultiplier = 1

        self.drivetrain.drive(self.stick)


if __name__ == "__main__":
    wpilib.run(Robot)
