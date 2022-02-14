import wpilib
import wpilib.drive

class DriveTrain:
    def __init__(self,leftFront: wpilib.PWMMotorController,leftRear: wpilib.PWMMotorController,rightFront: wpilib.PWMMotorController,rightRear: wpilib.PWMMotorController) -> None:
        self.leftFront = leftFront
        self.leftRear = leftRear
        self.rightFront = rightFront
        self.rightRear = rightRear
    def drive(self,Joystick: wpilib.Joystick) -> None:
        print("THIS SHOULD BE REPLACED!")
    def rightInverted(self, isInverted: bool) -> None:
        self.rightFront.setInverted(isInverted)
        self.rightRear.setInverted(isInverted)
    def leftInverted(self, isInverted: bool) -> None:
        self.leftFront.setInverted(isInverted)
        self.leftRear.setInverted(isInverted)
    
class MecanumDrive(DriveTrain):
    def __init__(self, leftFront: wpilib.PWMMotorController, leftRear: wpilib.PWMMotorController, rightFront: wpilib.PWMMotorController, rightRear: wpilib.PWMMotorController) -> None:
        super().__init__(leftFront, leftRear, rightFront, rightRear) # run the parent's __init__ function
        self.MecanumDrive = wpilib.drive.MecanumDrive(self.leftFront, self.leftRear, self.rightFront, self.rightRear) # create a mecanum drive object
    def drive(self, Joystick: wpilib.Joystick) -> None: # drive using this drivetrain
        self.MecanumDrive.drivePolar(Joystick.getMagnitude(), Joystick.getDirectionDegrees(), Joystick.getTwist()) # drive using joystick
    
