class Employee:
    def __init__(self, firstName, lastName, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary

    def calculate_payCheck(self):
        return self.salary/52