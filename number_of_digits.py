def number_of_digits(n):
    while type(n)==int:
        counter = 0
        while n>0:
            counter+=1
            n//=10
        return counter
    else:
        print("Try again")
