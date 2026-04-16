from collections import defaultdict
import heapq

class Twitter:
    # Goal: Design simplified Twitter supporting posts, follow/unfollow, and news feed
    # Approach: Hash maps for tweets/follows, min-heap for merging sorted tweet lists
    
    def __init__(self):
        # Initialize timestamp counter (negative for max-heap simulation with min-heap)
        self.count = 0
        
        # Map: userId -> set of followeeIds (who this user follows)
        self.following = defaultdict(set)
        
        # Map: userId -> list of [timestamp, tweetId] (user's tweets in chronological order)
        self.post = defaultdict(list)
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        # Goal: User posts a tweet with current timestamp
        # Append [timestamp, tweetId] to user's tweet list
        self.post[userId].append([self.count, tweetId])
        
        # Decrement timestamp (negative values allow min-heap to act as max-heap)
        # More recent tweets have more negative values, so they're "smaller" in min-heap
        self.count -= 1
    
    def getNewsFeed(self, userId: int) -> List[int]:
        # Goal: Return 10 most recent tweet IDs from user and their followees
        # Approach: Merge k sorted lists (each user's tweets) using min-heap
        
        # Edge case: User should see their own tweets in feed
        self.following[userId].add(userId)
        
        # Min-heap stores: [timestamp, tweetId, followeeId, index]
        # timestamp is key - most negative (most recent) has highest priority
        minHeap = []
        
        # Step 1: Initialize heap with most recent tweet from each followee
        for followee in self.following[userId]:
            # Get index of most recent tweet for this followee
            i = len(self.post[followee]) - 1
            
            # Check if this followee has posted any tweets
            if i >= 0:
                count, tweetId = self.post[followee][i]
                
                # Add to heap: [timestamp, tweetId, followeeId, next_index_to_check]
                # next_index = i (current position) for tracking which tweet to fetch next
                minHeap.append([count, tweetId, followee, i])
        
        # Convert list to heap in O(k) time where k = number of followees
        heapq.heapify(minHeap)
        
        res = []  # Store result tweet IDs
        
        # Step 2: Extract up to 10 most recent tweets
        while minHeap and len(res) < 10:
            # Pop tweet with smallest (most negative = most recent) timestamp
            count, tweetId, followee, index = heapq.heappop(minHeap)
            res.append(tweetId)
            
            # If this followee has older tweets, add next one to heap
            if index > 0:  # index-1 must be valid (>= 0)
                # Get next older tweet from same followee
                count, tweetId = self.post[followee][index - 1]
                
                # Push to heap with updated index pointing to next tweet
                heapq.heappush(minHeap, [count, tweetId, followee, index - 1])
        
        return res
    
    def follow(self, followerId: int, followeeId: int) -> None:
        # Goal: Follower starts following followee
        # Add followee to follower's follow set (set prevents duplicates)
        self.following[followerId].add(followeeId)
    
    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Goal: Follower stops following followee
        # Check if followee exists in follow set before removing (avoid KeyError)
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId, tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId, followeeId)
# obj.unfollow(followerId, followeeId)