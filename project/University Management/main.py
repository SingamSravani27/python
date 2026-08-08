class Person:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id


class Student(Person):

    def __init__(self, name, age, id, dept):
        super().__init__(name, age, id)
        self.dept = dept
    def get_percentage(marks):
        return 

class Employee(Person):
    def __init__(self, name, age, id, dept,salary,subject):
        super().__init__(name, age, id, dept)
        self.salary = salary
        self.subject = subject
        add bonus
    
class University(Student, Employee):

    def __init__(self, uni_name):
        self.uni_name = uni_name
        self.courses = ["B.Tech", "M.Tech"]
        self.student_data = {}
        self.employee_data = {}
        add_sudent(n a dep)
        id=len(stud_dt)+1
        std_obj=stuend(n,,id,dep)
        id:std_obj
        remove_std(stdid)
        add empolyye
        remove empoee
        seacch studnet
        search emoplyee