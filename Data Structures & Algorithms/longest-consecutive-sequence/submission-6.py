'''
Input: array (int)
Output: len (int) of longest seq of nums

Constraints:
0 <= nums.length <= 100,000
-10^9 <= nums[i] <= 10^9

Time: O(n)
Space: O(n)

Approach:
Init var to store hash set of input array
Init var to store results
Iterate through loop
Check if current num - 1 exists in set; if so, continue

Set results to 1
Repeatedly check if num + 1 exists in set and as long as it does:
	Increment sequence len
	Update results if current sequence larger than what is currently stored

Return results
'''



class Solution:
	def longestConsecutive(self, nums):
		unique = set(nums)
		results = 0
		
		for num in unique:
			if num-1 in unique:
				continue
			
			count = 1
			while num + count in unique:
				count += 1
			results = max(results, count)
			
		return results

        