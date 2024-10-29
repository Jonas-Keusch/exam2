class Students:
    def __init__(self,studentId,name,score):
        self.studentId = studentId
        self.name = name
        self.score = score
    def __str__(self):
        return (f"ID: {self.studentId}, Name: {self.name}, Score:{self.score}")
    
    @staticmethod
    def addStudent(studentsList,student):
        studentsList.append(student)
        print(f"Added: {student}")

    @staticmethod
    def sort(studentList):  
        studentList.sort(key=lambda student: student.score, reverse=True)

    @staticmethod
    def searchStudent(studentsList,studentId):
        for student in studentsList:
            if student.studentId == studentId:
                return str(student)
        return("Student not found.")

    @staticmethod
    def showStudents(studentList):
        for Students in studentList:
            print(Students)

studentList = []

Students.addStudent(studentList, Students(1,"Jonas", 100))
Students.addStudent(studentList, Students(2,"Jose", 98))
Students.addStudent(studentList, Students(3,"Amadeo", 99))

Students.showStudents(studentList)

Students.sort(studentList)

Students.showStudents(studentList)

print(Students.searchStudent(studentList, 2))

print(Students.searchStudent(studentList, 4))


