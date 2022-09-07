def polindromic_number(n):
    #Run reverse_a_number function
    while type(n)==int:
        while n == reverse_a_number(n):
            return True
        else:
            return False
    else:
        print("Try again")
