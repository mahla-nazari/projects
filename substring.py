def substring(ch , s):
        while len(ch) <= len(s) and type(s)==str:
                while ch in s:
                    return True
                return False
        else:
                print("Try again!")
               

# or________use in_func________
# first, Run in_func


def substring(ch , s):
        while len(ch) <= len(s) and type(s)==str:
                while in_func(ch , s)==True:
                        return True
                return False
        else:
                print("Try again!")
                        
                        
                        
                           
