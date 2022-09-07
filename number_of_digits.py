def number_of_digits(n):
    if type(n)!=int:
        print("Enter a number")
        
        
    while type(n)==int and n>0:
        counter = 0
        while n>0:
            counter+=1
            n//=10
        return counter
    # for Negative numbers
    while type(n)==int and n<0:
        counter_2 = 0
        m = n*-1
        while m>0:
            counter_2+=1
            m//=10
        return counter_2
