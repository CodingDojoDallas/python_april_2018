class Habitat(object):
    def __init__(self, location, climate):
        self.location = location
        self.climate = climate

    def print_habitat(self):
        print 'Location: {}, Climate: {}'.format(self.location, self.climate)

# This is a class ---- blueprint, schematic, recipe, structure
class Animal(object):
    def __init__(self, animal_name, habitat, weight): # This line initializes the class
        # set parameter name as attribute of class animal
        # self is the object, animal_name is the name we passed in
        self.name = animal_name
        self.bloodflow = True
        self.habitat = habitat
        self.weight = weight

    # method that prints the name of the animal
    def print_name(self):
        print self.name

    def print_habitat(self):
        for habitat in self.habitat:
            # what is habitat? Habitat object
            habitat.print_habitat()
        return self

    def print_weight(self):
        print self.weight
        return self

# Animal > Dog
class Dog(Animal):
    def __init__(self, name, voice, habitat, weight):
        super(Dog, self).__init__(name, habitat, weight) #Animal.__init__()
        self.voice = voice

# dog the object. It's an instantiation of a class.
# You made this from the Animal class.
# The house, the thing, the food, the
# Animal - class
couch = Habitat('Carrollton', 'room temperature')
greenChair = Habitat('living room', 'cold')
dog = Dog('Toby', 'woooooOooOOOOOof', [couch, greenChair], 55)
dog.print_name() # Animal.print_name(dog)
# print dog.bloodflow
# print dog.voice
dog.print_habitat()
