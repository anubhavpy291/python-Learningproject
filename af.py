d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
s = "XXX"
n = len(s)
t = 0
for i in range(n-1):
    for c in range(i+1,n):
        a = d[s[i]]
        b = d[s[c]]
        if a < b:
            t += b - a
        else:
            t += a
print(t)