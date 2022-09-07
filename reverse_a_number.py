def reverse_a_number(a):
    flag = 0
    while a > 0:
        x = number_of_digits(a)
        b = (a % 10)
        b*=10**(x-1)
        flag += b
        a//=10
    return flag