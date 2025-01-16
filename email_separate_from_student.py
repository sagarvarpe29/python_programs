contacts = {
            'number' : 4,
            'students' : [
                {'name': 'Sagar Varpe', 'email' : 'sagar@test.com'},
                {'name': 'Pallavi Varpe', 'email' : 'pallavi@test.com'},
                {'name': 'Satyaki Varpe', 'email' : 'satyaki@test.com'},
                {'name': 'Sheela Varpe', 'email' : 'sheela@test.com'},
                {'name': 'Varsha Varpe', 'email' : 'varsha@test.com'}
            ] 
}
var = ''
print('Student emails are:')
for student in contacts['students']:
    var = var + student['email']

print(var)