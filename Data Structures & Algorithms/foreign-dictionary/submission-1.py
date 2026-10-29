'''
Input(s): list of strings
Output: return string of unique letter in new alien lang sorted in lexicographically increasing order, else return ''

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.

Approach:
topological sort

Time: O(N + V + E) -> where V is the num of unique chars, E is the num of edges and N is the sum of the len of string 
Space: O(V + E)
'''

import heapq

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ''
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        queue = deque([c for c in indegree if indegree[c] == 0])
        result = []

        while queue:
            char = queue.popleft()
            result.append(char)

            for neighbor in adj[char]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) != len(indegree):
            return ''

        return ''.join(result)