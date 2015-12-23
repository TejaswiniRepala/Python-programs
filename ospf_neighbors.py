import re

def parsing_ospf_ne(output):
    p = re.compile("(\d{2}\.\d{1,2}\.\d{1,2}\.\d{1,2})\s+(\d{1})\s(\w+\/\w+)\s+(\d{1}\w\d{2}\w)\s+(\d+\.\d+\.\d+\.\d+)\s+(\w+\d{1}\/\d{1}\/\d{1}|\w+\d)")
    matches = [m.groups() for m in p.finditer(output)]
    #print "Groups of Matches list:",matches,"\n"

    neighbor_id = [a for a,b,c,d,e,f in matches]
    #print "Neighbor ID list:",neighbor_id,"\n"

    pri = [b for a,b,c,d,e,f in matches]
    #print "Pri_list:", pri,"\n"

    state = [c for a,b,c,d,e,f in matches]
    #print "State_list:",state,"\n"

    up_time = [d for a,b,c,d,e,f in matches]
    #print "Up Time:",up_time,"\n"

    ip_address = [e for a,b,c,d,e,f in matches]
    #print "Address_list:",ip_address,"\n"

    interface = [f for a,b,c,d,e,f in matches]
    #print "Interface_list:",interface,"\n"
    return(neighbor_id,pri,state,up_time,ip_address,interface)

def verification_ospf_ne():
    Expected_output=''' 
        Neighbor ID     Pri State            Up Time  Address         Interface
        12.1.1.1          1 FULL/DR          1d14h    101.11.12.2     Eth3/4/3
        13.1.1.1          1 FULL/DR          1d14h    101.11.13.2     Eth3/4/4
        99.99.99.99       1 FULL/DR          1d14h    50.1.1.102      Po11'''
    neighbor_id,pri,state,up_time,ip_address,interface = (parsing_ospf_ne(Expected_output))
    #print(neighbor_idx,prix,statex,up_timex,ip_addressx,interfacex )
    
    current_output='''
       Neighbor ID     Pri State            Up Time  Address         Interface
        12.1.1.2          1 FULL/DR          1d14h    101.11.12.2     Eth3/4/3
        13.1.1.3          1 FULL/DR          1d14h    101.11.13.2     Eth3/4/4
        99.99.99.99       1 FULL/DR          1d14h    50.1.1.102      Po11'''
    neighbor_id1,pri1,state1,up_time1,ip_address1,interface1 = (parsing_ospf_ne(current_output))
    #print(neighbor_idy,priy,statey,up_timey,ip_addressy,interfacey)
       
    i=0
    while (i<3):
        if neighbor_id[i]==neighbor_id1[i] and pri[i]==pri1[i] and state[i]==state1[i] and up_time[i]==up_time1[i] and ip_address[i]==ip_address1[i] and interface[i]==interface1[i]:
            print "pass",neighbor_id[i],pri[i],state[i],up_time[i],ip_address[i],interface[i],neighbor_id1[i],pri1[i],state1[i],up_time1[i],ip_address1[i],interface1[i]
        else:
            print "Fail",neighbor_id[i],pri[i],state[i],up_time[i],ip_address[i],interface[i],neighbor_id1[i],pri1[i],state1[i],up_time1[i],ip_address1[i],interface1[i]
        i+=1


           
verification_ospf_ne()    


    
    
    
    
    
    



