class Solution:
    def addDigits(self, num: int) -> int:
        num_l = list(map(int, str(num)))
        while len(num_l) > 1:
            total = sum(num_l)
            num_l = list(map(int, str(total)))
        return (num_l[0])
Solution()