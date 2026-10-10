'''
input: array int and k int
output: return k most freq elements of array

constraints: 
1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.

time: O(n)
space: O(n)

approach: 

count freq of each number and store as key/val pair hash map
create bucket the len of input array and we can store the val of each num at it's index (freq key)

create a var to store results
iterate through bucket in reverse order to get largest num
for each num; iterate through array and push num into results
check if len of result array is == k; if so, return result array
'''

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        res = []


        for num, freq in count.items():
            bucket[freq].append(num) # remember to APPEND as we are adding to a LIST !!! IMPORTANT

        for i in range(len(bucket) -1, 0, -1):
            for num in bucket[i]:
                res.append(num)

                if len(res) == k:
                    return res