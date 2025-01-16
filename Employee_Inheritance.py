class Employee1:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class SalaryEmployee(Employee1):
    def __init__(self,fname, lname, salary):
        super().__init(fname,lname)
        self.salary = salary

    def calculate_paycheck(self):
        return self.salary/52

class HourlyEmployee(Employee1):
    def __init__(self, fname, lname, weekly_hours, hourly_rate):
        super().__init__(fname, lname)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate

    def claculate_paycheck(self):
        return self.weekly_hours* self.hourly_rate

