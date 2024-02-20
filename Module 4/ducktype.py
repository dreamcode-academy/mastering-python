'''
    DuckType
     <(o )___
      ( ._> /
       `---' 

"If it looks like a duck, 
swims like a duck, 
and quacks like a duck, 
then it probably is a duck."
'''

class Bird:
    def fly(self):
        print("This bird is flying")

class Airplane:
    def fly(self):
        print("This airplane is flying")


def let_it_fly(entity):
    entity.fly() #DUCKTYPING

sparrow = Bird()
boeing = Airplane()

let_it_fly(sparrow)

let_it_fly(boeing)

