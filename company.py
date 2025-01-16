from employee import Employee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_Employee(self):
        print('Current Employees:')
        for i in self.employees:
            print(i.firstName, i.lastName)
        print('------------------------------')

    def display_payCheck(self):
        print('Current Paycheck is:')
        for i in self.employees:
            print('Paycheck for:', i.firstName, i.lastName)
            print(f'Amount :, ${i.calculate_payCheck():,.2f}')
            print('---------------------------------------')

def main():
    my_company = Company()

    employee1 = Employee('Sagar','Varpe',50000)
    my_company.add_employee(employee1)

    employee2 = Employee('Satyaki', 'Varpe', 60000)
    my_company.add_employee(employee2)

    employee3 = Employee('Pallavi','Varpe', 70000)
    my_company.add_employee(employee3)

    my_company.display_Employee()
    my_company.display_payCheck()

main()