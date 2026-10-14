V=[12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]
best_length=1
best_start=0
c_length=1
c_start=0
for i in range(1, len(V)):
    if V[i]<V[i-1]:
        c_length=c_length+1
    else:
        c_length=1
        c_start=i
    if c_length>best_length:
        best_length=c_length
        best_start=c_start
best_end=best_start+best_length-1
print(f"Longest continuous drop: {best_length}minutes")
print("Started at: ", V[best_start],"V")
print("Ended at: ", V[best_end], "V")