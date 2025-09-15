class Person:
    def __init__(self, person_id: str, name: str, email: str):
        self.person_id = person_id
        self.name = name
        self.email = email

    def get_details(self) -> str:
        return f"ID: {self.person_id} | Name: {self.name} | Email: {self.email}"

    def get_responsibilities(self) -> str:
        return "General responsibilities for a person."
