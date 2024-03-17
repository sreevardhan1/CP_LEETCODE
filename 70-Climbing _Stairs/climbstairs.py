'''You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 
Constraints:

1 <= n <= 45'''

#CODE
class Solution:
    def climbStairs(self, n: int) -> int:
        '''#  Using Dynamic Programming Tablulation
        ar=[0]*(n+1)
        if n==0 or n==1:
            return 1
        ar[0]=ar[1]=1
        for i in range(2,n+1):
            ar[i]=ar[i-1]+ar[i-2]
        return ar[n] '''

        # D.P Space Optimization
        if n==0 or n==1:
            return 1
        ways=0
        prev,bef_p=1,1
        # '2' bcz already 0,1 are climbed ,moving to the nth step ->(n+1)
        for i in range(2,n+1):
            ways=prev+bef_p
            bef_p=prev
            prev=ways
        return ways
           