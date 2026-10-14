def parallel_resistance(resistors):
    R_eq=0
    n=int(input("Enter no. of resistors: "))
    for i in range(1,n+1):
        R=float(input(f"Enter resistance of R{i}:"))
        R_eq=R_eq+1/R
    return(1/R_eq)
print(parallel_resistance([1,10]))