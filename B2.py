A=int(input("How many resistors? "))
R=0
for i in range(1,A+1):
  Req=float(input(f"Enter the resistance for R{i} (in ohms)"))
  R+=Req
print(f"The total resistance is: {R}")