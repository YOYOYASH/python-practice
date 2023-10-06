class Computer:
    type = 'laptop'

    def __init__(self, processor, ram):
        self.processor = processor
        self.ram = ram

    def config(self):
        print(f'This computer runs on {self.processor} with {self.ram}gb of ram')

    def compare(self, other):
        if self.processor == other.processor:
            return True
        else:
            return False

    @classmethod
    def info(cls):
        return cls.type


com1 = Computer('i5 12th gen', 16)
com2 = Computer('Ryzen5 5600x', 16)

com1.config()
com2.config()

if com1.compare(com2):
    print("Same processor")
else:
    print("Different processor")

print(Computer.info())
