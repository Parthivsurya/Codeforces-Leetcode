class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        newdigit = 0
        for i in range(len(digits)):
            newdigit=newdigit*10+digits[i]
        li = list(str(newdigit+1))
        return [int(x) for x in li]

        