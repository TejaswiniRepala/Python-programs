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


ne_id = re.findall(r'(N\w+\s\w{2})+\s+P\w+\s+S\w+\s+U\w{1}\s+T\w+\s+A\w+\s+I\w+',output)
priority=re.findall(r'N\w+\s\w+\s+(P\w+)\s+S\w+\s+U\w{1}\s+T\w+\s+A\w+\s+I\w+',output)
state=re.findall(r'N\w+\s\w+\s+P\w+\s+(S\w+)\s+U\w{1}\s+T\w+\s+A\w+\s+I\w+',output)
ut=re.findall(r'N\w+\s\w+\s+P\w+\s+S\w+\s+(U\w{1}\s+T\w+)\s+A\w+\s+I\w+',output)
addr=re.findall(r'N\w+\s\w+\s+P\w+\s+S\w+\s+U\w{1}\s+T\w+\s+(A\w+)\s+I\w+',output)
intr=re.findall(r'N\w+\s\w+\s+P\w+\s+S\w+\s+U\w{1}\s+T\w+\s+A\w+\s+(I\w+)',output)


ip=re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\d{1}\s+\w+\/?\w+\s+\w+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+\w.*',output)
p= re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+(\d{1})\s+\w+\/?\w+\s+\w+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+\w.*',output)
s=re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+\d{1}\s+(\w+\/?\w+)\s+\w+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+\w.*',output)
t=re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+\d{1}\s+\w+\/?\w+\s+(\w+)\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+\w.*',output)
a=re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+\d{1}\s+\w+\/?\w+\s+\w+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\w.*',output)
i=re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+\d{1}\s+\w+\/?\w+\s+\w+\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+(\w.*)',output)


keys   = [ne_id,priority,state,ut,addr,intr]

values = [ip,p,s,t,a,i]


klist=[]
for i in keys:
    klist.append(" ".join(i))

dict1={}
for j in range(len(klist)):
    dict1[klist[j]]=values[j]
print dict1        
       
                    
    





  

