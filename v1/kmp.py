def Search(string,pat):
    lconst = 5  #lconst is the large constant used to limit the maximum hash value
    string = string.upper()
    pat = pat.upper()
    #ASSUMING ALL CHARACTERS ARE UPPPER_CASE,
    #Can be extended for lower case if necessary
    
    l = len(string)
    l_p = len(pat)
    con = 26 #The constant for base system 26
    
    hashval = 0    #For the pattern
    currhash = 0 #For each substring
    for i in range(l_p):
        hashval += ((ord(pat[i])-ord('A')+1)*(con**(l_p-i-1)))%lconst
        currhash += ((ord(string[i])-ord('A')+1)*(con**(l_p-i-1)))%lconst
    for ind in range(l-l_p+1):
        if ind!=0:
            currhash = (con*(currhash-((ord(string[ind-1])-ord('A')+1)*(con**(l_p-1))))+((ord(string[ind+l_p-1])-ord('A')+1))%lconst)
  
        if(currhash==hashval):
            i,j = 1,ind+1
            while(i<l_p):
                if string[j]!=pat[i]:
                    break
                i += 1
                j += 1
            else:
                print(ind)