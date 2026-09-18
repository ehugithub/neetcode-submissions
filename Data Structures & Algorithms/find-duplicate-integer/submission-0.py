class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = fast = nums[0]

        slow = nums[slow]
        fast = nums[nums[fast]]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        ptr = nums[0]
        while ptr != slow:
            ptr = nums[ptr]
            slow = nums[slow]

        return slow
        