class Solution:
    def longestCommonPrefix(self, strs) :
        if strs =="":
            return ""
        answ=strs[0]
        for ele in strs:
            count=0
            for i in range (min(len(answ),len(ele))):
                if answ[i]==ele[i]:
                    count+=1
                else:
                    break
            answ=answ[:count]
        return answ
print(Solution().longestCommonPrefix(["flower","flow","flight"]))