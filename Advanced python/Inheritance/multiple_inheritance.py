class Father:
    def skills(self):
        print("Programming")

class Mother:
    def skills(self):
        print("Art")

class Child(Father,Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("Sports")

c=Child()
c.skills()