#longestcommonprefix.py

def longestcommonprefix():   
    strs = ["flower","flour","floor","flow","fly"] 
    result=''
    for i in range(len(strs)):
        minlen=min(len(strs[0]),len(strs[i]))
        #print minlen

    for i in range(minlen):
        let=strs[0][i]
        for j in range(1,len(strs)):
            if let!=strs[j][i]:
                return result
        result+=let
    print result

        


print longestcommonprefix()
