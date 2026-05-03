d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
s = "MCMXCIV"

n = (len(s) - 1)
t = 0
i = 0
while n >= 0:
    a = d[s[n]]
    if(n != 0):
        b = d[s[n-1]]
    
    if a > b and n != 0:
        t = t + (a - b)
        n -= 2
    else:
        t = t + a
        n -= 1
print(t)