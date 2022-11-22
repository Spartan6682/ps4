# Script to practice creating a class and
# using class functions

import datetime

class Person(object):

    def __init__(self, name):
        # Create an object of the class person
        self.name = name
        try:
            lastBlank = name.index(' ')
            self.lastName = name[lastBlank + 1:]
        except:
            self.lastName = name
        self.birthday = None
    
    def getName(self):
        # Returns self's full name
        return self.name
    
    def getLastName(self):
        # Returns self's last name
        return self.lastName
    
    def setBirthday(self, birthdate):
        """Assumes birthdate is of type datetime.date
           Sets self's birthday to birthdate"""
        self.birthday = birthdate

    def getAge(self):
        """Returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    
    def __lt__(self, other):
        """Returns True if self precedes other in alphabetical
           order, and False otherwise. Comparison is based on last
           names, but if these are the same full names are
           compared."""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    
    def __str__(self):
        """Returns self's name"""
        return self.name

class MITPerson(Person):

    nextIdNum = 0 # identification number

    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum
    
    def isStudent(self):
        return isinstance(self, Student)
    
    def __lt__(self, other):
        return self.idNum < other.idNum
    
class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year
    
class Grad(Student):
    pass

me = Person('Joel Calvert')
him = Person('Barrack Hussein Obama')
her = Person('Madonna')
print(him.getLastName())
him.setBirthday(datetime.date(1961, 8, 4))
her.setBirthday(datetime.date(1958, 8, 16))
print(him.getName(), 'is', him.getAge(), 'days old!')

p1 = MITPerson('Barbara Beaver')
print(str(p1) + '\'s id number is ' + str(p1.getIdNum()))

p1 = MITPerson('Mark Guttag')
p2 = MITPerson('Billy Bob Beaver')
p3 = MITPerson('Billy Bob Beaver')
p4 = Person('Billy Bob Beaver')

print('p1 < p2 = ', p1 < p2)
print('p3 < p2 =', p3 < p2)
print('p4 < p1 = ', p4 < p1)

p5 = Grad('Buzz Aldrin')
p6 = UG('Billy Beaver', 1984)
print(p5, 'is a graduate student is', type(p5) == Grad)
print(p5, 'is an undergraduate student is', type(p5) == UG)