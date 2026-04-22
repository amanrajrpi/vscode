# OOP
# 1. Class - blueprint that contains properties/attributes & behaviors/methods.
# 2. Object - instance of a class that consume storage.
class Student:
    college = "MSRIT"
    total_count = 0
    # Constructor
    def __init__(self, name, age, branch, subject, cgpa):
        self.name = name
        self.age = age
        self.branch = branch
        self.subject = subject
        self.cgpa = cgpa
        Student.total_count += 1    # common attribute among objects
        print(f"{self.name} enrolled successfully")
    
    # Instance methods
    def getDetails(self):
        return [self.name, self.age, self.college, self.branch, self.subject, self.cgpa]
    
    # Class methods (only access class attributes and methods)
    @classmethod
    def getCollege(cls):
        return cls.college
    @classmethod
    def getTotalStudentCount(cls):
        return cls.total_count
    
    # Static methods (can't access class or instance attributes or methods)
    @staticmethod
    def getFee(year):
        if(year==1 or year==2):
            return 100000
        else:
            return 200000
    
s1 = Student("Aman",24,"CSE",["Maths","Java","Python"],9.8)
s2 = Student("Raj",22,"ISE",["HTML","CSS","JS"],9.2)

print(s1.getDetails())
print(s1.getTotalStudentCount())
print(s2.getCollege())
print(s2.getFee(4))