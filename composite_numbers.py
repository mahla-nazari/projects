def composite_numbers(n):
    if n<=0:
        print("Enter another number")
    else:
        for i in range(0 , n):
            for j in range(0, n):
                while i<n and j<n and i*j==n:
                    return True
        return False