'''Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
 
Constraints:
1 <= numRows <= 30'''

#CODE
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
            
        Pasc_tri=[]
        row1=[1]
        Pasc_tri.append(row1)

        for i in range(1,numRows):
            prev_row=Pasc_tri[i-1]
            curr_row=[1]

            for j in range(1,i):
                #sum of above two values
                curr_row.append(prev_row[j-1]+prev_row[j])
            curr_row.append(1)
            Pasc_tri.append(curr_row)

        return Pasc_tri
            