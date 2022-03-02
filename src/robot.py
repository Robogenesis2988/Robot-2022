#!/usr/bin/env python3
"""
    This is a good foundation to build your robot code on
"""

from enum import Enum
import wpilib
import wpilib.drive

# our code imports
import drivetrain
import pneumatics
import autonomous
import winch
import ports
from vision import cameraLaunch
import ports


class Robot(wpilib.TimedRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        cameraLaunch()
        # self.solenoidDump = wpilib.DoubleSolenoid(
        #     wpilib.PneumaticsModuleType.CTREPCM, 1, 0)
        # self.solenoid2 = wpilib.DoubleSolenoid(
        #     wpilib.PneumaticsModuleType.CTREPCM, 3, 2)
        # self.solenoid3 = wpilib.DoubleSolenoid(
        #     wpilib.PneumaticsModuleType.CTREPCM, 5, 4)

        self.solenoidDump = pneumatics.DoubleSolenoid(
            *ports.PneumaticPorts.DUMP)
        self.solenoid2 = pneumatics.DoubleSolenoid(
            *ports.PneumaticPorts.CLIMB1)
        self.solenoid3 = pneumatics.DoubleSolenoid(
            *ports.PneumaticPorts.CLIMB2)

        self.leftFront = wpilib.Talon(ports.MotorPorts.LEFT_FRONT)
        self.leftRear = wpilib.Talon(ports.MotorPorts.LEFT_REAR)
        self.rightFront = wpilib.Talon(ports.MotorPorts.RIGHT_FRONT)
        self.rightRear = wpilib.Talon(ports.MotorPorts.RIGHT_REAR)

        self.leftWinchMotor = wpilib.Spark(ports.MotorPorts.LEFT_WINCH)
        self.rightWinchMotor = wpilib.Talon(ports.MotorPorts.RIGHT_WINCH)

        self.leftWinch = winch.Winch(self.leftWinchMotor)
        self.rightWinch = winch.Winch(self.rightWinchMotor)

        # self.drive = wpilib.drive.MecanumDrive(self.leftFront, self.leftRear, self.rightFront, self.rightRear)

        self.drivetrain = drivetrain.MecanumDrive(
            self.leftFront, self.leftRear, self.rightFront, self.rightRear)
        self.drivetrain.rightInverted(True)
        self.drivetrain.setDeadzone(0.2, 0.2)

        # self.rightFront.setInverted(True)
        # self.rightRear.setInverted(True)

        self.stick = wpilib.Joystick(ports.JoystickPorts.JOY)

        self.timer = wpilib.Timer()

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        # self.timer.reset()
        # self.timer.start()
        autonomous.autonomousInit()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        # # Drive for two seconds
        # if self.timer.get() < 1.0:
        #     # Drive forwards at half speed
        #     self.drivetrain.moveRobot(1, 90, 0)
        # else:
        #     self.drivetrain.moveRobot(0, 0, 0)
        autonomous.autonomousPeriodic(self.drivetrain)

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""

        # Toggle pistons on button 3
        if self.stick.getRawButtonPressed(3):
            self.solenoidDump.toggle()

        # Toggle speed multiplier on button 2
        if self.stick.getRawButtonPressed(2):
            if self.drivetrain.speedMultiplier == 1:
                self.drivetrain.speedMultiplier = 0.5
            else:
                self.drivetrain.speedMultiplier = 1

        # Button 4 hold -> climber down
        if self.stick.getRawButton(4):
            self.leftWinch.winchRetract()
        # Button 6 hold -> climber up
        elif self.stick.getRawButton(6):
            self.leftWinch.winchExtend()
        else:
            self.leftWinch.winchStop()

        self.drivetrain.drive(self.stick)


if __name__ == "__main__":
    wpilib.run(Robot)
