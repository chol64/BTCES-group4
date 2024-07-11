class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.classes = []

    def assign_class(self, class_obj):
        self.classes.append(class_obj)

class Teacher:
    def __init__(self, teacher_id, name):
        self.teacher_id = teacher_id
        self.name = name
        self.classes = []

    def assign_class(self, class_obj):
        self.classes.append(class_obj)

class Class:
    def __init__(self, class_id, class_name):
        self.class_id = class_id
        self.class_name = class_name
        self.students = []
        self.teacher = None

    def add_student(self, student):
        self.students.append(student)

    def set_teacher(self, teacher):
        self.teacher = teacher

class School:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.classes = []

    def register_student(self, student_id, name):
        student = Student(student_id, name)
        self.students.append(student)
        return student

    def register_teacher(self, teacher_id, name):
        teacher = Teacher(teacher_id, name)
        self.teachers.append(teacher)
        return teacher

    def create_class(self, class_id, class_name):
        class_obj = Class(class_id, class_name)
        self.classes.append(class_obj)
        return class_obj

    def assign_student_to_class(self, student, class_obj):
        class_obj.add_student(student)
        student.assign_class(class_obj)

    def assign_teacher_to_class(self, teacher, class_obj):
        class_obj.set_teacher(teacher)
        teacher.assign_class(class_obj)

    def track_attendance(self, class_obj):
        return {student.name: "Present" for student in class_obj.students}

    def track_performance(self, student):
        return {class_obj.class_name: "Performance Data" for class_obj in student.classes}
# Your existing classes and code

if __name__ == "__main__":
     print("School Management System script executed successfully.")
