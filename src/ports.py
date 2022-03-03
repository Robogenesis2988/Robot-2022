class MotorPorts():
    # Drivetrain motors
    LEFT_FRONT = 0
    LEFT_REAR = 1
    RIGHT_FRONT = 2
    RIGHT_REAR = 3

    # Winch motors
    LEFT_WINCH = 4
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
