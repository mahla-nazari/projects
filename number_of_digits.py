def number_of_digits(n):
    counter = 0
    while n>0:
        counter+=1
        n//=10
    return counter