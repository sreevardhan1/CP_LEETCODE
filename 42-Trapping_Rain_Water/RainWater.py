'''Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
 In this case, 6 units of rain water (blue section) are being trapped.

 Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105'''

#CODE
class Solution:
    def trap(self, height: List[int]) -> int:
        water_trapped=0
        n=len(height)
        lef_max=[0]*n   # Creating a arr of max building from left
        rig_max=[0]*n   # Creating a arr of max building from right

        # Fixing the first(0) and last(n-1) posi values
        lef_max[0]=height[0]
        rig_max[n-1]=height[n-1]

        # Traversing from left and comparing original list & lef_max
        # and storing the max val i.e max(build height,lef_max)
        for i in range(1,n):
            lef_max[i]=max(lef_max[i-1],height[i])

        #Traversing from right and comparing original list & rig_max 
        #and storing the max val i.e max(build height,rig_max)
        for i in range(n-2,-1,-1):
            rig_max[i]=max(rig_max[i+1],height[i])

        # find the min(lef_max,rig_max)
        # and also subtract the min values with original list values
        for i in range(n):
            water_trapped+=min(lef_max[i],rig_max[i])-height[i]

        return water_trapped