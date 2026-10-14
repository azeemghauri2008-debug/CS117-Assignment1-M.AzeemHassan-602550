n=int(input("Enter no. of resistors: "))
i=0
a=0
b=0
c=0
while i<n:
    i=i+1
    R=float(input(f"Enter resistance of R{i}:"))
    if R!=0:
        if R in range(98, 102):
            a=a+1
        elif R in range(94, 106):
            (b)=b+1
        elif R<95:
             c=c+1
        elif R>105:
             c=c+1
    else:
        quit()
print(f"No. of resistors with 1% tolerance= {a}")
print(f"No. of resistors with 5% tolerance= {b}")
print(f"No. of rejected resistors= {c}")