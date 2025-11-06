from dataclasses import dataclass


@dataclass
class User:
    def __init__(self, id: str, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

    def change_email(self, new_email: str):
        if '@' not in new_email:
            raise ValueError("Invalid email format")
        self.email = new_email
