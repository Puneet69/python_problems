class Student:
    def __init__(self,name,subjects_marks):
        self.name=name
        self.subjects_marks=subjects_marks
    def average(self):
        # print("Average marks of",self.name,"is",sum(self.subjects_marks.values())/len(self.subjects_marks))
        sum=0
        for marks in self.subjects_marks.values():
            sum+=marks
        print("Average marks of",self.name,"is",sum/len(self.subjects_marks))
    @staticmethod
    def college():
        print("I am from Maharshi Dayanand University")

s1=Student("Puneet Gupta",{"Maths":50,"Science":90,"English":90})
s1.average()
Student.college()