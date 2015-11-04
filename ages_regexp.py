import re
exampleString = '''
Adam is 20 years old,and Ram is 27 years old.
Jessica is 18 years old, and her brother Carnumber is 232.
'''
ages = re.findall(r'\d{1,3}', exampleString)
names = re.findall(r'[A-Z][a-z]*', exampleString)

print(ages)
print(names)

names_ages = {}
age=0
for name in names:
    names_ages[name] = ages[age]
    age+=1
print(names_ages)
    
