from sets import Set
engineers = Set(['John', 'Jane', 'Jack', 'Janice'])
programmers = Set(['Jack', 'Sam', 'Susan', 'Janice'])
managers = Set(['Jane', 'Jack', 'Susan', 'Zack'])
employees = engineers | programmers | managers
engineering_management = engineers & managers            
fulltime_management = managers - engineers - programmers 
engineers.add('Marvin')                                  
print engineers 
Set(['Jane', 'Marvin', 'Janice', 'John', 'Jack'])
employees.issuperset(engineers)     
False
employees.update(engineers)         
employees.issuperset(engineers)
True
for group in [engineers, programmers, managers, employees]: 
     group.discard('Susan')          
     print group
