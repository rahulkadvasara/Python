class Teacher:
    def teacher_action(self):
        print("I can teach")

class Engineer:
    def engineer_action(self):
        print("I can code")

class Youtuber:
    def youtuber_action(self):
        print("I can code and teach")

class Person(Teacher,Engineer,Youtuber):
    pass

coder=Person()
coder.teacher_action()
coder.engineer_action()
coder.youtuber_action()
