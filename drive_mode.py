# We'll use inheritance to extend the DriveMode class such that the 3 child classes will inherit from DriveMode, but will have their own implementations of ther methods.
# We'll use the speed and fuel methods to for the 3 extended classes, and print out a message related to the specific driver mode selected. The 3 all have different behaviours but have access to the base class methods

class DriveMode:
    def __init__(self, mode_type):
        ## constructor intializing the mode type
        self.mode_type = mode_type

    def speeds(self, speed):
        print(f"Speeds in {self.mode_type} are: {speed}")


class ECOMode(DriveMode):
    def __init__(self):
        super().__init__("ECO Mode")

    def speeds(self, speed):
        super().speeds(speed)
        print("ECO mode limits top speed for energy efficiency.")


## Pass the speeds here
if __name__ == "__main__":
    eco_mode = ECOMode()
    eco_mode.speeds(30)

