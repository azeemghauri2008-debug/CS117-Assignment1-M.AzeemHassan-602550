A=int(input("Enter A: "))
B=int(input("Enter B: "))
if A==1:
    if B==1:
        print("AND=1\nOR=1\nXOR=0")
    elif B==0:
        print("AND=0\nOR=1\nXOR=1")
elif A==0:
    if B==0:
        print("AND=0\nOR=0\nXOR=0")
    elif B==1:
        print("AND=0\nOR=1\nXOR=1")
else:
    print("Bits must be 0 or 1")

