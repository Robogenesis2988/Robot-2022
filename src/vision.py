from cscore import CameraServer #need to install cscore, it is on the readthedocs

def main():
    cs = CameraServer.getInstance()
    cs.enableLogging()

    usb1 = cs.startAutomaticCapture(dev=0)
    usb2 = cs.startAutomaticCapture(dev=1)
    #two camera streaming to the FRC dashboard program
    #This needs collaboration with Hardware to test

    cs.waitForever()