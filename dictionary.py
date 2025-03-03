print ("\nPython Dictionaries:")
my_dict = {'name':'Connor','age':17,'city':'Canton'}
print (f'My name is: {my_dict['name']}')

print ("\nAdding and Updating Items in a Dictionary:")
my_dict['country'] = 'America' # Adding a key value pair
print (my_dict)
my_dict ['age'] = 782
print (f"\n{my_dict}")

print ("\nRemoving Items from a dictionary:")
del my_dict['country']
print (my_dict)

print ("\nDelete an item from the dictionary and return it's value:")
remmy = my_dict.pop('age')
print (remmy)
print (my_dict)

print ("\nA new dictionary:")
dict2 = {'fruits':['apple','banana','orange'], 'veggies':['broccoli','brussel sprouts','carrot']}
print (dict2)
# add a new fruit
dict2['fruits'].append('cherry')
print (f"\n{dict2}\n")
print (dict2['fruits'])