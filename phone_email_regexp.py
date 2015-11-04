import re

a = ''' Teja:408-657-4135,
        Nani:408-332-1445 '''

b='''tejaswini.repala@gmail.com
        repal.lalitha@gmail.com'''

name=re.findall(r'[A-Z][a-z]*',a)
phonenum=re.findall(r'\d{1,3}\-\d{1,3}\-\d{1,4}',a)
#e-mail
email = re.findall(r'([a-z0-9]+\.[a-z]+\@[a-z]+\.[a-z]+)',b)

print(phonenum)
print(name)
print(email)

