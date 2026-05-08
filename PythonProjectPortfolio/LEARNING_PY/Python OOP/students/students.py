

class student:
    def __init__ (self, Class, hr_teacher, student_id, is_in_honors, major):
        self.class_name = Class
        self.hr_teacher = hr_teacher
        self.student_id = student_id
        self.is_in_honors = is_in_honors
        self.major = major

    def declare_class(self):
        if self.class_name == 2029:
            self.level = "freshman"
        elif self.class_name == 2028:
            self.level = "sophomore"
        elif self.class_name == 2027:
            self.level = "junior"
        elif self.class_name == 2026:
            self.level = "senior"

print("Enter student data - (student_name,Class,hr_teacher,student_id,is_in_honors,major)")
data = input("")
        
data = data.split(",")

name = data[0]

