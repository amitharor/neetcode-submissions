'''
i: int nums list and int k
o: k most freq elements as a list

constraints: 
1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.



time: O(n)
space: O(n)

init var get freq count of each elements
using bucket sort create a dict with freq as key and element as value

init results var to store top k elements
iterate through bucket list from reverse (to get largest num first)
push the num at current element into results
if results len == k; return results
'''

from collections import Counter, defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in num_count.items():
            buckets[freq].append(num)


        results = []

        for freq in range(len(buckets)-1, 0, -1): #start, stop, step
            for num in buckets[freq]:
                results.append(num)

                if len(results) == k:
                    return results