class Directory:
    def __init__(self):
        self.contacts = []

    def __len__(self):
        return len(self.contacts)

    def add(self, contact):
        self.contacts.append(contact)

    def query(self, name=None):
        return [contact for contact in self.contacts if contact.name == name]

    def find(self, query):
        return [
            contact for contact in self.contacts
            if query in contact.name or
               (hasattr(contact, 'surname') and contact.surname and query in contact.surname) or
               (contact.phone and query in contact.phone)
        ]


class Person:
    def __init__(self, name, surname=None, phone=None):
        self.name = name
        self.surname = surname
        self.phone = phone


class Business:
    def __init__(self, name, phone=None):
        self.name = name
        self.phone = phone
