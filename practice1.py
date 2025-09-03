# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius * self.radius
#     def perimeter(self):
#         return 2 * 3.14 * self.radius

# c1=Circle(10)
# print(c1.area())
# print(c1.perimeter())

class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
    def show_details(self):
        print("Role:", self.role)
        print("Department:", self.department)
        print("Salary:", self.salary)

class Engineer(Employee):
    def __init__(self, name , age):
        self.name = name
        self.age = age
        super().__init__("Developer", "Engineering", 60000)

e1= Employee("Manager", "Sales", 75000)
e1.show_details()
e2= Engineer("Alice", 30)
e2.show_details()