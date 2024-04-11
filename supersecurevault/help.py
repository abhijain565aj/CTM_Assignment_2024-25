g1 = "\r\a\n\f\020\f[[\0174\001[\t4+\037?\036\005\033+\b\0Z\005\f\026"
flag = ''.join(chr(ord(c) ^ 107) for c in g1)
print(flag)
