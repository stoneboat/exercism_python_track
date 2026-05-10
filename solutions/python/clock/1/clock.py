class Clock:
    def __init__(self, hour, minute):
        modulus = minute // 60
        self.minute = minute % 60
        self.hour = (hour+modulus) % 24

    def __repr__(self):
        # "Clock(6, 45)"
        return "Clock(" + str(self.hour) + ", " + str(self.minute) + ")"

    def __str__(self):
        string = f"{self.hour:02}" + ":" + f"{self.minute:02}"
        return string

    def __eq__(self, other):
        if self.minute == other.minute and self.hour == other.hour:
            return True
        
        return False

    def __add__(self, minutes):
        modulus = (self.minute + minutes) // 60
        self.minute = (self.minute + minutes) % 60
        self.hour = (self.hour+modulus) % 24
        return self

    def __sub__(self, minutes):
        return self.__add__(-minutes)
