def star_to_delta(ra, rb, rc):
    num=ra*rb+rb*rc+rc*ra
    r_ab=num/rc
    r_bc=num/ra
    r_ca=num/rb
    return round(r_ab, 2), round(r_bc, 2), round(r_ca, 2)
print(star_to_delta(10,20,30))