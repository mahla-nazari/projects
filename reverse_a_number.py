
def revers_int(n):
    flag = 0
    if type(n)!=int:
        print("Enter a number")
    while type(n)==int:
        while n>0 :
            x=number_of_digits(n)
            c= (n%10)
            c*=10**(x-1)
            flag+=c
            n//=10
        return flag
