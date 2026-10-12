'''
input: array (int)
output: array of sub arrays of all triplets that == 0, they are all different indices

constraints:
3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5


time: O(n^2)
space: O(n)


approach:

sort array
init left and right pointer
init result array to 

iterate through array 
start at beginning of list, left pointer + 1, right pointer at end
if they sum to 0, add the results array

return results array


'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])

                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return results
