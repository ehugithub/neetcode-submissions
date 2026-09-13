class Twitter:

    def __init__(self):
        self.posts = {}
        self.following: Dict[int, Set[int]] = {} # user -> who they follow
        self.idx = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # need to store temporal information
        self.posts[userId] = self.posts.get(userId, []) + [(self.idx, tweetId)]
        self.idx += 1        

    def getNewsFeed(self, userId: int) -> List[int]:
        following = self.following.get(userId, [])
        own_posts = self.posts.get(userId, [])
        all_posts = own_posts + [(time, post) for followId in following for time, post in self.posts.get(followId, [])]

        heap = []
        
        for time, post in all_posts:
            heapq.heappush(heap, (time, post))
            if len(heap) > 10: heapq.heappop(heap)

        heap.sort(reverse = True)
        return[post for time, post in heap]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following.setdefault(followerId, set()).discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)