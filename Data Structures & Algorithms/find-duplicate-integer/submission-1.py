class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # treat each number as a ptr its next one in a linked list
        # note this make sense since nums are in range [1, n].
        # a cycle of length > 1 is guaranteed to appear

        slow = fast = nums[0]

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if slow == fast: break
        
        # now need to find the cycle entrance
        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow