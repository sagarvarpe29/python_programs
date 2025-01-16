# Create an empty dictionary
menu = {}

# Add values to dictionary
menu['Soup'] = 10.5
menu['Salad'] = 12.5
menu['Paneer'] = 15
menu['Bread'] = 3

# Print 'menu' dictionary object
print(menu)

definition = menu.get('Mix veg')

if definition:
    print(definition)
else:
    print('Key doesnot exist')

# update dictionary

menu['Salad'] = 17

print("Updated value of Salad is",menu['Salad'])

# Delete Panner from menu
del menu['Paneer']

print("Panner is deleted from", menu)