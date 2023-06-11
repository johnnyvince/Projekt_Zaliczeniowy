from animal import Animal, create_animal, create_dog
from person import Person, create_person
from welcome_message import print_welcome


print_welcome()


while True:
    choice = input("Would you like to create a person or an animal? (p/a)\n"
                   "Or maybe you would like to adopt a dog! (Then type d): ")

    if choice.lower() == 'p':
        create_person()
        break

    elif choice.lower() == 'a':
        create_animal()
        break

    elif choice.lower() == 'd':
        create_dog()
        break

    else:
        print("Invalid choice. Please try again.")
