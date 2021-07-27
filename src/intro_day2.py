"""
Student
 - First name
 - Last name
 - Student number

Course
 - Course name
 - Course code  
 
Assessment
 - Questions 10
 - Marks
 - Date
 - Lecturer
 - Answers 10

 Exam: Student, Course and Assessment


"""

class Student(object):
    """
    This is a blueprint for the student demographic data
    """
    
    def __init__(self, student_firstname, student_lastname,student_number):
        self.student_firstname =  student_firstname
        self.student_lastname = student_lastname
        self.student_number = int(student_number)


    def print_demographic(self):
        """
        This is the function that returns students demographic data
        """

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


# student_1 = Student("Thapelo", "Seletisha", "1234567")
# student_demo_1 = student_1.print_demographic()
# print(student_demo_1)


# student_2 = Student("Teboho", "Molise", "24681012")
# student_demo_2 = student_2.print_demographic()
# print(student_demo_2)


course_object = Course("Maths", "MATH123")
c =course_object.print_information()
print(c)