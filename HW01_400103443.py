# AP-HW01 Hossein Shadman 400103443

#Class
class Animal:
    def __init__(self,name,age,gender,breed,color):
        self.name = name
        self.age = age
        self.gender = gender
        self.breed = breed
        self.color = color
        
    def namedescription(self):
        return f"my name is {self.name}"
    
    def agedescription(self):
        return f"I am {self.age}"
    
    def genderdescription(self):
        return f"my gender is {self.gender}"
    
    def breeddescription(self):
        return f"my breed is {self.breed}"
    
    def colordescription(self):
        return f"my color is {self.color}"