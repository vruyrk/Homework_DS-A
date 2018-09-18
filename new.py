import hashlib

class User:
    def __init__(self, first_name, last_name, ID, mail, password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__ID = ID
        self.__mail = mail
        self.__password = password

    def setFirstName(self, name):
        if name != "":
            return self.__first_name

    def setLastName(self, name):
        if name != "":
            return self.__last_name

    def setID(self, ID):
        if ID != "":
            return self.__ID

    def setmail(self, mail):
        if mail != "":
            return self.__mail

    def setPassword(self, password):
        if password != "":
            encoder = hashlib.sha224(password.encode('utf-8')).hexdigest()
            print("Hi " + self.__first_name + " " + self.__last_name)
            self.__password = encoder
            return self.__password

    def getFirstName(self):
        return self.__first_name

    def getLastName(self):
        return self.__last_name

    def getID(self):
        return self.__ID

    def getmail(self):
        return self.__mail

    def getPassword(self):
        return self.__password

class Student(User):
    def __init__(self, first_name, last_name, ID, mail, password):
        super(User, self).__init__(first_name, last_name, ID, mail, password)
        self.courses = []
        self.grades = []

    def displayInfo(self):
        print("ID: " + self.getID())
        print("Mail: " + self.getmail())

        courses_list = []
        for course in self.courses:
            courses_list.append(course.name)
            print (course.name)

        for i, course in enumerate(courses_list):
            print("Assignments and grades for " + course + " are: ")
            if self.courses[i].assignments != []:
                for grade in self.grades:
                    print grade.course.name + ": " + grade.assignment.name + ": " + str(grade.grade.mark)
            else:
                print("There are not any assignments yet!")


class Course:
    def __init__(self, name, ID, credit, lecturer):
        self.name = name
        self.ID = ID
        self.credit = credit
        self.lecturer = lecturer
        self.assignments = []

    def setName(self, name):
        if name != "":
            return self.name

    def setID(self, ID):
        if ID != "":
            return self.ID

    def setCredit(self, credit):
        if credit != "":
            return self.credit

    def setLecturer(self, lecturer_name):
        if lecturer_name != "":
            return self.lecturer

    def getName(self):
        return self.name

    def getID(self):
        return self.ID

    def getCredit(self):
        return self.credit

    def getLecturer(self):
        return self.lecturer

class Assignment:
    __min = 0
    __max = 100

    def __init__(self, name, deadline, description):
        self.name = name
        self.deadline = deadline
        self.description = description

    def setName(self, name):
        if name != "":
            return self.name

    def setDeadline(self, deadline):
        if deadline != "":
            return self.deadline

    def setDescription(self, description):
        if description != "":
            return self.description

    def getName(self):
        return self.name

    def getDeadline(self):
        return self.deadline

    def getDescription(self):
        return self.description

class Lecturer(User):
    def __init__(self, first_name, last_name, ID, mail, password):
        super(User, self).__init__(first_name, last_name, ID, mail, password)
        self.courses = []

    def getCourses(self):
        return self.courses

class AssignmentGrade:
    def __init__(self, course, assignment, percentage, grade):
        self.course = course
        self.assignment = assignment
        self.percentage = percentage
        self.grade = Grade(grade)

    def setPercentage(self, percentage):
        if percentage != "":
            return self.percentage

    def getPercentage(self):
        return self.percentage

class Grade:
    __min = 0
    __max = 100

    def __init__(self, grade):
        self.__grade = grade

    def setGrade(self, grade):
        while grade == "" or grade < Grade.__min or grade > Grade.__max:
            grade = int(input("PLease input a number between 0 and 100! "))
        self.__grade = grade
        return True

    def getGrade(self):
        return self.__grade

def main():
    student = Student("Vruyr", "Kocharyan", "A09170296", "vruyr_kocharyan@edu.aua.am", "12345678")
    student.setFirstName(student.getFirstName())
    student.setLastName(student.getLastName())
    student.setID(student.getID())
    student.setmail(student.getmail())
    student.setPassword(student.getPassword())

    course = Course("Data Structures and Algorithms", "ENGS115", 3, "Satenik")
    course.setName(course.getName())
    course.setID(course.getID())
    course.setCredit(course.getCredit())
    course.setLecturer(course.getLecturer())

    assignment1 = Assignment("Assignment1", "03.09.2018", "MacBook Pro Technical Specifications")
    assignment1.setName(assignment1.getName())
    assignment1.setDeadline(assignment1.getDeadline())
    assignment1.setDescription(assignment1.getDescription())

    assignment2 = Assignment("Assignment2", "03.09.2018", "Program 2 breakdown")
    assignment2.setName(assignment1.getName())
    assignment2.setDeadline(assignment1.getDeadline())
    assignment2.setDescription(assignment1.getDescription())

    assignment3 = Assignment("Assignment3", "2018-09-16", "Grade Calculator")
    assignment3.setName(assignment1.getName())
    assignment3.setDeadline(assignment1.getDeadline())
    assignment3.setDescription(assignment1.getDescription())

    course.assignments.append(assignment1)
    course.assignments.append(assignment2)
    course.assignments.append(assignment3)

    student.courses.append(course)

    assignment1_grade = AssignmentGrade(course, assignment1, 40, 100)
    assignment1_grade.setPercentage(assignment1_grade.getPercentage())

    assignment2_grade = AssignmentGrade(course, assignment2, 30, 100)
    assignment2_grade.setPercentage(assignment2_grade.getPercentage())

    assignment3_grade = AssignmentGrade(course, assignment3, 30, 100)
    assignment3_grade.setPercentage(assignment3_grade.getPercentage())

    if assignment1_grade.grade.setGrade(assignment1_grade.grade.getGrade()) == True \
            and assignment2_grade.grade.setGrade(assignment2_grade.grade.getGrade()) == True \
            and assignment3_grade.grade.setGrade(assignment3_grade.grade.getGrade()) == True:
        student.grades.append(assignment1_grade)
        student.grades.append(assignment2_grade)
        student.grades.append(assignment3_grade)

    student.displayInfo()

main()