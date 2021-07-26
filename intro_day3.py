
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
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code
        self.assessments = list()

    def print_information(self):
        """
        This function returns course information
        """
        student_info = Student("Thapelo", "Seletisha", "1234567")
        student_demo_1 = student_info.print_demographic()

    

        return "{}".format( student_demo_1)

    def add_assesment(self, lecturer, date):
        """
        This allows lecturers to add assessments

        arg: 
            - lectuerer: this is lecturers name
            - date: this is the date  in format DD/MM/YYYY
        return: this function ....
        """
        pass

student_1 = Student("Thapelo", "Seletisha", "1234567")
print(student_1)



