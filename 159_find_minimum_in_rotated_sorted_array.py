'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

Notice

You may assume no duplicate exists in the array.

'''

class Solution:
    """
    @param: nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):

        start, end = 0, len(nums) - 1
        target = nums[len(nums) - 1] # find the min, target = nums[-1]; find the max, target = nums[0]
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                end = mid
            else:
                start = mid

        return min(nums[start], nums[end]) #find the min, use min(); find the max, use max()


# def main():
#     s = Solution()
#     print(s.findMin([4, 5, 6, 7]))
#     print(s.findMin([4, 3, 2, 1]))
#     print(s.findMin([4, 5, 6, 7, 1, 2, 3]))
#
# if __name__ == '__main__':
#     main()
