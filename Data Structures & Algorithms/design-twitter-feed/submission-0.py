'''
input: 

output: implement twitter

constraints:
1 <= userId, followerId, followeeId <= 500
0 <= tweetId <= 10^4
All the tweets have unique IDs.
At most 3 * 10^4 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
A user cannot follow themself.

approach:
heap

time: O(n log n)
space: O(n * m)



'''


class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        candidates = list(self.tweets[userId][-10:])
        for followee in self.following[userId]:
            candidates.extend(self.tweets[followee][-10:])
        candidates.sort(reverse = True)
        return [tweet_id for time, tweet_id in candidates[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)









        
