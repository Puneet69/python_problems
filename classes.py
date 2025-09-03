class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def Welcome(self):
        print("Welcome",self.name)
        print("Your marks are",self.marks)
s1=Student("Puneet Gupta",85)
s1.Welcome()