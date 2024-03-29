'''Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

* Starting with any positive integer, replace the number by the sum of the squares of its digits.

* Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.

* Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:
Input: n = 2
Output: false
 
Constraints:
1 <= n <= 231 - 1'''

#CODE
class Solution:
    def isHappy(self, n: int) -> bool:
        def sqr(num):
            sum=0
            while num>0:
                r=num%10
                sum+=r**2
                num=num//10
            return sum
        for i in range(70):
            n=sqr(n)
            if n==1:
                return True
        return False

        ''' already=[]
        l=list(str(n))
        if n==1:
            return true
        sum=0
        while sum!=0:
            for i in l:
                sum  += int(i)**2
            if sum==1:
                return true
            else:
                if sum in already:
                    return false
                already.append(sum)
                l=list(str(sum)) 
                sum=0  ''' 