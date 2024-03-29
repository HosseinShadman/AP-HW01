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
       
#Inheritance
class Invertebrate(Animal):
    def __init__(self, name, age, gender, breed, color, weight, length):
        super().__init__(name, age, gender, breed, color)
        self.weigh = weight
        self.length = length
        
    def weightdescription(self):
        return f"my weight is {self.weight}"
    
    def lengthdescription(self):
        return f"my length is {self.length}"
    
class Worm(Invertebrate):
    def __init__(self, name, age, gender, breed, color, weight, length, location):
        super().__init__(name, age, gender, breed, color, weight, length)
        self.location = location
        
    def locationdescription(self):
        return f"my location is {self.location}"
    
class Mollusc(Invertebrate):
    def __init__(self, name, age, gender, breed, color, weight, length, location):
        super().__init__(name, age, gender, breed, color, weight, length)
        self.location = location
        
    def locationdescription(self):
        return f"my location is {self.location}"

class Echinoderm(Invertebrate):
    def __init__(self, name, age, gender, breed, color, weight, length, location):
        super().__init__(name, age, gender, breed, color, weight, length)
        self.location = location
        
    def locationdescription(self):
        return f"my location is {self.location}"

class Arthropod(Invertebrate):
    def __init__(self, name, age, gender, breed, color, weight, length, location):
        super().__init__(name, age, gender, breed, color, weight, length)
        self.location = location
        
    def locationdescription(self):
        return f"my location is {self.location}"

#Inheritance
class Vertebrate(Animal):
    def __init__(self, name, age, gender, breed, color, weight, height):
        super().__init__(name, age, gender, breed, color)
        self.weigh = weight
        self.height = height
        
    def weightdescription(self):
        return f"my weight is {self.weight}"
    
    def heightdescription(self):
        return f"my height is {self.height}"

class Fish(Vertebrate):
    def __init__(self, name, age, gender, breed, color, weight, height, numberofvertebras):
        super().__init__(name, age, gender, breed, color, weight, height)
        self.numberofvertebras = numberofvertebras
        
    def numberofvertebrasdescription(self):
        return f"I have {self.numberofvertebras} vertebras"
    
class Bird(Vertebrate):
    def __init__(self, name, age, gender, breed, color, weight, height, numberofvertebras):
        super().__init__(name, age, gender, breed, color, weight, height)
        self.numberofvertebras = numberofvertebras
        
    def numberofvertebrasdescription(self):
        return f"I have {self.numberofvertebras} vertebras"

class Reptiles(Vertebrate):
    def __init__(self, name, age, gender, breed, color, weight, height, numberofvertebras):
        super().__init__(name, age, gender, breed, color, weight, height)
        self.numberofvertebras = numberofvertebras
        
    def numberofvertebrasdescription(self):
        return f"I have {self.numberofvertebras} vertebras"

class Amphibian(Vertebrate):
    def __init__(self, name, age, gender, breed, color, weight, height, numberofvertebras):
        super().__init__(name, age, gender, breed, color, weight, height)
        self.numberofvertebras = numberofvertebras
        
    def numberofvertebrasdescription(self):
        return f"I have {self.numberofvertebras} vertebras"
    
class Mammal(Vertebrate):
    def __init__(self, name, age, gender, breed, color, weight, height, numberofvertebras):
        super().__init__(name, age, gender, breed, color, weight, height)
        self.numberofvertebras = numberofvertebras
        
    def numberofvertebrasdescription(self):
        return f"I have {self.numberofvertebras} vertebras"
    
#Aggregation and Encapsulation
class Foot:
    def __init__(self, numberoffingers):
        self.numberoffingers = numberoffingers
        
    def display(self):
        return self.numberoffingers

class Human(Mammal):
    def __init__(self, name, age, gender, breed, color, weight, height, numberofvertebras, numberoffingers, address):
        super().__init__(name, age, gender, breed, color, weight, height, numberofvertebras)
        self.numberoffingers = numberoffingers   # Aggregation
        self.__address = address   # Private attribute
    
    def speak(self):
        return "Hello!"
    
    def display(self):
        print("No of foot fingers: ", foot.display())
        
#Composition and Polymorphism
class Heart:
    def __init__(self, heartValves):
        self.heartValves = heartValves
        
    def display(self):
        return self.heartValves

class Dog(Mammal):
    def __init__(self, name, age, gender, breed, color, weight, height, numberofvertebras, heartValves):
        super().__init__(name, age, gender, breed, color, weight, height, numberofvertebras)
        self.heartValves = heartValves
        self.heartObject = Heart(self.heartValves)    # Composition
        
    def speak(self):
        return "Woof!"   # Polymorphism

    def display(self):
        print("No of Heart Valves: ", self.heartObject.display())
        
# finish HW01