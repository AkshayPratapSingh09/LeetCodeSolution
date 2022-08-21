class Solution:
    def trailingZeroes(self, n: int) -> int:
        fact = 1
        for i in range(1,n+1):
            fact = fact * i
        print(fact)
        a = fact
        count = 0
        i = 0
        b = a
        while i==0:
            b = b/10
            print(b)
            i = b%10
            b = b
            count += 1
        return count

        
a = Solution()
print(a.trailingZeroes(30))

# a = 12340000
# print(list(str(a)).count("0"))

#trailing zeroes
count = 0


