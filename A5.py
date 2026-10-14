R1=float(input("Enter R1: "))
R2=float(input("Enter R2: "))
R3=float(input("Enter R3: "))
if R1>R2:
    if R2>R3:
        print(f"Largest: {R1}\nSmallest: {R3}")
    elif R1<R3:
        print(f"Largest: {R3}\nSmallest: {R2}")
elif R2>R1:
    if R2<R3:
        print(f"Largest: {R3}\nSmallest: {R1}")
    elif R3<R1:
        print(f"Largest: {R2}\nSmallest: {R3}")
elif R1<R3:
       if R2>R3:
        print(f"Largest: {R2}\nSmallest: {R1}")
       elif R2<R1:
        print(f"Largest: {R3}\nSmallest: {R2}")