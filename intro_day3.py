
class Student(object):
    """
    This is a blueprint for the student demographic data
    """
    
    def __init__(self, firstname, lastname, student_number):
        self.student_firstname =  firstname
        self.student_lastname = lastname
        self.student_number = int(student_number)

    def __repr__(self):

        return "{} {}".format(self.student_firstname, self.student_lastname)

  
class Course(object):
    """
    This is ablueprint for course information
    """
    def __init__(self, course_name, course_code, lecturer_name):
        self.course_name = course_name
        self.course_code = course_code
        self.lecturer_name = lecturer_name

    def __repr__(self):
        return "{} {}".format(self.course_name, self.lecturer_name)
    
student_object = Student("Thapelo", "Seletisha", "1234567")
course_object = Course("Linear Algebra", "MATH2025", "Zellenyik")




