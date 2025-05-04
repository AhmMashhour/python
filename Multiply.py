def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i} * {j}" ,"=",i*j)
            if j==i:
                break
        print()  

num = int(input("Enter a number: "))
multiplication_table(num)
