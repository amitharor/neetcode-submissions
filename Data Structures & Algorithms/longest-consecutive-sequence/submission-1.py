'''
input: array (int)
output: len of longest consecutive sequence

constraints: 
0 <= nums.length <= 100,000
-10^9 <= nums[i] <= 10^9


time: O()
space: O()

approach:
init var to store input array as a set to get all unique nums (lookup will be o1 time)
init var to store sequence len

iterate through input array and check to see if there is a num in the set that is 1 smaller than the current element;
    if so, move to next element because this is not the start of the element
    otherwise, its the first num in sequence, check if current element + 1 exists in set, if so; track len and keep checking


return length
'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        ans = 0
        


        for num in nums:
            tracker = 1
            if (num-1) in unique:
                continue
            
            while (num+1) in unique:
                tracker+=1
                num += 1
            
            ans = max(ans, tracker)
            

        return ans