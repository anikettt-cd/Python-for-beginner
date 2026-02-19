class animal:
      pass
  
class pet(animal):
      pass
  
class dogs(pet):
    @staticmethod
    def bark():
        print("Woof Woof")
        
d = dogs()
d.bark()
      