# We'll use inheritance to extend the DriveMode class such that the 3 child classes will inherit from DriveMode, but will have their own implementations of ther methods.
# We'll use the speed and fuel methods to for the 3 extended classes, and print out a message related to the specific driver mode selected. The 3 all have different behaviours but have access to the base class methods

class DriveMode:
    def __init__(self, mode_type):
        ## constructor intializing the mode type
        self.mode_type = mode_type
        print(f"%%%%%Switching modes. You are currently in {self.mode_type}%%%%%%")

    def speeds(self, speed):
        print(f"Speeds in {self.mode_type} are: {speed}")

    def fuel(self, fuel_consumption):
        print(f"Fuel consumption in {self.mode_type} is: {fuel_consumption}")    


class ECOMode(DriveMode):
    ## This is an additional class representing the ECO mode. It inherits from DriveMode, and overides the speed and fuel_consumption methods providing its own implemetation
    def __init__(self):
        super().__init__("ECO Mode")

    def speeds(self, speed):
        super().speeds(speed)
        print("ECO mode limits top speed for energy efficiency.")

    def fuel(self, fuel_consumption):
        super().fuel(fuel_consumption)
        print("ECO mode fuel consumption is pretty LOW")    


class SPORTMode(DriveMode):
    def __init__(self):
        super().__init__("SPORT Mode")

    def speeds(self, speed):
        super().speeds(speed)
        print("SPORT mode has very high speeds.")

    def fuel(self, fuel_consumption):
        super().fuel(fuel_consumption)
        print("SPORT mode fuel consumption is pretty HIGH")           
        

class OFFROADMode(DriveMode):
    def __init__(self):
        super().__init__("OFF-ROAD Mode")

    def speeds(self, speed):
        super().speeds(speed)
        print("OFF-ROAD mode has very low speeds.")

    def fuel(self, fuel_consumption):
        super().fuel(fuel_consumption)
        print("OFF-ROAD mode fuel consumption is MEDIUM")         


## Pass the speeds here
if __name__ == "__main__":
    eco_mode = ECOMode()
    eco_mode.speeds(30)
    eco_mode.fuel("LOW")


    sport_mode = SPORTMode()
    sport_mode.speeds(180)
    sport_mode.fuel("HIGH")

    sport_mode = OFFROADMode()
    sport_mode.speeds(15)
    sport_mode.fuel("MEDIUM")

