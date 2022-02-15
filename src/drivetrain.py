import wpilib
import wpilib.drive
import wpilib.interfaces


class DriveTrain:
    def __init__(self, leftFront: wpilib.interfaces.MotorController, leftRear: wpilib.interfaces.MotorController, rightFront: wpilib.interfaces.MotorController, rightRear: wpilib.interfaces.MotorController) -> None:
        self.leftFront = leftFront
        self.leftRear = leftRear
        self.rightFront = rightFront
        self.rightRear = rightRear

    def drive(self, Joystick: wpilib.Joystick, deadzone_threashold: float = 0) -> None:
        print("THIS SHOULD BE REPLACED!")

    def rightInverted(self, isInverted: bool) -> None:
        self.rightFront.setInverted(isInverted)
        self.rightRear.setInverted(isInverted)

    def leftInverted(self, isInverted: bool) -> None:
        self.leftFront.setInverted(isInverted)
        self.leftRear.setInverted(isInverted)


class MecanumDrive(DriveTrain):
    def __init__(self, leftFront: wpilib.interfaces.MotorController, leftRear: wpilib.interfaces.MotorController, rightFront: wpilib.interfaces.MotorController, rightRear: wpilib.interfaces.MotorController) -> None:
        # run the parent's __init__ function
        super().__init__(leftFront, leftRear, rightFront, rightRear)
        self.MecanumDrive = wpilib.drive.MecanumDrive(
            self.leftFront, self.leftRear, self.rightFront, self.rightRear)  # create a mecanum drive object

    # drive using this drivetrain
    def drive(self, Joystick: wpilib.Joystick, deadzone_threashold: float = 0) -> None:
        mag = Joystick.getMagnitude()
        angle = Joystick.getDirectionDegrees()
        rotate = Joystick.getTwist()
        if mag < deadzone_threashold:
            mag = 0
        if abs(rotate) < deadzone_threashold:  # absolute value b/c rotate goes from -1 to 1
            rotate = 0
        self.MecanumDrive.drivePolar(
            mag, angle, rotate)  # drive using joystick
