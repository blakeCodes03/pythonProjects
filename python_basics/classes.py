# python inheritance classes
class Student:
    def __init__(self, Firstname, Level, age ):
        self.name = Firstname
        self.Email = f'{Firstname}{Level}@gmail.com'.lower()
        self.Level = Level
        self.age =  age

    def printDetails(self):
            print(self.name + "\n", self.Email + "\n", self.Level, self.age)
p1 = Student("Okafor",  300, 19)
p1.printDetails()


class Teacher(Student):
    def __init__(self, Firstname, Level, age, year):
        super().__init__(Firstname, Level, age)
        self.retirementYear = year
    def welcome(self):
        print(self.name, "nice having you with us but you retire in", self.retirementYear) 
t1 = Teacher("Issac Nephtha", 14, 54, 2045).welcome()
t2 = Teacher("Jordan Whithers", 7, 32, 2073).welcome()
t3 = Teacher("Francis Rivers", 14, 54, 2045).welcome()
t4 = Teacher("Jason Bourne", 14, 54, 2045).welcome()
t1.printDetails()

