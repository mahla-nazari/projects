def in_func(char , s):
    
    #for dictionary
    while type(s)==dict:
        try:
            return s[char]!=""
        except KeyError:
            return False
        
    #for List & tuple & set
    while type(s)==list or type(s)==tuple  or type(s)==set:
        for i in s:
            if i==char:
                return True
        return False
    
    #for string
    while type(s)==str:
        for i in range(0,len(s)):
            if char[0]==s[i]:
                counter=i+1
                for j in range(1,len(char)):
                    if char[j]==s[counter]:
                        counter+=1
                        j+=1
                    else:
                        return False
                return True
        return False
    
    #for int
    while type(s)==int:
        raise TypeError('Enter str, tuple, list, dict or set')