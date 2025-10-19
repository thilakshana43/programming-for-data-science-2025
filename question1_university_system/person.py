class Person:
    # Constructor method initializes the base attributes for all people in the university.
    def __init__(self, person_id: str, name: str, email: str):
        # 'self' refers to the instance of the class.
        # Assigning attributes that every person will have.
        self.person_id = person_id
        self.name = name
        self.email = email

    # Common method to return formatted personal details.
    def get_details(self) -> str:
        return f"ID: {self.person_id} | Name: {self.name} | Email: {self.email}"

    # This method will be overridden (polymorphism) by subclasses (Student, Faculty, etc.).
    def get_responsibilities(self) -> str:
        return "General responsibilities for a person."
