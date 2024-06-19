class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello! My name is {self.name}. I am {self.age} years old and I am {self.gender}.")

# Create an instance of the Person class
person_instance = Person("John Doe", 30, "male")

# Call the introduce method to display the person's information
person_instance.introduce()

"""
Explanation:
Class Definition:

The Person class is defined using the class keyword.
The __init__ method is the constructor that initializes the attributes name, age, and gender when a new instance of the class is created.
Attributes:

name, age, and gender are instance attributes initialized in the __init__ method.
Method:

The introduce method prints out a message introducing the person using the instance's attributes.
Creating an Instance:

An instance of the Person class is created with the name "John Doe", age 30, and gender "male".
Calling the Method:

The introduce method is called on the instance to print the introduction message.
Running the Code:
To run the code:

Save it to a file, for example, person.py.
Open a terminal or command prompt.
Navigate to the directory where the person.py file is saved.
Run the script using the command:
sh
Copy code
python person.py
You should see the following output:

sh
Copy code
Hello! My name is John Doe. I am 30 years old and I am male.
"""
