R=float(input("Enter the resistance (ohms): "))
if R<=0:
    print("Invalid resistance")
else:
    V=float(input("Enter the voltage (V): "))
    I=V/R
    print(f"Current={I}")
    if I>2:
      print("Fuse will blow.")
    else:
      print("Circuit is safe.")