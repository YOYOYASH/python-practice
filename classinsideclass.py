class Student:

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.lap = self.Laptop()

    def show(self):
        print(f'The student name is {self.name} and their roll no. is {self.roll_no}')
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'Acer'
            self.cpu = 'i5 8th gen'
            self.ram = 16

        def show(self):
            print(f'{self.brand} laptop with {self.cpu} cpu and {self.ram}gb of ram')


s1 = Student('Yash', 54)

s1.show()

