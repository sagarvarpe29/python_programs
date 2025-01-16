menus = {'Breakfast' : ['Pohe','Upma','Sandwich'],
         'Lunch' : ['Panner','Khichadi','Roti'],
         'Dinner' : ['Mix veg','Rice','Dal']}

print("Here is the whole list:\n", menus,sep='')

# To print key and values of above menus dictionary
print("-----Here is the list with key and value pair-----")
for name, value in menus.items():
    print(name,':',value)

person = { 'Name' : 'Sagar Varpe',
           'Age' : '35',
           'City' : 'Sangamner' }

print(person.get('Name'),'is', person.get('Age'), 'years old and living in', person.get('City'))