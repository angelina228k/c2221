class Computer:
    def __init__(self):
        self.memory =128

class Display:
        def __init__(self):
            self.resolution ="4k"

class SmartPhone(Display, Computer):
                def print_info(self):
                    print (self.resolution)
                    print(self.memory)
                    iphone = SmartPhone()
                    iphone.print_info()

