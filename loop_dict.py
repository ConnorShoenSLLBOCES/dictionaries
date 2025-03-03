# Collect some data from user
name = input("Please Enter Your First Name: ")
age = int(input("Please Enter Your Age: "))
city = input("Please Enter Your City: ")

user = {'Name':name,'Age':age,'City':city}
print (user)

print ("\n\nKeys:")
for key in user: #loops through keys
    print (key)

print ("\n\nData Values:")
for value in user.values():
    print (value)

print ("\n\nBoth:")
for key, value in user.items():
    print (key, value)
    key1 = user.items()
    print (key1)

grades = {'Hannah':90,'Gavin':45,'Cameron':87,'Hunter':91,'Eva':73,'Connor':2,'Christian':98,'David':1}

for student, grade in grades.items():
    print (f"{student}: {grade}")