#solution 
def romanToInt(self,s: str) -> int:
    map_of_char ={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    length=len(s)
    r=0
    for i in range(length):
        if(i+1<length) and (map_of_char[s[i]]<map_of_char[s[i+1]]):
            r-= map_of_char[s[i]]
        else:
            r+=map_of_char[s[i]]
    return r


#Sending  test cases to the function
s="MCMXCIV"
p=romanToInt(s)
print(p)

