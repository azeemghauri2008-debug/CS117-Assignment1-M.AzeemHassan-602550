def loaded_divider(vs, r1, r2, rl):
    rp=(r2*rl)/(r2+rl)
    unloaded=vs*r2/(r1+r2)
    loaded=vs*rp/(r1+rp)
    return (unloaded, loaded)

print(loaded_divider(12, 1000, 1000, 500))