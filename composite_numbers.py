def composite_numbers(n):
    if n<=3:
        print("Enter another number")
    else:
        for i in range(3 , n):
            for j in range(3, n):
                while i<n and j<n and i*j==n:
                    return True
        return False
