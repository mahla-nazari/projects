def polindromic_number(n):
    while n == reverse_a_number(n):
        return True
    else:
        return False