import re

a = ''' Teja:408-657-4135,
        Nani:408-363-1233 '''

b='''tejaswini.repala@gmail.com
        repal.lalitha@gmail.com'''

name=re.findall(r'[A-Z][a-z]*',a)
phonenum=re.findall(r'\d{1,3}\-\d{1,3}\-\d{1,4}',a)
#e-mail
email = re.findall(r'(\w+\.\w+\@\w+\.\w+)',b)

print(phonenum)
print(name)
print(email)

