import re

output1 = '''show ip ospf database 
        OSPF Router with ID (1.1.1.1) (Process ID 1 VRF default)

                Router Link States (Area 0.0.0.0)

Link ID         ADV Router      Age        Seq#       Checksum Link Count
1.1.1.1         1.1.1.1         1303       0x800000c0 0x5b03   7         
2.2.2.2         2.2.2.2         319        0x800000c1 0x2905   4         
11.11.11.11     11.11.11.11     1508       0x800000c3 0xa62f   3         
12.12.12.12     12.12.12.12     1499       0x800000c3 0xbe09   3         
13.13.13.13     13.13.13.13     1505       0x800000c2 0x3dbc   2         
14.14.14.14     14.14.14.14     1499       0x800000c2 0x5596   2         
21.21.21.21     21.21.21.21     315        0x800000c4 0x25d0   2 '''        


l_id = re.findall(r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+\d{1,3}.\d{1,2}.\d{1,2}.\d{1,2}\s+[\d]+\s+[\d\w]+\s+[\d\w]+\s+[\d]{1}',output1)
a_r_id = re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\s+(\d{1,3}.\d{1,2}.\d{1,2}.\d{1,2})\s+[\d]+\s+[\d\w]+\s+[\d\w]+\s+[\d]{1}',output1)
a = re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\s+\d{1,3}.\d{1,2}.\d{1,2}.\d{1,2}\s+([\d]+)\s+[\d\w]+\s+[\d\w]+\s+[\d]{1}',output1)
s = re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\s+\d{1,3}.\d{1,2}.\d{1,2}.\d{1,2}\s+[\d]+\s+([\d\w]+)\s+[\d\w]+\s+[\d]{1}',output1)
c_s = re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\s+\d{1,3}.\d{1,2}.\d{1,2}.\d{1,2}\s+[\d]+\s+[\d\w]+\s+([\d\w]+)\s+[\d]{1}',output1)
l_c = re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\s+\d{1,3}.\d{1,2}.\d{1,2}.\d{1,2}\s+[\d]+\s+[\d\w]+\s+[\d\w]+\s+([\d]{1})',output1)


L_ID = re.findall(r'(L[\w]+\s[\w]{2})\s+A[\w]{2}\s[\w]+\s+A[\w]{2}\s+S[\w]{2}.\s+C[\w]+\s+L[\w]+\s[\w]+',output1)
A_R_ID = re.findall(r'L[\w]+\s[\w]{2}\s+(A[\w]{2}\s[\w]+)\s+A[\w]{2}\s+S[\w]{2}.\s+C[\w]+\s+L[\w]+\s[\w]+',output1)
A = re.findall(r'L[\w]+\s[\w]{2}\s+A[\w]{2}\s[\w]+\s+(A[\w]{2})\s+S[\w]{2}.\s+C[\w]+\s+L[\w]+\s[\w]+',output1)
S = re.findall(r'L[\w]+\s[\w]{2}\s+A[\w]{2}\s[\w]+\s+A[\w]{2}\s+(S[\w]{2}.)\s+C[\w]+\s+L[\w]+\s[\w]+',output1)
C_S = re.findall(r'L[\w]+\s[\w]{2}\s+A[\w]{2}\s[\w]+\s+A[\w]{2}\s+S[\w]{2}.\s+(C[\w]+)\s+L[\w]+\s[\w]+',output1)
L_C = re.findall(r'L[\w]+\s[\w]{2}\s+A[\w]{2}\s[\w]+\s+A[\w]{2}\s+S[\w]{2}.\s+C[\w]+\s+(L[\w]+\s[\w]+)',output1)




keys1 =(L_ID,A_R_ID,A,S,C_S,L_C)
values1 =(l_id,a_r_id,a,s,c_s,l_c)
 

klist1=[]
for i in keys1:
   klist1.append(" ".join(i))


ospf_database = {}
for i in range(len(klist1)):
    ospf_database[klist1[i]] = values1[i]
print ospf_database     
    
        

  
