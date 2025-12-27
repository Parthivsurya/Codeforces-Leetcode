class Solution:
    def romanToInt(self, s: str) -> int:
        refection= {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000}
        New= list(s)
        ref=[]
        number=0
        #print(New)
        for i in range (len(New)):
            ref.append(refection[New[i]])
        #print(ref)
        for i in range(len(ref)-1):
            if ref[i]<ref[i+1]:
                number-=ref[i]
            else:
                number+=ref[i]
        return (number+refection[New[-1]])                   
                        
sol = Solution()
print(sol.romanToInt("MCMXCIV"))
        