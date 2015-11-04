# Python-programs
import re

output = '''
OSPF Process ID 100 VRF default
Total number of neighbors: 3
Neighbor ID     Pri State            Up Time  Address         Interface
12.1.1.1          1 FULL/DR          1d14h    101.11.12.2     Eth3/4/3
13.1.1.1          1 FULL/DR          1d14h    101.11.13.2     Eth3/4/4
99.99.99.99       1 FULL/DR          1d14h    50.1.1.102      Po11
'''


ne_id = re.findall(r'(N[a-z]+\s[A-Z]{2})+\s+P[a-z]+\s+S[a-z]+\s+U[a-z]{1}\s+T[a-z]+\s+A[a-z]+\s+I[a-z]+',output)
priority=re.findall(r'N[a-z]+\s[A-Z]+\s+(P[a-z]+)\s+S[a-z]+\s+U[a-z]{1}\s+T[a-z]+\s+A[a-z]+\s+I[a-z]+',output)
state=re.findall(r'N[a-z]+\s[A-Z]+\s+P[a-z]+\s+(S[a-z]+)\s+U[a-z]{1}\s+T[a-z]+\s+A[a-z]+\s+I[a-z]+',output)
ut=re.findall(r'N[a-z]+\s[A-Z]+\s+P[a-z]+\s+S[a-z]+\s+(U[a-z]{1}\s+T[a-z]+)\s+A[a-z]+\s+I[a-z]+',output)
addr=re.findall(r'N[a-z]+\s[A-Z]+\s+P[a-z]+\s+S[a-z]+\s+U[a-z]{1}\s+T[a-z]+\s+(A[a-z]+)\s+I[a-z]+',output)
intr=re.findall(r'N[a-z]+\s[A-Z]+\s+P[a-z]+\s+S[a-z]+\s+U[a-z]{1}\s+T[a-z]+\s+A[a-z]+\s+(I[a-z]+)',output)


ip=re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\d{1}\s+[A-Z]+\/?[A-Z]+\s+[0-9a-z]+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+[A-Za-z].*',output)
p= re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+(\d{1})\s+[A-Z]+\/?[A-Z]+\s+[0-9a-z]+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+[A-Za-z].*',output)
s=re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+\d{1}\s+([A-Z]+\/?[A-Z]+)\s+[0-9a-z]+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+[A-Za-z].*',output)
t=re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+\d{1}\s+[A-Z]+\/?[A-Z]+\s+([0-9a-z]+)\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+[A-Za-z].*',output)
a=re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+\d{1}\s+[A-Z]+\/?[A-Z]+\s+[0-9a-z]+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+[A-Za-z].*',output)
i=re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+\d{1}\s+[A-Z]+\/?[A-Z]+\s+[0-9a-z]+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+([A-Za-z].*)',output)


keys   = [ne_id,priority,state,ut,addr,intr]

values = [ip,p,s,t,a,i]


klist=[]
for i in keys:
    klist.append(" ".join(i))

dict1={}
for j in range(len(klist)):
    dict1[klist[j]]=values[j]
print dict1        
       
                    
    





  

