class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        
        # First pass: copy non-zero elements
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        
        # Fill remaining with zeros
        for i in range(j, len(nums)):
            nums[i] = 0