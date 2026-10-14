def ohms_current(v,r):
    return v/r
def power_dissipated(i,r):
    return i**2*r
v=12
r=6
I=ohms_current(v,r)
P=power_dissipated(I,r)
print(f"Current= {I}A")
print(f"Power= {P}W")