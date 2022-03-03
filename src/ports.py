class MotorPorts():
    # Drivetrain motors
    LEFT_FRONT = 1
    LEFT_REAR = 3
    RIGHT_FRONT = 0
    RIGHT_REAR = 2

    # Winch motors
    LEFT_WINCH = 5
    RIGHT_WINCH = 5


class PneumaticPorts():
    DUMP = (0, 1)
    CLIMB1 = (3, 2)
    CLIMB2 = (5, 4)

class JoystickPorts():
    JOY = 0 

class JoystickButtons():
    WINCHEXTEND = 6 
    WINCHRETRACT = 4
    CLIMBPISTONTOGGLE = 5 
    DUMPTOGGLE = 3 
    SPEEDMULTIPLIER = 2
