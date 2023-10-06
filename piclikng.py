import pickle


class Student:
    def __init__(self, name, roll, address):
        self.name = name
        self.roll = roll
        self.address = address

    def show(self):
        print(f'Student name is {self.name}, with roll no. {self.roll} and address {self.address}')


with open('student.bat', mode='wb') as f:
    st1 = Student('Yash', 54, 'Gorakhpur')
    pickle.dump(st1, f)
    print("Pickling done")
