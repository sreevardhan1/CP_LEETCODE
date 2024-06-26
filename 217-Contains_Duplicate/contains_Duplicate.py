'''Given an integer array nums, return true if any value appears 
at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 
Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109'''

#CODE
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Brute Force
        '''n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]==nums[j]:
                    return True
        return False'''

       # hash set
        visit=set()
        n=len(nums)
        for i in nums:
            if i in visit:
                return True
            visit.add(i)
        return False