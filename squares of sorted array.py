class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Initialize pointers and result array
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        
        # Fill the result array from the end to the beginning
        for i in range(n - 1, -1, -1):
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2
            
            if left_square > right_square:
                result[i] = left_square
                left += 1
            else:
                result[i] = right_square
                right -= 1
                
        return result
