class Animal:
    def __init__(self, name, species, age):
        self._name = name
        self._species = species
        self._age = age

    def display_info(self):
        print(f"Animal's name:", Animal.get_name(self))
        print(f"Animal's occupation:", Animal.get_species(self))
        print(f"Animal's age:", Animal.get_age(self))

    # Setter
    def set_name(self, name):
        self._name = name

    def set_species(self, species):
        self._species = species

    def set_age(self, age):
        self._age = age

    # Getter
    def get_name(self):
        return self._name

    def get_species(self):
        return self._species

    def get_age(self):
        return self._age


def create_animal():
    name = input("Enter name: ")
    species = input("Enter species: ")
    age = input("Enter age: ")

    animal = Animal(name, species, age)
    animal.display_info()
    print("Animal created!")


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, "Dog", age)

    def bark(self):
        print("Woof!")


def create_dog():
    name = input("Enter dog's name: ")
    age = input("Enter dog's age: ")

    dog = Dog(name, age)
    dog.display_info()
    dog.bark()
    print("Dog created!")


