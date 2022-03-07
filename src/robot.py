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
        self.solenoidClimb1 = pneumatics.DoubleSolenoid(
            *ports.PneumaticPorts.CLIMB1)
        self.solenoidClimb2 = pneumatics.DoubleSolenoid(
            *ports.PneumaticPorts.CLIMB2)

        self.leftFront = wpilib.Talon(ports.MotorPorts.LEFT_FRONT)
        self.leftRear = wpilib.Talon(ports.MotorPorts.LEFT_REAR)
        self.rightFront = wpilib.Talon(ports.MotorPorts.RIGHT_FRONT)
        self.rightRear = wpilib.Talon(ports.MotorPorts.RIGHT_REAR)

        self.leftWinchMotor = wpilib.Talon(ports.MotorPorts.LEFT_WINCH)
        self.rightWinchMotor = wpilib.Spark(ports.MotorPorts.RIGHT_WINCH)
        # self.rightWinchMotor.setInverted(True)

        self.leftWinch = winch.Winch(self.leftWinchMotor)
        self.rightWinch = winch.Winch(self.rightWinchMotor)

        # self.drive = wpilib.drive.MecanumDrive(self.leftFront, self.leftRear, self.rightFront, self.rightRear)

        self.drivetrain = drivetrain.MecanumDrive(
            self.leftFront, self.leftRear, self.rightFront, self.rightRear)
        self.drivetrain.rightInverted(True)
        self.drivetrain.setDeadzone(0.5, 0.5)
        self.drivetrain.speedMultiplier = 0.75
        self.drivetrain.twistMultiplier = 0.75

        # self.rightFront.setInverted(True)
        # self.rightRear.setInverted(True)

        self.stick = wpilib.Joystick(ports.JoystickPorts.JOY)

        self.timer = wpilib.Timer()

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()
        # autonomous.autonomousInit()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        if self.timer.get() < 2.5:
            self.drivetrain.moveRobot(0.3, 0, 0)
        elif self.timer.get() > 2.5 and self.timer.get() < (2.5+2.5):
            self.solenoidDump.open()
            self.drivetrain.moveRobot(0.3, 180, 0)
        else:
            self.drivetrain.moveRobot(0, 0, 0)

        # if self.timer.get() < 3:
        #     # drives foward for one second at 1/4 speed
        #     self.drivetrain.moveRobot(.25, 0, 0)
        # elif (self.timer.get() > 3) and (self.timer.get() < 6):
        #     # from 1 - 4 seconds the solenoid extends
        #     self.solenoidDump.open()
        # # if self.solenoid1.get() == self.solenoid1.Value.kOff:
        #     # self.solenoid1.set(self.solenoid1.Value.kForward)
        # elif (self.timer.get() > 6) and (self.timer.get() < 8):
        #     self.solenoidDump.close()
        # elif (self.timer.get() > 8) and (self.timer.get() < 10):
        #     self.drivetrain.moveRobot(-.25, 0, 0)
        # elif (self.timer.get() > 10) and (self.timer.get() < 12):
        #     self.drivetrain.moveRobot(0, 0, .72)
        # if self.timer.get() < 1.0:
        #     # Drive forwards at half speeds
        #     self.drivetrain.moveRobot(1, 90, 0)
        # else:
        #     self.drivetrain.moveRobot(0, 0, 0)
        # autonomous.autonomousPeriodic(self.drivetrain)

    def teleopInit(self) -> None:
        self.timer.reset()
        self.timer.start()

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""

        # Test code
        # self.timer.reset()
        # self.timer.start()
        # self.drivetrain.motorTest(self.timer)

        # Toggle pistons on button 3
        if self.stick.getRawButtonPressed(ports.JoystickButtons.DUMPTOGGLE):
            self.solenoidDump.toggle()

        if self.stick.getRawButtonPressed(ports.JoystickButtons.CLIMBPISTONTOGGLE):
            self.solenoidClimb1.toggle()
            self.solenoidClimb2.toggle()

        # Toggle speed multiplier on button 2
        if self.stick.getRawButtonPressed(ports.JoystickButtons.SPEEDMULTIPLIER):
            if self.drivetrain.speedMultiplier == 0.75:
                self.drivetrain.speedMultiplier = 0.5
            else:
                self.drivetrain.speedMultiplier = 0.75

        # Button 4 hold -> climber down
        # if self.stick.getRawButton(ports.JoystickButtons.WINCHRETRACT):
        #     self.leftWinch.winchRetract()
        #     self.rightWinch.winchRetract()
        #     # self.leftWinchMotor.set(0.1)
        #     # self.rightWinchMotor.set(0.1)

        # # Button 6 hold -> climber up
        # elif self.stick.getRawButton(ports.JoystickButtons.WINCHEXTEND):
        #     self.leftWinch.winchExtend()
        #     self.rightWinch.winchExtend()
            # print("go!")
            # self.leftWinchMotor.set(0.1)
            # self.solenoidDump.open()
            # self.rightWinchMotor.set(-0.1)
        if self.stick.getRawButton(7):
            self.leftWinch.winchExtend()
        elif self.stick.getRawButton(9):
            self.leftWinch.winchRetract()
        else:
            self.leftWinch.winchStop()

        if self.stick.getRawButton(8):
            self.rightWinch.winchExtend()
        elif self.stick.getRawButton(10):
            self.rightWinch.winchRetract()
        else:
            self.rightWinch.winchStop()
            # self.rightWinch.winchStop()
            # self.leftWinchMotor.set(0)
            # self.rightWinchMotor.set(0)

        self.drivetrain.drive(self.stick)


if __name__ == "__main__":
    wpilib.run(Robot)
