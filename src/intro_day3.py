
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


class Question(object):
    """
    This is a blueprint that stores the question and corresponding answer
    """

    def __init__(self, question_statement, correct_answer ):
        self.question_statement = question_statement
        self.correct_answer = correct_answer
    

    def __repr__(self):

        return "{} {}".format(self.question_statement, self.correct_answer)


    def get_ask_and_evaluate(self):
        """
        This method prints the question, accepts solution from the student 
        and returns True if the solution is correct else it returns False.
        """

        print(self.question_statement)
        user_solution =   input("")
        if user_solution == self.correct_answer:
            
            return True
        else:
            return False        

class Assessment(object):
    """
    This is ablue print for putting questions together to ask students
    """
    def __init__(self, title,date):
        self.title = title
        self.date = date
        self.question = list()
        self.mark = 0

    def __repr__(self):
        
        return " "

# student_object = Student("Thapelo", "Seletisha", "1234567")
# course_object = Course("Linear Algebra", "MATH2025", "Zellenyik")
question_object = Question("Was Mandela born on the 18th of July 1950?", "False")
question_1 =  question_object.get_ask_and_evaluate()
print(question_1)

