from collections import defaultdict
import heapq
 
class Twitter:

    def __init__(self):
        self.count = 0  # Global timestamp (decremented to simulate Max-Heap)
        self.tweetMap = defaultdict(list)   # userId -> list of [count, tweetId]
        self.followMap = defaultdict(set)   # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Decrement count so more recent tweets have smaller (more negative) numbers
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        minHeap = []

        # Ensure the user always follows themselves so their own tweets appear in the feed
        self.followMap[userId].add(userId)

        # Step 1: For every person the user follows, get their latest tweet
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap and self.tweetMap[followeeId]:
                # Index of the most recent tweet is at the end of the user's tweet list
                lastIndex = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][lastIndex]
                
                # Push [count, tweetId, followeeId, next_index_to_look_at]
                heapq.heappush(minHeap, [count, tweetId, followeeId, lastIndex - 1])

        # Step 2: Pop up to 10 most recent tweets using the heap
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, nextIndex = heapq.heappop(minHeap)
            res.append(tweetId)

            # If this followee has more previous tweets, push the next one onto the heap
            if nextIndex >= 0:
                count, tweetId = self.tweetMap[followeeId][nextIndex]
                heapq.heappush(minHeap, [count, tweetId, followeeId, nextIndex - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # A user cannot unfollow themselves, and can only unfollow someone they already follow
        if followeeId in self.followMap[followerId] and followerId != followeeId:
            self.followMap[followerId].remove(followeeId)