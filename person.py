class Person:
    def __init__(self, name, occupation, age):
        self._name = name
        self._occupation = occupation
        self._age = age

    def display_info(self):
        print("Person's name:", Person.get_name(self))
        print("Person's occupation:", Person.get_occupation(self))
        print("Person's age:", Person.get_age(self))

    # Setter
    def set_name(self, name):
        self._name = name

    def set_occupation(self, occupation):
        self._occupation = occupation

    def set_age(self, age):
        self._age = age

    # Getter
    def get_name(self):
        return self._name

    def get_occupation(self):
        return self._occupation

    def get_age(self):
        return self._age


def create_person():
    name = input("Enter name: ")
    occupation = input("Enter occupation: ")
    age = input("Enter age: ")

    person = Person(name, occupation, age)
    person.display_info()
    print("Person created!")

