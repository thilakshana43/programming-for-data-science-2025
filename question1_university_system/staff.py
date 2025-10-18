from question1_university_system.person import Person


class Staff(Person):
    def __init__(self, staff_id, name, email, position):
        #This is the constructor method that runs when a new Staff object is created.
        super().__init__(staff_id, name, email)
        #This calls the constructor of the parent class Person to initialize the shared attributes staff_id, name, and email.
        self.position = position
        #creates a new attribute position specific to Staff objects

    def get_responsibilities(self):
        return "Support for the faculty"