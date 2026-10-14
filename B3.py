V=(3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)
count=0
highest=V[0]
lowest=V[0]
total=0
for r in V:
    if r>3.2:
        count=count+1
    if r>highest:
        highest=r
    if r<lowest:
        lowest=r
    total=total+r
average=total/len(V)
print(f"No. of voltages above 3.2V: {count}\nHighest:{highest}V\nLowest:{lowest}V\nAverage:{average}V")